import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QHBoxLayout

from graph.contour_graph import CanvasContourGraph
from graph.graph_3d import Canvas3dGraph
from graph.slice_graph import CanvasSliceGraph
from test_func import test_func


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("application main window")

        self.main_widget = QWidget(self)

        a = [[6, 7], [3, 4], [6, 6], [4, 7], [3, 5]]
        c = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
        p = [[0.5, 0.6], [1.6, 1.6], [0.8, 0.8], [1.8, 1.8], [2, 2]]
        b = [0, 1, 2, 3, 4]
        n = 5

        f = test_func.get_test_function_method_min(n, a, c, p, b)

        l = QVBoxLayout(self.main_widget)
        h = QHBoxLayout(self.main_widget)

        g1 = Canvas3dGraph(self.main_widget)
        h.addWidget(g1)
        g1.create_graph([-6, 6], [-6, 6], f)

        # dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)

        l.addLayout(h)

        g2 = CanvasContourGraph(self.main_widget)
        g2.create_graph([-6, 6], [-6, 6], f)
        h.addWidget(g2)

        h1 = QHBoxLayout(self.main_widget)
        l.addLayout(h1)

        g3 = CanvasSliceGraph(self.main_widget)
        g3.create_graph([-6, 6], [-6, 6], f, expr_x="y")
        h1.addWidget(g3)

        g4 = CanvasSliceGraph(self.main_widget)
        g4.create_graph([-6, 6], [-6, 6], f, expr_y="2")
        h1.addWidget(g4)

        # sc.contour_graph(0)
        # sc.graph_slice(0, i=3)
        # sc.graph_slice(0, i=4)
        # l.addWidget(g3)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)


def main():
    qApp = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.show()
    sys.exit(qApp.exec_())


if __name__ == "__main__":
    main()
