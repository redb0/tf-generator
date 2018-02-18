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
    # TODO: добавить комментарии
    p = Parameters(d["idx"],
                   d["num_extrema"],
                   d["coordinates"],
                   d["function_values"],
                   d["degree_smoothness"],
                   d["coefficients_abruptness"])
    return p
