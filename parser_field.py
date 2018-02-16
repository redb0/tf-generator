import json

import validation


def parse_field(field: str, label: str, print_error):
    array = parse_number_list(print_error, field, label)
    return array


# def parse_coefficients_abruptness(field, label, print_error, separator=';'):
#     # text = main_window.ui.coefficients_abruptness_function.text()
#     # field_name = main_window.ui.coefficients_abruptness_function_label.text()
#     array = parse_number_list(print_error, field, label)
#     return array
#
#
# def parse_function_values(main_window, separator=';'):
#     text = main_window.ui.function_values.text()
#     field_name = main_window.ui.function_values_label.text()
#     array = parse_number_list(main_window, text, field_name)
#     return array
#
#
# def parse_degree_smoothness(main_window, separator=';'):
#     text = main_window.ui.degree_smoothness.text()
#     field_name = main_window.ui.degree_smoothness_label.text()
#     array = parse_number_list(main_window, text, field_name)
#     return array


def parse_coordinates(s: str, print_error, separator=';'):
    """
    Функция разбора строки, содержащей координаты экстремумов
    :param print_error: 
    :param s: 
    :param separator  : 
    :return: список с координатами, если преобразование успешно,
             сообщение об ошибке и пустой список в противном случае
    """
    text = s.replace(' ', '')
    if len(text) == 0:
        error = "Поле \"Координаты экстремумов\" не заполнено"
        print_error(error)
        return []
    text = '[' + text + ']'
    # coordinates = text.split(separator)
    try:
        coordinates_array = json.loads(text)
        return coordinates_array
    except ValueError:
        error = "Поле \"Координаты экстремумов\" заполнено некорректно"
        print_error(error)
    # except:
    #     error = "Exterminate all the bugs!"
    #     self.display_error_message(error)

    return []


def parse_number_extrema(field, print_error) -> int:
    number = field.value()
    ok = validation.validation_num_extrema(number)
    if ok:
        return number
    else:
        error = "Поле \"Количество экстремумов\" заполнено некорректно"
        print_error(error)
        return 0


def parse_number_list(print_error, s: str, field_name: str):
    """
    Метод разбора строки.
    Преобразует строку состоящую из чисел разделенных запятой в одномерный список.
    :param print_error: 
    :param s          : строка, содержащая числа
    :param field_name : имя поля из которого считывалась строка
    :return           : возвращает одномерный список, если введена корректная строка, 
                        иначе возвращает пустой список
    """
    s = s.replace(' ', '')
    if len(s) == 0:
        error = "Поле \"" + field_name + "\" не заполнено"
        print_error(error)
        return []
    s = '[' + s + ']'
    try:
        values = json.loads(s)
        return values
    except ValueError:
        error = "Поле \"" + field_name + "\" заполнено некорректно"
        return error
        # main_window.display_error_message(error)
