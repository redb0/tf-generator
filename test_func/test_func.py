import numpy as np

# def tryeval (f, *args, **kwargs):
#     try:
#         f(*args, **kwargs)


def get_test_function_method_min(n, a, c, p, b):
    """
    Функция-замыкание, генерирует и возвращает тестовую функцию, применяя метод Фельдбаума, 
    т. е. применяя оператор минимума к одноэкстремальным степенным функциям.
    :param n: количество экстремумов, целое число >= 1
    :param a: список коэффициентов крутости экстремумов (длиной n), чем выше значения, 
              тем быстрее функция убывает/возрастает и тем уже область экстремума, List[List[float]]
    :param c: список координат экстремумов длиной n, List[List[float]]
    :param p: список степеней гладкости в районе экстремума, 
              если 0<p[i][j]<=1 функция в точке экстремума будет угловой
    :param b: список значений функции (длиной n) в экстремуме, List[float], len(b) = n
    :return: возвращает функцию, которой необходимо передавать одномерный список координат точки, 
             возвращаемая функция вернет значение тестовой функции в данной точке
    """
    def func(x):
        l = []
        for i in range(n):
            res = 0
            for j in range(len(x)):
                res = res + a[i][j] * np.abs(x[j] - c[i][j]) ** p[i][j]
            res = res + b[i]
            l.append(res)
        res = np.array(l)
        return np.min(res)
    return func


def get_tf_hyperbolic_potential_abs(n, a, c, p, b):
    """
    
    :param n: количество экстремумов, целое число >= 1
    :param a: 
    :param c: 
    :param p: 
    :param b: 
    :return: возвращает функцию, которой необходимо передавать одномерный список координат точки, 
             возвращаемая функция вернет значение тестовой функции в данной точке
    """
    def func(x):
        value = 0
        for i in range(n):
            res = 0
            for j in range(len(x)):
                res = res + np.abs(x[j] - c[i][j]) ** p[i][j]
            res = a[i] * res + b[i]
            res = -(1 / res)
            value = value + res
        return value
    return func


def get_tf_hyperbolic_potential_sqr(n, a, c, b):
    """
    
    :param n: количество экстремумов, целое число >= 1
    :param a: 
    :param c: 
    :param b: 
    :return: возвращает функцию, которой необходимо передавать одномерный список координат точки, 
             возвращаемая функция вернет значение тестовой функции в данной точке
    """
    def func(x):
        value = 0
        for i in range(n):
            res = 0
            for j in range(len(x)):
                res = res + a[i][j] * (x[j] - c[i][j]) ** 2
            res = res + b[i]
            res = -(1 / res)
            value = value + res
        return value
    return func


def get_tf_exponential_potential(n, a, c, p, b):
    """
    
    :param n: количество экстремумов, целое число >= 1
    :param a: 
    :param c: 
    :param p: 
    :param b: 
    :return: возвращает функцию, которой необходимо передавать одномерный список координат точки, 
             возвращаемая функция вернет значение тестовой функции в данной точке
    """
    def func(x):
        value = 0
        for i in range(n):
            res = 0
            for j in range(len(x)):
                res = res + np.abs(x[j] - c[i][j]) ** p[i][j]
            res = (-b[i]) * np.exp((-a[i]) * res)
            value = value + res
        return value
    return func


def main():
    a = [1, 0.5, 2, 1, 0.8]
    c = [[-5, 0], [-3, 0], [-1, 0], [1, 0], [4, 0]]
    p = [[1, 1], [1, 1], [0.8, 0.8], [1.8, 1.8], [0.6, 0.6]]
    b = [1, 2, 3, 4, 5]
    n = 5

    x = [-5, 0]

    f = get_tf_hyperbolic_potential_abs(n, a, c, p, b)

    print(f(x))


if __name__ == '__main__':
    main()
