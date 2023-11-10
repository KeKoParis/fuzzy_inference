"""
Лабораторная работа 1
выполнили Войткус С.А., Лапковский М.А.
норма Лукасевича
Дата выполнения: 26.10.2023
"""

def format_sets(sets: dict):
    """
    Function a new dictionary more convenient to use.
    :param sets:
    :return:
    """
    formatted = dict()

    keys = sets.keys()

    for i in keys:
        curr_set: str = sets[i]
        curr_set = curr_set[1:-1]
        curr_set = curr_set.replace('>,<', '>!<')
        formatted_set = curr_set.split('!')
        for j in range(len(formatted_set)):
            formatted_set[j] = formatted_set[j].replace('<', '')
            formatted_set[j] = formatted_set[j].replace('>', '')
            formatted_set[j] = formatted_set[j].split(',')

        formatted[i] = formatted_set

    return formatted


def format_rules(rules: list):
    """
    Function makes a string of two sets names.
    "a(x)~>b(y)" to "ab"
    :param rules: list of str
    :return:
    """
    for i in range(len(rules)):
        rules[i] = rules[i][:1] + rules[i][rules[i].find('>') + 1:]
        rules[i] = rules[i][:2]
