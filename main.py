from loguru import logger

import checker.check as check
import inference.inference as inf
from formatting.formatting import format_rules
from formatting.formatting import format_sets
from input.input_class import GetData

logger.add("program.log", format="{time} {level} {message}", level="INFO")


def main():
    logger.info("main started")

    data = GetData("input_jsons/input.json")

    sets, rules = data.get_data()
    logger.info("Data got successfully")

    if not check.check_sets(sets) or not check.check_rules(rules):
        logger.error("Program finished because of invalid json input")
        return

    logger.info("Input data is correct")

    formatted_sets = format_sets(sets)
    formatted_rules = list(rules)
    format_rules(formatted_rules)

    print(inf.inference(formatted_sets, formatted_rules))


if __name__ == "__main__":
    main()
