from typing import TypeVar, List

from parameters import Parameters


# параметризация дженериков
T = TypeVar('T')


def validation_parameters(p: Parameters, func_type: str) -> bool:
    """
    Валидатор параметров тестовой функции.
    Проверяет:
    1) соответствие длин массивов с количеством экстремумов;
    2) типы хранящихся в массивах данных, допустимы только int или float;
    3) соответствие длин подмассивов (в двумерных массивах) 
       с эталонной длиной (длины всех подмассивов должны быть одинаковы)
    
    Пример корректных данных для типа method_min:
    p.number_extrema         : 3
    p.coordinates            : [[1, 1], [0, 0], [4, 2]]
    p.function_values        : [0, 1, 2]
    p.degree_smoothness      : [[2, 2], [0.5, 0.5], [1.3, 1.3]]
    p.coefficients_abruptness: [[7, 7], [5, 5], [5, 5]]
    
    Пример корректных данных для типа hyperbolic_potential:
    p.number_extrema         : 3
    p.coordinates            : [[-4, 0], [0, 0], [-3, 3]]
    p.function_values        : [0.25, 0.2, 0.1]
    p.degree_smoothness      : [[1, 1], [1, 1], [0.6, 0.6]]
    p.coefficients_abruptness: [1, 2, 0.5]
    
    Пример корректных данных для типа exponential_potential:
    p.number_extrema         : 3
    p.coordinates            : [[-3, 3], [2, 2], [-3, -4]]
    p.function_values        : [6, 5, 7]
    p.degree_smoothness      : [[0.3, 1], [1, 1], [0.6, 1.1]]
    p.coefficients_abruptness: [2, 0.5, 1.5]
    
    :param p        : экземпляр класса Parameters, содержащий параметры тестовой функции
    :param func_type: тип тестовой функции, строка.
                      Возможные типы: method_min, hyperbolic_potential, exponential_potential
    :return: возвращает True. если проверка пройдена, иначе False
    """
    n = p.number_extrema
    if n < 1:
        return False
    ok = (n == len(p.coordinates)) and \
         (n == len(p.function_values)) and \
         (n == len(p.degree_smoothness)) and \
         (n == len(p.coefficients_abruptness))
    if not ok:
        return False

    if not type_valid(p.function_values, [int, float]):
        return False
    for i in range(n):
        if not type_valid(p.coordinates[i], [int, float]):
            return False
        if not type_valid(p.degree_smoothness[i], [int, float]):
            return False

    l = len(p.coordinates[0])
    if not are_subarray_len_valid(p.coordinates, l):
        return False
    if not are_subarray_len_valid(p.degree_smoothness, l):
        return False

    if func_type == "method_min":
        # проверка типов
        for i in range(n):
            if not type_valid(p.coefficients_abruptness[i], [int, float]):
                return False
        # проверка длин подмассивов
        if not are_subarray_len_valid(p.coefficients_abruptness, l):
            return False

    if (func_type == "hyperbolic_potential") or (func_type == "exponential_potential"):
        if not are_positive_elem_valid(p.function_values):
            return False
        if not type_valid(p.coefficients_abruptness, [int, float]):
            return False

    return True


def are_subarray_len_valid(array: List[List[T]], l: int) -> bool:
    """
    Проверка длин подмассивов на соответствие эталонной длине.
    :param array: двумерный массив, требующий проверки
    :param l: эталонная длина подмассива
    :return: возвращает True. если проверка пройдена, иначе False
    """
    for subarray in array:
        if len(subarray) != l:
            return False
    return True


def type_valid(array: List[T], t: List[type]) -> bool:
    """
    Функция проверки типов элементов в массивах.
    :param array: одномерный массив
    :param t: одномерных список корректных типов
    :return: возвращает True. если проверка пройдена, иначе False
    """
    for s in array:
        if type(s) not in t:
            return False
    return True


def are_positive_elem_valid(array: List[T]) -> bool:
    """
    Проверка элементов массива на неотрицательность.
    :param array: одномерный массива, требующий проверки
    :return: возвращает True. если проверка пройдена, иначе False
    """
    for s in array:
        if s < 0:
            return False
    return True


def validation_num(number: int) -> bool:
    """
    Функция проверки корректности ввода количества экстремумов.
    :param number: количество экстремумов, целое число >= 1
    :return: True - если параметр >= 1, в противном случае False
    """
    return number >= 1


# import itertools
#
# def rangeED(*argv):
#     rlist = [range(x) for x in argv]
#     return itertools.product(*rlist)
#
# for x,y,z in rangeED(2,3,4):
# 	print(x,y,z)
