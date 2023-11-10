"""
Лабораторная работа 1
выполнили Войткус С.А., Лапковский М.А.
норма Лукасевича
Дата выполнения: 26.10.2023
"""
import re

from loguru import logger

from exceptions.correct_input_exception import InputException


def check_sets(sets: dict):
    """
    Function checks is data correct.
    :param sets: dict
    :return:
    """
    keys = list(sets.keys())

    # for i in keys:
    #     if ord(i) > 122 or ord(i) < 97:
    #         logger.error(InputException('Set "' + i + '"'))
    #         return False

    for i in keys:
        curr_set: str = sets[i]
        if not __check_set_structure__(curr_set):
            logger.error(InputException('Set "' + i + '"'))
            return False
        if not __check_set_vars__(curr_set):
            logger.error(InputException('Set "' + i + '"'))
            return False

    logger.info("Set is correct")

    return True


__sets_pattern__ = '({((<[a-z],((0\\.[0-9]+)|0|1)>,)+)?(<[a-z],((0\\.[0-9]+)|0|1)>)})'


def __check_set_structure__(curr_set: str):
    """
    Function checks is set's structure is correct.
    :param curr_set: string of currently checking set
    :return: bool
    """
    if re.fullmatch(__sets_pattern__, curr_set) is None:
        return False

    return True


def __check_set_vars__(curr_set: str):
    """
    Function checks if set's variables are not duplicated.
    :param curr_set:
    :return:
    """
    var_list = list()
    for i in curr_set:
        if i.isalpha():
            var_list.append(i)

    if len(var_list) == len(set(var_list)):
        return True

    return False


def check_rules(rules: list):
    for i in rules:
        if not __check_rule_structure__(i):
            logger.error(InputException('Rule "' + i + '"'))
            return False
        if i[i.find('(') - 1] == i[i.rfind('(') - 1]:
            logger.error(InputException('Rule "' + i + '"'))
            return False

    logger.info("Rule is correct")

    return True


__rules_pattern__ = '^([a-z]\\([a-z]\\)~>[a-z]\\([a-z]\\))$'


def __check_rule_structure__(curr_rule: str):
    if re.fullmatch(__rules_pattern__, curr_rule) is None:
        return False

    return True
