from typing import List, Union


class Parameters:
    def __init__(self, idx: int, type_f: str, num_extrema: int,
                 coord, func_values, degree_smoothness, c_abruptness, constraints_x, constraints_y,
                 global_min, global_max, min_f: float = 0, max_f: float = 0) -> None:
        # FIXME: Исправить документацию
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
        self.type = type_f
        self.index = idx
        self.number_extrema = num_extrema
        self.coordinates = coord
        self.func_values = func_values
        self.degree_smoothness = degree_smoothness
        self.coefficients_abruptness = c_abruptness
        self.constraints_high = constraints_x
        self.constraints_down = constraints_y

        self._global_min = global_min
        self._global_max = global_max

        self.min_value = min_f
        self.Max_value = max_f

        self.amp_noise = (max_f - min_f) / 2
        self.dimension = len(coord[0])

    def get_number_extrema(self) -> int:
        return self.number_extrema

    def get_type(self) -> str:
        return self.type

    def get_coordinates(self):
        return self.coordinates

    def get_function_values(self):
        return self.func_values

    def get_degree_smoothness(self):
        return self.degree_smoothness

    def get_coefficients_abruptness(self):
        return self.coefficients_abruptness

    def set_number_extrema(self, value: int):
        self.number_extrema = value

    def get_dimension(self) -> int:
        return len(self.coordinates[0])

    def set_min_f(self, value: float) -> None:
        self.min_value = value

    def set_max_f(self, value: float):
        self.Max_value = value

    def get_min_f(self) -> float:
        return self.min_value

    def get_max_f(self) -> float:
        return self.Max_value

    @property
    def global_min(self) -> List[Union[int, float]]:
        return self._global_min

    @global_min.setter
    def global_min(self, value: List[Union[int, float]]) -> None:
        self._global_min = value

    @property
    def global_max(self) -> List[Union[int, float]]:
        return self._global_max

    @global_max.setter
    def global_max(self, value: List[Union[int, float]]) -> None:
        self._global_max = value
