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
    min_f = None
    max_f = None
    if d["min_f"] != "":
        min_f = d["min_f"]
    if d["max_f"] != "":
        max_f = d["max_f"]
    p = Parameters(d["idx"], d["type_f"], d["num_extrema"], d["coordinates"], d["function_values"],
                   d["degree_smoothness"], d["coefficients_abruptness"], d["constraints_x"],
                   d["constraints_y"], min_f, max_f)
    return p
