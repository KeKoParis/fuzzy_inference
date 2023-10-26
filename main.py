"""
Лабораторная работа 1
выполнили Войткус С.А., Лапковский М.А.
Дата выполнения: 26.10.2023
"""
from loguru import logger
from prettytable import PrettyTable

import checker.check as check
import inference.inference as inf
from formatting.formatting import format_rules
from formatting.formatting import format_sets
from input.input_class import GetData

logger.remove()
logger.add("program.log", format="{time} {level} {message}", level="INFO")


def str_result(result: list, curr_set: list):
    string = ""

    for j in range(len(result[0])):  # columns
        curr_value = 0
        for k in range(len(result)):  # rows
            if float(result[k][j]) > float(curr_value):
                curr_value = float(result[k][j])

        string += "(" + curr_set[j][0] + ',' + str(curr_value) + "),"

    string = "{" + string[:-1] + "}"

    return string


def make_pretty_tables(tables: dict, sets: dict):
    keys_table = tables.keys()

    formatted_tables = list()

    for i in keys_table:
        curr_table = PrettyTable()

        columns = list()
        columns.append(i)
        for j in sets[i[-1]]:
            if j[0].isalpha():
                columns.append(j[0])
        curr_table.field_names = columns

        for j in range(len(tables[i])):
            curr_table.add_row(list(sets[i[0]][j][0]) + tables[i][j])
        formatted_tables.append(curr_table)

    return formatted_tables


def main():
    logger.info("main started")

    data = GetData("input_jsons/data.json")  # data json

    sets, rules = data.get_data()
    if len(rules) == 0:
        return

    logger.info("Data got successfully")

    if not check.check_sets(sets) or not check.check_rules(rules):
        logger.error("Program finished because of invalid json input")
        return

    logger.info("Input data is correct")

    formatted_sets = format_sets(sets)
    formatted_rules = list(rules)
    format_rules(formatted_rules)

    result, inferences = inf.inference(formatted_sets, formatted_rules)

    formatted_inferences = make_pretty_tables(inferences, formatted_sets)
    formatted_results = make_pretty_tables(result, formatted_sets)

    logger.info("Tables created")

    for i in formatted_inferences:
        print(i)

    for i in formatted_results:
        print(i)

    result_keys = result.keys()

    for i in result_keys:
        print(str_result(result[i], formatted_sets[i[-1]]))


if __name__ == "__main__":
    main()
    logger.info("Program finished")
