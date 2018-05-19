import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from graph.mpl_canvas import MlpCanvas

from settings import Settings


class Canvas3dGraph(MlpCanvas):
    def create_graph(self, constraints_high, constraints_down, func, h=0.2, subplot_n=2, subplot_m=2):
        x, y, z = self.make_data(constraints_high, constraints_down, func, h=h)
        # TODO: добавить подпись для легенды
        self.axes = Axes3D(self.fig)
        self.axes.plot_surface(x, y, z,
                               rstride=Settings.settings['rstride'].value,
                               cstride=Settings.settings['cstride'].value,
                               cmap=plt.get_cmap('Spectral'))
        self.axes.grid()

    def make_data(self, constraints_high, constraints_down, func, h=0.2):
        x = np.arange(constraints_down[0], constraints_high[0], Settings.settings['grid_spacing'].value)
        y = np.arange(constraints_down[1], constraints_high[1], Settings.settings['grid_spacing'].value)
        xgrid, ygrid = np.meshgrid(x, y)

        zgrid = np.zeros(xgrid.shape)

        for i in range(xgrid.shape[0]):
            for j in range(xgrid.shape[1]):
                zgrid[i][j] = func([xgrid[i][j], ygrid[i][j]])

        return xgrid, ygrid, zgrid
