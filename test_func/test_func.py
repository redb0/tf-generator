import numpy as np

# def tryeval (f, *args, **kwargs):
#     try:
#         f(*args, **kwargs)


def get_test_function_method_min(n, a, c, p, b):
    """
    
    :param n: 
    :param a: 
    :param c: 
    :param p: 
    :param b: 
    :return: 
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
    
    :param n: 
    :param a: 
    :param c: 
    :param p: 
    :param b: 
    :return: 
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
    
    :param n: 
    :param a: 
    :param c: 
    :param b: 
    :return: 
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
