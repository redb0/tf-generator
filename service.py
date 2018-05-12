from typing import List, Tuple

from parameters import Parameters


def get_file_name(idx: int, pattern: str, expansion: str) -> str:
    """
    Функция составления имени файла с кодом тестовой функции.
    :param idx: индекс тестовой функции, целое число
    :param pattern: шаблон имени файла, строка
    :param expansion: расширение файла, строка
    :return: возвращает имя файла в виде строки
    """
    file_name = pattern + str(idx) + expansion
    return file_name


def dict_in_obj(d) -> Parameters:
    """
    Функция преобразования списка (dict) в экземпляр класса Parameters.
    :param d: список с параметрами тестовой функции (dict)
    :return: возвращает экземпляр класса Parameters
    """
    min_f = 0
    max_f = 0
    if d["min_value"] != "":
        min_f = d["min_value"]
    if d["Max_value"] != "":
        max_f = d["Max_value"]
    p = Parameters(d["index"], d["type"], d["number_extrema"], d["coordinates"], d["func_values"],
                   d["degree_smoothness"], d["coefficients_abruptness"], d["constraints_high"],
                   d["constraints_down"], d["global_min"], d["global_max"], min_f, max_f)
    return p


def only_one_true(x: List[bool]) -> Tuple[bool, int]:
    for i in range(len(x)):
        if x[i]:
            if not any(x[i+1:]):
                return True, i
            else:
                return False, -1
    return False, -1
