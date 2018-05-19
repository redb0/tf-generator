import json
from typing import Tuple

import validation


def parse_field(field: str, label: str):
    """
    Функция для разбора строки с одномерным числовым массивом
    :param field      : текст из поля
    :param label      : наименование поля, откуда происходило считавание
    :param print_error: функция для вывода ошибки на экран
    :return: Если проверка прошла успешно возвращает массив, иначе текст ошибки
    """
    array = parse_number_list(field, label)
    return array


def parse_coordinates(s: str, separator=';'):
    """
    Функция разбора строки, содержащей координаты экстремумов
    :param print_error: функция для вывода ошибки на экран
    :param s          : строка содержащая списки координат
    :param separator  : 
    :return: список с координатами, если преобразование успешно,
             сообщение об ошибке и пустой список в противном случае
    """
    error = ""
    coordinates_array = []
    text = s.replace(' ', '')
    if len(text) == 0:
        error = "Поле \"Координаты экстремумов\" не заполнено"
        return [], error
    text = '[' + text + ']'
    try:
        coordinates_array = json.loads(text)
    except ValueError:
        error = "Поле \"Координаты экстремумов\" заполнено некорректно"
    return coordinates_array, error


def parse_number(number, field_name: str) -> Tuple[int, str]:
    """
    Функция проверки числа на >=1.
    :param number     : число
    :param field_name : имя поля из которого считывалась строка
    :param print_error: функция для вывода ошибки на экран
    :return: если число больше либо равно 1, возвращает это число, 
             иначе выводит сообщение об ошибки и возвращает 0
    """
    if number >= 1:
        return number, ""
    else:
        error = "Поле \"" + field_name + "\" заполнено некорректно"
        return 0, error


def parse_number_list(s: str, field_name: str):
    """
    Метод разбора строки.
    Преобразует строку состоящую из чисел разделенных запятой в одномерный список.
    :param s          : строка, содержащая числа
    :param field_name : имя поля из которого считывалась строка
    :return           : возвращает одномерный список, если введена корректная строка, 
                        иначе возвращает пустой список
    """
    s = s.replace(' ', '')
    if len(s) == 0:
        error = "Поле \"" + field_name + "\" не заполнено"
        return [], error
    s = '[' + s + ']'
    try:
        values = json.loads(s)
        return values, ""
    except ValueError:
        error = "Поле \"" + field_name + "\" заполнено некорректно"
        return [], error
