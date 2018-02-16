from typing import List, Tuple

import methods.PythonMethod
from parameters import Parameters


class MethodMinPython(methods.PythonMethod.Method):
    def __init__(self):
        super().__init__()
        # self.pattern_name_func = "func"
        # self.pattern_function = ""
        self.pattern_expression = "A_ij * np.abs(x[idx] - C) ** P_ij"

        # self.main_func_str = ""
        self.func_name = ""
        self.subfunc_list = []
        self.subfunc_names_list = []

    def generate_function(self, idx: int, file_name: str, p: Parameters) -> str:
        names_subfunc, _ = self.generate_subfunc_list(idx, p)
        for func in self.subfunc_list:
            self.main_func_str = self.main_func_str + func
        _, header_func = self.construction_main_function(idx, names_subfunc)
        self.main_func_str = "import numpy as np\n\n\n" + header_func + self.main_func_str
        self.write_in_file(file_name)
        return self.main_func_str

    def generate_subfunc_list(self, idx_main_func: int, p: Parameters) -> Tuple[List[str], List[str]]:
        """
        Метод для генерации списка вспомогательных функций.
        
        :param idx_main_func: индекс тестовой функции, целое число >=0
        :param p            : экземпляр класса Parameters, где храняться параметры тестовой функции
        :return             : возвращает кортеж из двух элементов.
                              Первый элемент - список, содержащий имена вспомогательных функций.
                              Второй элемент - список, содержащий вспомогательные функции.
        """
        for i in range(p.number_extrema):
            # a_i = p.coefficients_abruptness[i * len(p.coordinates[i]): len(p.coordinates[i]) * (i + 1)]
            # p_i = p.degree_smoothness[i * len(p.coordinates[i]): len(p.coordinates[i]) * (i + 1)]
            a_i = p.coefficients_abruptness[i]
            p_i = p.degree_smoothness[i]
            expression = self.generate_expression(a_i, p.coordinates[i], p_i, p.function_values[i])
            name, func_str = self.subfunction_construction(idx_main_func, i, expression)
            self.subfunc_names_list.append(name)
            self.subfunc_list.append(func_str)
        return self.subfunc_names_list, self.subfunc_list

    def construction_main_function(self, idx: int, names_subfunc: List[str]) -> Tuple[str, str]:
        """
        Метод генерации кода для главной функции.
        Пример: m = MethodMinPython()
                m.construction_main_function(5, ["func5_0", "func5_1", "func5_2", "func5_3", "func5_4"])
        ('func5', 'def func5(x):\n    res = np.array([func5_0(x),func5_1(x),func5_2(x),func5_3(x),func5_4(x)])\n    return np.min(res)\n\n')
        
        :param idx          : индекс тестовой функции, целое число >=0
        :param names_subfunc: имена вспомогательных функций, которые входят в главную, одномерный список из строк
        :return             : возвращает кортеж из двух элементов.
                              Первый элемент - строка, содержащая имя главной функции. Пример: "func5".
                              Второй элемент - строка, содержащая код главной функции на языке Python.
        """
        self.func_name = self.pattern_name_func + str(idx)
        header = "def " + self.func_name + "(x):\n    "
        expression = "res = np.array(["
        for i in range(len(names_subfunc)):
            if i != len(names_subfunc) - 1:
                expression = expression + names_subfunc[i] + "(x), "
            else:
                expression = expression + names_subfunc[i] + "(x)"
        expression = expression + "])"
        func_str = header + expression + "\n    return np.min(res)\n\n\n"
        return self.func_name, func_str

    def generate_expression(self, a, c, p, b) -> str:
        """
        Функция для составления выражения подфункции.
        Составляет выражение вида:
                I = SUM(a_i * (|x_i - c_i|)^p_i + b_i); i = 1,...,n; p_i>=0
        Пример: m = MethodMinPython()
                m.generate_expression([5, 7], [0, 0], [0.5, 1.6], 6)
                result "5 * np.abs(x[0] - 0) ** 0.5 + 7 * np.abs(x[1] - 0) ** 1.6 + 6"
        :param a: одномерный список коэффициентов, 
                  определяющих быстроту наростания функции при отклонении от экстремума
        :param c: одномерный список, содержащий координаты экстремума
        :param p: одномерный список степеней гладкости функции в окрестности экстремума
        :param b: значение функции в точке экстремума, число типа float
        :return: возвращает выражение в виде строки
        """
        expression = self.pattern_expression
        for i in range(len(c)):
            if a[i] < 0:
                expression = expression.replace('A_ij', '(' + str(c[i]) + ')')
            else:
                expression = expression.replace('A_ij', str(a[i]))
            if c[i] < 0:
                expression = expression.replace('- C', '+ ' + str(c[i] * (-1)))
            else:
                expression = expression.replace('C', str(c[i]))
            expression = expression.replace('P_ij', str(p[i]))
            expression = expression.replace('idx', str(i))
            if i != len(c) - 1:
                expression = expression + ' + ' + self.pattern_expression
        expression = expression + ' + ' + str(b)
        return expression
