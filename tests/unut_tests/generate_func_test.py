import unittest

from test_func import test_func as tf


class GenerateFuncTestCase(unittest.TestCase):
    # get_test_function_method_min(n: int, a: List[List[float]], c: List[List[float]],
    #                              p: List[List[float]], b: List[float])

    def test_method_min(self):
        a = [[1, 0.5], [2, 1], [0.8, 1.2], [0.6, 0.9], [1.5, 0.3]]
        c = [[-5, 0], [-3, 0], [-1, 0], [1, 0], [4, 0]]
        p = [[1, 1], [1, 1], [0.8, 0.8], [1.8, 1.8], [0.6, 0.6]]
        b = [1, 2, 3, 4, 5]
        n = 5
        f = tf.get_test_function_method_min(n, a, c, p, b)

        for i in range(n):
            res = f(c[i])
            # print(res)
            self.assertEqual(res, b[i])

    # get_tf_hyperbolic_potential_abs(n: int, a: List[float], c: List[List[float]],
    #                                 p: List[List[float]], b: List[float])
    def test_hyperbolic_potential_abs(self):
        a = [1, 0.5, 2, 1, 0.8]
        c = [[-5, 0], [-3, 0], [-1, 0], [1, 0], [4, 0]]
        p = [[1, 1], [1, 1], [0.8, 0.8], [1.8, 1.8], [0.6, 0.6]]
        b = [1, 2, 3, 4, 5]
        n = 5
        f = tf.get_tf_hyperbolic_potential_abs(n, a, c, p, b)

        res = []
        for i in range(n):
            res.append(f(c[i]))

        s = sorted(res)
        # print(res)
        for i in range(len(res)):
            self.assertEqual(res[i], s[i])

    # get_tf_exponential_potential(n: int, a: List[float], c: List[List[float]],
    #                              p: List[List[float]], b: List[float])
    def test_exponential_potential(self):
        a = [1, 0.5, 2, 1, 0.8]
        c = [[-5, 0], [-3, 0], [-1, 0], [1, 0], [4, 0]]
        p = [[1, 1], [1, 1], [0.8, 0.8], [1.8, 1.8], [0.6, 0.6]]
        b = [1, 2, 3, 4, 6]
        n = 5
        f = tf.get_tf_exponential_potential(n, a, c, p, b)

        res = []
        for i in range(n):
            res.append(f(c[i]))

        s = sorted(res, reverse=True)
        # print(res)
        for i in range(len(res)):
            self.assertEqual(res[i], s[i])


if __name__ == '__main__':
    unittest.main(verbosity=2)
