import random
import unittest

import validation as vld
from parameters import Parameters


class ValidationTestCase(unittest.TestCase):
    random.seed()

    # validation_num
    # Классы эквивалентности для этой функции:
    # 1) валидные значения:
    #    a) целые числа >= 1;
    #    b) целые числа < 1;
    # 2) невалидные значения:
    #    a) строка
    def test_validation_num_1(self):
        """Подход анализа граничных значений"""
        n = 0
        res = vld.validation_num(n)
        self.assertEqual(res, False)

    def test_validation_num_2(self):
        """Подход анализа граничных значений"""
        n = 1
        res = vld.validation_num(n)
        self.assertEqual(res, True)

    def test_validation_num_3(self):
        """Подход случайного выбора"""
        n = random.randint(1, 10000)
        res = vld.validation_num(n)
        self.assertEqual(res, True)

    def test_validation_num_bad_data_str(self):
        n = "123"
        self.assertRaises(TypeError, vld.validation_num, n)

    # def test_bad_data_float(self):
    #     n = 1.1
    #     res = vld.validation_num(n)
    #     print(res)
    #     self.assertRaises(TypeError, vld.validation_num, n)

    # are_positive_elem_valid
    # Классы эквивалентности для этой функции:
    # 1) валидные значения:
    #    a) массив целых чисел (от 15 до 30) произвольной длины от 1 до 15
    #    b) массив чисел с плавающей запятой (от 0) произвольной длины от 1 до 20
    #    c) пустой массив ???
    #    d) массив отрицательных целых чисел произвольной длины от 1 до 10
    #    e) массив неотрицательных целых чисел с одним отрицательным
    #    f) массив из нулей
    # 2) невалидные значения:
    #    a) строка
    def test_are_positive_elem_valid_bad_data_str(self):
        n = "123"
        self.assertRaises(TypeError, vld.are_positive_elem_valid, n)

    def test_are_positive_elem_valid_1(self):
        n = random.sample(range(random.randint(15, 30)), random.randint(1, 15))
        res = vld.are_positive_elem_valid(n)
        self.assertEqual(res, True)

    def test_are_positive_elem_valid_2(self):
        n = [random.uniform(0, i + 1) for i in range(random.randint(1, 20))]
        print(n)
        res = vld.are_positive_elem_valid(n)
        self.assertEqual(res, True)

    def test_are_positive_elem_valid_3(self):
        n = []
        res = vld.are_positive_elem_valid(n)
        self.assertEqual(res, True)

    def test_are_positive_elem_valid_4(self):
        n = random.sample([-1, -2, -9, -10, -5, -7, -13, -3, -8, -4, -1, -4, -5, -7, -6], random.randint(1, 10))
        print(n)
        res = vld.are_positive_elem_valid(n)
        self.assertEqual(res, False)

    def test_are_positive_elem_valid_5(self):
        n = random.sample([1, 2, 9, 10, 5, 7, 13, 3, 8, -4], 10)
        print("are_positive_elem_valid_5", n)
        res = vld.are_positive_elem_valid(n)
        self.assertEqual(res, False)

    def test_are_positive_elem_valid_6(self):
        n = random.sample([0, 0, 0, 0, 0], random.randint(1, 5))
        print("are_positive_elem_valid_6", n)
        res = vld.are_positive_elem_valid(n)
        self.assertEqual(res, True)

    # type_valid(array: List[T], t: List[type]) -> bool
    # Классы эквивалентности для этой функции:
    # 1) валидные значения:
    #    a) массив целых чисел
    #    b) массив float'ов
    #    c) массив целых и float'ов
    #    d) пустой массив
    # 2) невалидные значения:
    #    a) строка
    def test_type_valid_int(self):
        n = random.sample(range(random.randint(10, 30)), random.randint(1, 10))
        print("type_valid_int", n)
        res = vld.type_valid(n, [int])
        self.assertEqual(res, True)

    def test_type_valid_float(self):
        n = [random.uniform(0, i + 1) for i in range(random.randint(1, 20))]
        print("type_valid_float", n)
        res = vld.type_valid(n, [float])
        self.assertEqual(res, True)

    def test_type_valid_int_and_float(self):
        n = random.sample([0, 1, 2, 3, 4, 5, 6.5, 8.345, 0.728675917, 1.1, 759, 9.3451, 2.0], random.randint(1, 10))
        print("type_valid_int_and_float", n)
        res = vld.type_valid(n, [int, float])
        self.assertEqual(res, True)

    def test_type_valid_empty_list(self):
        n = []
        res = vld.type_valid(n, [int, float])
        self.assertEqual(res, True)

    def test_type_valid_bad_data_str(self):
        n = "1234"
        res = vld.type_valid(n, [int, float])
        self.assertEqual(res, False)

    # are_subarray_len_valid
    # Классы эквивалентности для этой функции:
    # 1) валидные значения:
    #    a) строка ???
    #    b) массив с одинаковыми по длине подмассивами
    #    c) массив с одним отличающимся по длине подмассивом
    #    d) пустой массив
    # 2) невалидные значения:
    #    a) булева переменная
    def test_are_subarray_len_valid_str(self):
        n = "1234"
        res = vld.are_subarray_len_valid(n, 1)
        self.assertEqual(res, True)

    def test_are_subarray_len_valid_true(self):
        n = [[1, 0], [1, 2], [3, 4], [5, 6]]
        res = vld.are_subarray_len_valid(n, 2)
        self.assertEqual(res, True)

    def test_are_subarray_len_valid_false(self):
        n = [[1, 0], [1, 2, 5], [3, 4], [5, 6]]
        res = vld.are_subarray_len_valid(n, 2)
        self.assertEqual(res, False)

    def test_are_subarray_len_empty_list(self):
        n = []
        res = vld.are_subarray_len_valid(n, 0)
        self.assertEqual(res, True)

    def test_are_subarray_len_valid_false_2(self):
        n = [[1, 0], [1], [3, 4], [5, 6]]
        res = vld.are_subarray_len_valid(n, 2)
        self.assertEqual(res, False)

    def test_are_subarray_len_valid_false_3(self):
        n = [[1, 0], [1, 2], [3, 4], [5, 6]]
        res = vld.are_subarray_len_valid(n, 5)
        self.assertEqual(res, False)

    def test_are_subarray_len_valid_bad_data(self):
        n = True
        self.assertRaises(TypeError, vld.are_subarray_len_valid, n, 1)

    # validation_parameters(p: Parameters, func_type: str) -> bool
    # Классы эквивалентности для этой функции:
    # 1) валидные значения:
    #    a)
    #    b)
    #    c)
    #    d)
    # 2) невалидные значения:
    #    a) p = None
    #    b) p =
    def test_validation_parameters_bad_1(self):
        p = None
        f_type = "feldbaum_function"
        self.assertRaises(AttributeError, vld.validation_parameters, p, f_type)

    def test_validation_parameters_false_1(self):
        """
        n = p.number_extrema
        if n < 1:
            return False
        """
        p = Parameters(1, "feldbaum_function", 0, [], [0, 1], [], [], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)
        # self.assertRaises(AttributeError, vld.validation_parameters, p, f_type)

    def test_validation_parameters_false_2(self):
        """
        ok = (n == len(p.coordinates)) and \  # истино 
         (n == len(p.function_values)) and \  # ложно
         (n == len(p.degree_smoothness)) and \  # истино 
         (n == len(p.coefficients_abruptness))  # истино 
        if not ok:
            return False
        """
        p = Parameters(1, "feldbaum_function", 2, [[0, 0], [1, 1]], [1], [[0, 0], [1, 1]], [[0, 0], [1, 1]], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)
        # self.assertRaises(AttributeError, vld.validation_parameters, p, f_type)

    def test_validation_parameters_false_3(self):
        """
        ok = (n == len(p.coordinates)) and \  # истино 
         (n == len(p.function_values)) and \  # истино 
         (n == len(p.degree_smoothness)) and \  # ложно
         (n == len(p.coefficients_abruptness))  # истино 
        if not ok:
            return False
        """
        p = Parameters(1, "feldbaum_function", 2, [[1, 1], [1, 1]], [0, 1], [0], [1, 1], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_4(self):
        """
        ok = (n == len(p.coordinates)) and \  # истино 
         (n == len(p.function_values)) and \  # истино 
         (n == len(p.degree_smoothness)) and \  # истино 
         (n == len(p.coefficients_abruptness))  # ложно
        if not ok:
            return False
        """
        p = Parameters(1, "feldbaum_function", 2, [[1, 1], [1, 1]], [0, 1], [0, 0], [1, 1, 1], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_5(self):
        """
        if not type_valid(p.function_values, [int, float]):
            return False
        """
        p = Parameters(1, "feldbaum_function", 2, [[1, 1], [1, 1]], ['0', 1], [[1, 1], [1, 1]], [[1, 1], [1, 1]], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_6(self):
        """
        for i in range(n):
            if not type_valid(p.coordinates[i], [int, float]):
                return False 
            if not type_valid(p.degree_smoothness[i], [int, float]):
                return False  # выход
        """
        p = Parameters(1, "feldbaum_function", 2, [[0, 1], [1.5, 1]], [0, 2.3],
                       [[1.2, 'h'], ['2', 1]], [[1, 1], [1, 1]], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_7(self):
        """
        for i in range(n):
            if not type_valid(p.coordinates[i], [int, float]):
                return False  # выход
            if not type_valid(p.degree_smoothness[i], [int, float]):
                return False 
        """
        p = Parameters(1, "feldbaum_function", 2, [[1.5, 1], ['0', 'h']], [0, 1], [[1, 1], [1, 1]], [[1.4, 1], [0.1, 3]], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_8(self):
        """
        l = len(p.coordinates[0])
        if not are_subarray_len_valid(p.coordinates, l):
            return False
        """
        p = Parameters(1, "feldbaum_function", 2, [[1.5, 1], [0, -1, 0]], [0, 1], [[1, 1], [1, 1]], [[1.4, 1], [0.1, 3]], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_9(self):
        """
        if not are_subarray_len_valid(p.degree_smoothness, l):
            return False
        """
        p = Parameters(1, "feldbaum_function", 2, [[1.5, 1], [0, -1]], [0, 1], [[-2, 1], [7.9]], [[1.4, 1], [0.1, 3]], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_10(self):
        """
        if func_type == "method_min":
            for i in range(n):
                if not type_valid(p.coefficients_abruptness[i], [int, float]):
                    return False
        """
        p = Parameters(1, "feldbaum_function", 2, [[1.5, 1], [0, -1]], [0, 1],
                       [[-2, 1], [7.9, 0]], [[1.4, '6'], [0.1, 'dfg']], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_11(self):
        """
        if not are_subarray_len_valid(p.coefficients_abruptness, l):
            return False
        """
        p = Parameters(1, "feldbaum_function", 2, [[1.5, 1], [0, -1]], [0, 1],
                       [[-2, 1], [7.9, 0]], [[1.4, 7], [0.1, 1.1, 0, 6]], [], [])
        f_type = "feldbaum_function"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_12(self):
        """
        if (func_type == "hyperbolic_potential") or (func_type == "exponential_potential"):
            if not are_positive_elem_valid(p.function_values):
                return False
        """
        p = Parameters(1, "hyperbolic_potential_abs", 2, [[1.5, 1], [0, -1]], [0, -1],
                       [[-2, 1], [7.9, 0]], [[1.4, 7], [0.1, 1.1]], [], [])
        f_type = "hyperbolic_potential_abs"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_13(self):
        """
        if (func_type == "hyperbolic_potential") or (func_type == "exponential_potential"):
            ...
            if not type_valid(p.coefficients_abruptness, [int, float]):
                return False
        """
        p = Parameters(1, "exponential_potential", 2, [[1.5, 1], [0, -1]], [0, 1],
                       [[-2, 1], [7.9, 0]], [1.4, '123'], [], [])
        f_type = "exponential_potential"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_false_14(self):
        """
        if func_type not in ["method_min", "hyperbolic_potential", "exponential_potential"]:
            return False
        """
        p = Parameters(1, "exponential_potential", 2, [[1.5, 1], [0, -1]], [0, 1],
                       [[-2, 1], [7.9, 0]], [1.4, 1], [], [])
        f_type = "qwerty"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, False)

    def test_validation_parameters_true(self):
        """
        if (func_type == "hyperbolic_potential") or (func_type == "exponential_potential"):
            ...
            if not type_valid(p.coefficients_abruptness, [int, float]):
                return False
        """
        p = Parameters(1, "exponential_potential", 2, [[1.5, 1], [0, -1]], [0, 1],
                       [[-2, 1], [7.9, 0]], [1.4, 1], [], [])
        f_type = "exponential_potential"
        res = vld.validation_parameters(p, f_type)
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
