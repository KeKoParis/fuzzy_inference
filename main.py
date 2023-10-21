from loguru import logger

import checker.check as check
from input.input_class import GetData

logger.add("program.log", format="{time} {level} {message}", level="INFO")


def main():
    logger.info("main started")

    data = GetData("input_json/input.json")

    sets, rules = data.get_data()
    logger.info("Data got successfully")

    if not check.check_sets(sets) or not check.check_rules(rules):
        logger.error("Program finished because of invalid json input")
        return

    logger.info("Input data is correct")


if __name__ == "__main__":
    main()
