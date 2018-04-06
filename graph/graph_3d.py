import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from graph.mpl_canvas import MlpCanvas


class Canvas3dGraph(MlpCanvas):
    def create_graph(self, constraints_x, constraints_y, func, h=0.2, subplot_n=2, subplot_m=2):
        x, y, z = self.make_data(constraints_x, constraints_y, func, h=0.2)
        # TODO: добавить подпись для легенды
        self.axes = Axes3D(self.fig)
        # ax = fig.add_subplot(111, projection='3d')
        self.axes.plot_surface(x, y, z,
                               rstride=4,
                               cstride=4,
                               cmap=plt.get_cmap('Spectral'))
        self.axes.grid()

    def make_data(self, constraints_x, constraints_y, func, h=0.2):
        x = np.arange(constraints_x[0], constraints_x[1], h)
        y = np.arange(constraints_y[0], constraints_y[1], h)
        xgrid, ygrid = np.meshgrid(x, y)

        zgrid = np.zeros(xgrid.shape)
        # zgrid = np.zeros(xgrid.shape)

        # for i in range(xgrid.shape[0]):
        #     for j in range(xgrid.shape[1]):
        #         zgrid[i][j] = func([xgrid[i], ygrid[j]])

        for i in range(xgrid.shape[0]):
            for j in range(xgrid.shape[1]):
                zgrid[i][j] = func([xgrid[i][j], ygrid[i][j]])

        return xgrid, ygrid, zgrid
