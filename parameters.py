

class Parameters:
    def __init__(self, idx: int, type_f: str, num_extrema: int,
                 coord, func_values, degree_smoothness, c_abruptness, constraints_x, constraints_y,
                 min_f: float = None, max_f: float = None) -> None:
        """
        Класс хранит данные описывающие функцию
                                        
        :param type_f           : 
        :param idx              : индекс тестовой функции, целое число >0 
        :param num_extrema      : количество экстремумов, целое число >= 1
        :param coord            : список координат экстремумов, длиной num_extrema
        :param func_values      : значения функции в соответствующих экстремумах, 
                                  список длиной num_extrema
        :param degree_smoothness: степень гладкости экстремумов, 
                                  список длиной num_extrema с элементами >=0
        :param c_abruptness     : 
        :param constraints_x    :
        :param constraints_y    :
        :param min_f            : 
        :param max_f            : 
        """
        self.type_f = type_f
        self.idx = idx
        self.number_extrema = num_extrema
        self.coordinates = coord
        self.function_values = func_values
        self.degree_smoothness = degree_smoothness
        self.coefficients_abruptness = c_abruptness
        self.constraints_x = constraints_x
        self.constraints_y = constraints_y
        self.min_f = min_f
        self.max_f = max_f

    def get_number_extrema(self) -> int:
        return self.number_extrema

    def get_type(self) -> str:
        return self.type_f

    def get_coordinates(self):
        return self.coordinates

    def get_function_values(self):
        return self.function_values

    def get_degree_smoothness(self):
        return self.degree_smoothness

    def get_coefficients_abruptness(self):
        return self.coefficients_abruptness

    def set_number_extrema(self, value: int):
        self.number_extrema = value

    def get_dimension(self) -> int:
        return len(self.coordinates[0])

    def set_min_f(self, value: float) -> None:
        self.min_f = value

    def set_max_f(self, value: float):
        self.max_f = value

    def get_min_f(self) -> float:
        return self.min_f

    def get_max_f(self) -> float:
        return self.max_f
