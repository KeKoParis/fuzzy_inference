"""
Лабораторная работа 1
выполнили Войткус С.А., Лапковский М.А.
Дата выполнения: 26.10.2023
"""
import json

from loguru import logger


class GetData:
    __path__: str
    __sets__ = dict()
    __rules__ = list()

    def __init__(self, path: str):
        """
        Init method. Put path to json here.
        :param path: path is a sting to data-json
        """
        self.__path__ = path

        logger.info("Object declared successfully")

    def __read_json__(self):
        """
        Method reads data from json and put it into class fields.
        """
        with open(self.__path__, "r") as file:
            data = json.load(file)
            try:
                self.__sets__ = data["sets"]
                self.__rules__ = data["rules"]
                logger.info("Data got successfully")
            except KeyError:
                logger.error("Invalid keys in input json")

    def get_data(self):
        """
        Method for getting data from input json.
        :return: sets type(dict), rules type(list)
        """
        self.__read_json__()

        return self.__sets__, self.__rules__
