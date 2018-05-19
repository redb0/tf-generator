class Setting:
    __slots__ = ['_name', '_t', '_value']

    def __init__(self, name: str, t, value):
        self._name = name
        self._t = t
        self._value = value

    @property
    def name(self) -> str:
        return self._name

    @property
    def type_setting(self):
        return self._t

    @property
    def value(self):
        return self._value

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @type_setting.setter
    def type_setting(self, value: type) -> None:
        self._t = value

    @value.setter
    def value(self, value) -> None:
        self._value = value


class Settings:
    settings = {
        "grid_spacing": Setting("Шаг сетки", float, 0.2),
        "chart_step": Setting("Шаг графика", float, 0.05),
        "line_thickness": Setting("Толщина линий", float, 1.),
        "contour_level_step": Setting("Шаг уровня изолиний", float, 2.),
        "delta": Setting("Дельта", float, 1),
        "xlabel": Setting("Подпись оси X", str, "${x}{_1}$"),
        "ylabel": Setting("Подпись оси Y", str, "${x}{_2}$"),
        "rstride": Setting("Шаг сетки 3D графика по оси Y", int, 2),
        "cstride": Setting("Шаг сетки 3D графика по оси X", int, 2)
    }

    def __init__(self):
        pass
