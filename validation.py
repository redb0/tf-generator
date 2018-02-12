from parameters import Parameters


def validation_parameters(p: Parameters, func_type):
    n = p.number_extrema
    len_coord = len(p.coordinates)
    func_val_len = len(p.function_values)
    coef_len = len(p.coefficients_abruptness)
    if n < 1:
        return False
    ok = (n == len_coord) and \
         (n == func_val_len) and \
         (2 * n == len(p.degree_smoothness)) and \
         (2 * n == coef_len)
    if not ok:
        return False

    len_c = len(p.coordinates[0])
    for c in p.coordinates:
        if len_c != len(c):
            return False

    if func_type == "method_min":
        for i in range(len(p.degree_smoothness)):
            if p.degree_smoothness[i] < 0:
                return False

    if (func_type == "hyperbolic_potential") or (func_type == "exponential_potential"):
        for i in range(len(p.function_values)):
            if p.function_values[i] < 0 or p.coefficients_abruptness < 0:
                return False

    return True


def validation_num_extrema(number: int):
    """
    Функция проверки корректности ввода количества экстремумов.
    :param number: количество экстремумов, целое число >= 1
    :return: True - если параметр >= 1, в противном случае False
    """
    return number >= 1

# TODO: написать отдельные проверки для каждого поля формы
