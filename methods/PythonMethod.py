import os

from typing import Tuple


class Method:
    def __init__(self):
        self.pattern_name_func = "func"
        self.main_func_str = ""

    # def function_construction(self):
    #     """Метод конструирования главной функции"""
    #     pass

    # def generate_expression(self):
    #     """Метод генерации математического выражения для вспомогательной функции"""
    #     pass

    def subfunction_construction(self, idx_main_func: int, idx_subfunc: int, expression: str) -> Tuple[str, str]:
        """
        Метод конструирования вспомогательной функции.
        Пример: m = MethodMinPython()
                expression = "5 * np.abs(x[0] - 0) ** 0.57 * np.abs(x[1] - 0) ** 1.6 + 6"
                m.subfunction_construction(5, 0, expression)
                "def func5_0(x):\n    return 5 * np.abs(x[0] - 0) ** 0.57 * np.abs(x[1] - 0) ** 1.6 + 6\n"
        :param idx_main_func: индекс главной функции, целое число >=0
        :param idx_subfunc  : индекс вспомогательной функции, целое число >=0
        :param expression   : математическое выражение, 
                              результат вычисления которого будет возвращать 
                              сконструированная вспомогательная функция, строка
        :return             : возвращает кортеж из двух строк.
                              Первый элемент - строка, содержащая имя вспомогательной функции. Пример: "func5_0".
                              Второй элемент - строка, содержащая код вспомогательной функции на языке Python
        """
        func_name = self.pattern_name_func + str(idx_main_func) + '_' + str(idx_subfunc)
        func_str = "def " + func_name + "(x):\n"
        func_str = func_str + "    return " + expression + "\n\n\n"
        return func_name, func_str

    def write_in_file(self, file_name: str):
        """
        Метод для записи сгенерированного кода в файл.
        :param file_name: имя файла, строка. Пример "test.py"
        :return: -
        """
        script_dir = os.path.dirname(__file__)  # <-- абсолютный путь до места с программой
        rel_path = "../code/python/"  # <-- относительный путь до файла
        abs_file_path = os.path.join(script_dir, rel_path + file_name)  # <-- абсолютный путь до файла
        with open(abs_file_path, 'w', encoding="utf-8") as f:
            f.write(self.main_func_str)
