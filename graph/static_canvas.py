import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from graph.mpl_canvas import MlpCanvas


class StaticCanvas(MlpCanvas):
    def create_graph(self, data, subplot_n=2, subplot_m=2):
        x, y, z = self.make_data_for_3d_graph()

        self.axes = Axes3D(self.fig)
        # ax = fig.add_subplot(111, projection='3d')
        self.axes.plot_surface(x, y, z,
                               rstride=4,
                               cstride=4,
                               cmap=plt.get_cmap('Spectral'))

        # self.axes.plot(t, s)

    def contour_graph(self, data, subplot_n=2, subplot_m=2):
        x, y, z = self.make_data_for_3d_graph()
        # plt.subplot(subplot_n, subplot_m, 2)

        self.axes = Axes3D(self.fig)

        self.axes.plot_surface(x, y, z,
                               rstride=4,
                               cstride=4,
                               cmap=plt.get_cmap('Spectral'))

    def graph_slice(self, data, subplot_n=2, subplot_m=2, i=3):
        x, y, z = self.make_data_for_3d_graph()
        # plt.subplot(subplot_n, subplot_m, i)

        self.axes = Axes3D(self.fig)

        self.axes.plot_surface(x, y, z,
                               rstride=4,
                               cstride=4,
                               cmap=plt.get_cmap('Spectral'))

    def make_data_for_3d_graph(self, constraints_x, constraints_y, func, h=0.2):
        x = np.arange(constraints_x[0], constraints_x[1], h)
        y = np.arange(constraints_y[0], constraints_y[1], h)
        xgrid, ygrid = np.meshgrid(x, y)

        zgrid = np.zeros((len(x), len(y)))

        for i in range(len(x)):
            for j in range(len(y)):
                zgrid[i][j] = func([x[i], y[j]])

        return xgrid, ygrid, zgrid
