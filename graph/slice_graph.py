import numpy as np
import sympy

from graph.mpl_canvas import MlpCanvas
from service import only_one_true
from settings import Settings


class CanvasSliceGraph(MlpCanvas):
    """Класс для построения графиков срезов функции"""
    def create_graph(self, constraints_high, constraints_down, func, expression="", axes=0, h=0.2, amp_noise=0):
        # TODO: добавить подпись для легенды
        np.random.seed()

        if expression:  # expression != ""
            x, y = self.make_data(constraints_high,
                                  constraints_down,
                                  func,
                                  expression=expression,
                                  axes=axes,
                                  h=h,
                                  amp_noise=amp_noise)
            self.axes.plot(x, y, lw=Settings.settings['line_thickness'].value, label='F')
            self.axes.grid()

    def make_data(self, constraints_high, constraints_down, func, expression="", axes=0, h=0.2, amp_noise=0):
        # TODO: сделать в параметрах одно выражение expression и номер оси для среза
        """
        Метод генерации данных для построения графика
        :param expression: 
        :param axes: 
        :param constraints_high: одномерный масиив ограничений по оси x(x1)
                              Пример: [ограничение снизу, ограничение сверху]
                                      [-6, 6]
        :param constraints_down: одномерный масиив ограничений по оси y(x2)
                              Пример: [ограничение снизу, ограничение сверху]
                                      [-6, 6]
        :param func         : тестовая функции, принимающая координаты точки
        :param h            : шаг вычисления точек для графика, по умолчанию равен 0.2
        :param amp_noise    : амплитуда шума, по умолчанию равна 0
                              Если amp_noise > 0 происходит добавление аддитивной равномерно распределенной помехи 
                              к значению функции
        :return: возвращает массив координат x(x1) или y(x2) и координаты функции z, одномерные массивы
        """
        # TODO: параметрические уравнения?

        symbol = ["x2", "x1"]
        if (expression != "") and (0 <= axes < 2):
            x = np.arange(constraints_down[axes], constraints_high[axes], h)
            z = np.zeros(len(x))

            t = [expression.find(symbol[i]) != -1 for i in range(len(symbol))]
            condition, i = only_one_true(t)
            if condition:
                var_x = sympy.Symbol(symbol[i])
                expr = sympy.S(expression)
                f = sympy.lambdify(var_x, expr, "numpy")
                y = f(x)
                for i in range(len(x)):
                    if axes == 0:
                        z[i] = func([x[i], y[i]])
                    elif axes == 1:
                        z[i] = func([y[i], x[i]])
                    if amp_noise > 0:
                        z[i] = z[i] + np.random.uniform(-amp_noise, amp_noise)
                return x, z
            elif not all(t):
                y = float(expression)
                for i in range(len(x)):
                    if axes == 0:
                        z[i] = func([x[i], y])
                    elif axes == 1:
                        z[i] = func([y, x[i]])
                    if amp_noise > 0:
                        z[i] = z[i] + np.random.uniform(-amp_noise, amp_noise)
                return x, z
            else:
                return None


