import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from graph.mpl_canvas import MlpCanvas


class CanvasContourGraph(MlpCanvas):
    def contour_graph(self, constraints_x, constraints_y, func, h=0.1, delta=0.2):
        x, y, z, levels = self.make_data(constraints_x, constraints_y, func, h=h, delta=delta)
        # fig, self.axes = plt.subplot()

        plt.contour(x, y, z, levels=levels)  # , levels=levels
        self.axes.grid()

    def make_data(self, constraints_x, constraints_y, func, h=0.2, delta=0.3):
        x = np.arange(constraints_x[0], constraints_x[1], h)
        y = np.arange(constraints_y[0], constraints_y[1], h)
        xgrid, ygrid = np.meshgrid(x, y)

        zgrid = np.zeros(xgrid.shape)

        for i in range(xgrid.shape[0]):
            for j in range(xgrid.shape[1]):
                zgrid[i][j] = func([xgrid[i][j], ygrid[i][j]])

        levels = []
        for i in self.get_delta(np.min(zgrid), np.max(zgrid), delta=delta, l=0.1):
            levels.append(i)

        return xgrid, ygrid, zgrid, levels

    def get_delta(self, min_z, max_z, delta=0.5, l=0.5):
        j = 1
        while min_z < max_z:
            min_z = min_z + (delta * j)
            yield min_z
            j = j + l
