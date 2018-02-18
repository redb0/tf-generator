from parameters import Parameters


def validation_parameters(p: Parameters, func_type: str):
    n = p.number_extrema
    if n < 1:
        return False
    ok = (n == len(p.coordinates)) and \
         (n == len(p.function_values)) and \
         (n == len(p.degree_smoothness)) and \
         (n == len(p.coefficients_abruptness))
    if not ok:
        return False

    len_c = len(p.coordinates[0])
    for c in p.coordinates:
        if len_c != len(c):
            return False

    if func_type == "method_min":
        if (type(p.degree_smoothness[0]) == int) or (type(p.degree_smoothness[0]) == float):
            return False
        len_p_i = len(p.degree_smoothness[0])
        for p_i in p.degree_smoothness:
            if (len_p_i != len(p_i)) or (len_p_i != len_c):
                return False
            for i in range(len(p_i)):
                if p_i[i] < 0:
                    return False

    if (func_type == "hyperbolic_potential") or (func_type == "exponential_potential"):
        for i in range(len(p.function_values)):
            if p.function_values[i] < 0:
                return False
        len_a_i = len(p.coefficients_abruptness[0])
        for a_i in p.coefficients_abruptness:
            if len_a_i != len(a_i):
                return False
            for i in range(len(a_i)):
                if a_i[i] < 0:
                    return False

    return True


def validation_num(number: int):
    """
    Функция проверки корректности ввода количества экстремумов.
    :param number: количество экстремумов, целое число >= 1
    :return: True - если параметр >= 1, в противном случае False
    """
    return number >= 1

# TODO: написать отдельные проверки для каждого поля формы
