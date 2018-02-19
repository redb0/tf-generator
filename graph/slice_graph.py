import numpy as np
import sympy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from graph.mpl_canvas import MlpCanvas


class CanvasSliceGraph(MlpCanvas):
    def graph_slice(self, constraints_x, constraints_y, func, expr_x="", expr_y="", h=0.2, amp_noise=0):
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
            self.axes.plot(y, z)
            self.axes.grid()
        elif expr_y != "":
            x, z = self.make_data(constraints_x,
                                  constraints_y,
                                  func,
                                  expression_x="",
                                  expression_y=expr_y,
                                  h=h,
                                  amp_noise=amp_noise)
            self.axes.plot(x, z)
            self.axes.grid()

        # x, z = self.make_data(constraints_x, constraints_y, func, expression_x=expr_x, expression_y=expr_y, h=h)
        # plt.subplot(subplot_n, subplot_m, i)

        # TODO: доделать вычисление срезов

        # self.axes.plot(x, y, z)

    def make_data(self, constraints_x, constraints_y, func, expression_x="", expression_y="", h=0.2, amp_noise=0):
        # TODO: параметрические уравнения

        if expression_x != "":
            # x1
            y = np.arange(constraints_y[0], constraints_y[1], h)
            z = np.zeros(len(y))
            if expression_x.find('y') != -1:
                var_y = sympy.Symbol('y')
                # y = np.arange(constraints_y[0], constraints_y[1], h)
                expr = sympy.S(expression_x)
                f = sympy.lambdify(var_y, expr, "numpy")
                x = f(y)
                # z = np.zeros(len(y))
                # for i in range(len(y)):
                #     z[i] = func([x[i], y[i]])
            else:
                x = float(expression_x)
                # y = np.arange(constraints_y[0], constraints_y[1], h)
                # z = np.zeros(len(y))
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
                # x = np.arange(constraints_x[0], constraints_x[1], h)
                expr = sympy.S(expression_y)
                f = sympy.lambdify(var_x, expr, "numpy")
                y = f(x)
                # z = np.zeros(len(x))
                # for i in range(len(x)):
                #     z[i] = func([x[i], y[i]])
            else:
                y = float(expression_y)
                # x = np.arange(constraints_y[0], constraints_y[1], h)
                # z = np.zeros(len(x))
            for i in range(len(x)):
                z[i] = func([x[i], y])
                if amp_noise > 0:
                    z[i] = z[i] + np.random.uniform(-amp_noise, amp_noise)

            return x, z


