

class Parameters:
    def __init__(self, idx, num_extrema, coord, func_values, degree_smoothness, c_abruptness):
        """
        Класс хранит данные описывающие функцию
                                        
        :param num_extrema      : количество экстремумов, целое число >= 1
        :param coord            : список координат экстремумов, длиной num_extrema
        :param func_values      : значения функции в соответствующих экстремумах, 
                                  список длиной num_extrema
        :param degree_smoothness: степень гладкости экстремумов, 
                                  список длиной num_extrema с элементами >=0
        :param c_abruptness     : , список длиной num_extrema
        """
        # self.func_type = func_type
        self.idx = idx
        self.number_extrema = num_extrema
        self.coordinates = coord
        self.function_values = func_values
        self.degree_smoothness = degree_smoothness
        self.coefficients_abruptness = c_abruptness

    def get_number_extrema(self) -> int:
        return self.number_extrema

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

    def get_dimension(self):
        return len(self.coordinates[0])
