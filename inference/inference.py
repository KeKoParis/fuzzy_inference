"""
Лабораторная работа 1
выполнили Войткус С.А., Лапковский М.А.
норма Лукасевича
Дата выполнения: 26.10.2023
"""
from loguru import logger


def inference(sets: dict, rules: list):
    """
    Function solves fuzzy inference.
    :param sets:
    :param rules:
    :return:
    """
    logger.info("Inference started")

    inferences = dict()

    for i in rules:
        inferences[i] = __implication__(sets, i)

    keys = inferences.keys()

    result = dict()

    for i in keys:
        sets_names = __find_suitable_sets__(sets, i)
        for j in sets_names:
            result[j + "," + i] = __lucasievich_norma__(inferences[i], sets[j])

    return result, inferences


def __implication__(sets: dict, rule):
    """
    Function resolves classic fuzzy inference.
    :param sets: dict
    :param rule: str
    :return: fuzzy inference result matrix
    """
    set_1 = sets[rule[0]]
    set_2 = sets[rule[1]]

    result = list()

    for i in set_1:
        curr_inference = list()
        for j in set_2:
            if float(i[1]) < float(j[1]):
                curr_inference.append(1)
            else:
                # order = __find_num_order__(float(i[1]), float(j[1]))
                curr_inference.append(1 - float(i[1]) + float(j[1]))
        result.append(curr_inference)

    return result


def __find_suitable_sets__(sets: dict, rule: str):
    """
    Function find sets with the same elements.
    :param sets:
    :param rule:
    :return:
    """
    fit_set = set()

    for i in sets[rule[0]]:  # finds suitable sets elements
        fit_set.add(i[0])

    keys = sets.keys()

    set_list = list()
    for i in keys:  # find all set names with the same elements
        curr_set = set()
        for j in sets[i]:
            curr_set.add(j[0])

        if curr_set == fit_set:
            set_list.append(i)

    return set_list


def __lucasievich_norma__(inf: list, curr_set: list):
    """
    Function solves Lukasievich norma.
        min(0, a + b - 1)
    :param inf:
    :param curr_set:
    :return curr_table:
    """
    curr_table = list()

    for i in range(len(inf)):
        curr_row = list()
        for k in inf[i]:
            # order = __find_num_order__(float(curr_set[i][1]), float(k))
            curr_row.append(max(0.0, float(curr_set[i][1]) + float(k) - 1))
            # curr_row.append(min(float(k), float(curr_set[i][1])))  # is for checking to Gödel example
            # curr_set example [[a, 0.5], [b,0.4]], so curr_set[0][1] is 0.5.

        curr_table.append(curr_row)

    return curr_table


def __find_num_order__(a: float, b: float):
    """
    Function finds num order.
    """
    return min(len(str(a).split('.')[1]), len(str(b).split('.')[1]))
