from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class MlpCanvas(FigureCanvas):
    def __init__(self, parent=None, width=7, height=5, fontsize=14):
        self.set_params(fontsize)
        self.fig = plt.figure(figsize=(width, height))
        self.axes = plt.subplot()

        # self.compute_initial_figure()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

    def get_toolbar(self):
        toolbar = NavigationToolbar(self, self)
        return toolbar

    def graph_3d(self, constraints_x, constraints_y, func):
        pass

    def contour_graph(self, constraints_x, constraints_y, func):
        pass

    def graph_slice(self, constraints_x, constraints_y, func):
        pass

    def make_data(self, constraints_x, constraints_y, func, h):
        pass

    def set_labels(self, xlabel="", ylabel="", title="", legend_title=""):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title, loc='center')
        plt.legend(loc='center left', title=legend_title, bbox_to_anchor=(1, 0.5))

    def set_params(self, fontsize=14):
        params = {'legend.fontsize': fontsize,
                  'axes.labelsize': fontsize,
                  'axes.titlesize': fontsize,
                  'xtick.labelsize': fontsize - 2,
                  'ytick.labelsize': fontsize - 2}
        plt.rcParams.update(params)

    def close(self):
        plt.close()
