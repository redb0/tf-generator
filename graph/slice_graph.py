import numpy as np
import sympy
import matplotlib.pyplot as plt

from graph.mpl_canvas import MlpCanvas


class CanvasSliceGraph(MlpCanvas):
    """Класс для построения графиков срезов функции"""
    def create_graph(self, constraints_x, constraints_y, func, expr_x="", expr_y="", h=0.2, amp_noise=0):
        # TODO: добавить подпись для легенды
        np.random.seed()
        if expr_x != "":
            y, z = self.make_data(constraints_x,
                                  constraints_y,
                                  func,
                                  expression_x=expr_x,
                                  expression_y="",
                                  h=h,
                                  amp_noise=amp_noise)
            self.axes.plot(y, z, lw=0.5)
            self.axes.grid()
        elif expr_y != "":
            x, z = self.make_data(constraints_x,
                                  constraints_y,
                                  func,
                                  expression_x="",
                                  expression_y=expr_y,
                                  h=h,
                                  amp_noise=amp_noise)
            self.axes.plot(x, z, lw=0.5)
            self.axes.grid()

    def make_data(self, constraints_x, constraints_y, func, expression_x="", expression_y="", h=0.2, amp_noise=0):
        """
        Метод генерации данных для построения графика
        :param constraints_x: одномерный масиив ограничений по оси x(x1)
                              Пример: [ограничение снизу, ограничение сверху]
                                      [-6, 6]
        :param constraints_y: одномерный масиив ограничений по оси y(x2)
                              Пример: [ограничение снизу, ограничение сверху]
                                      [-6, 6]
        :param func         : тестовая функции, принимающая координаты точки
        :param expression_x : выражение среза относительно оси x(x1) в виде строки
                              Для преобразование выражения из строки применяется библиотека Sympy.
                              В выражении среза относительно оси x(x1), поддерживается переменная "y"
        :param expression_y : выражение среза относительно оси y(x2) в виде строки
                              В выражении среза относительно оси y(x2), поддерживается переменная "x"
        :param h            : шаг вычисления точек для графика, по умолчанию равен 0.2
        :param amp_noise    : амплитуда шума, по умолчанию равна 0
                              Если amp_noise > 0 происходит добавление аддитивной равномерно распределенной помехи 
                              к значению функции
        :return: возвращает массив координат x(x1) или y(x2) и координаты функции z, одномерные массивы
        """
        # TODO: параметрические уравнения
        if expression_x != "":
            # x1
            y = np.arange(constraints_y[0], constraints_y[1], h)
            z = np.zeros(len(y))
            if expression_x.find('y') != -1:
                var_y = sympy.Symbol('y')
                expr = sympy.S(expression_x)
                f = sympy.lambdify(var_y, expr, "numpy")
                x = f(y)
                # for i in range(len(y)):
                #     z[i] = func([x[i], y[i]])
            else:
                x = float(expression_x)
            for i in range(len(y)):
                z[i] = func([x, y[i]])
                if amp_noise > 0:
                    z[i] = z[i] + np.random.uniform(-amp_noise, amp_noise)
            return y, z

        if expression_y != "":
            # x2
            x = np.arange(constraints_x[0], constraints_x[1], h)
            z = np.zeros(len(x))
            if expression_y.find('x') != -1:
                var_x = sympy.Symbol('x')
                expr = sympy.S(expression_y)
                f = sympy.lambdify(var_x, expr, "numpy")
                y = f(x)
                # for i in range(len(x)):
                #     z[i] = func([x[i], y[i]])
            else:
                y = float(expression_y)
            for i in range(len(x)):
                z[i] = func([x[i], y])
                if amp_noise > 0:
                    z[i] = z[i] + np.random.uniform(-amp_noise, amp_noise)

            return x, z


