import contextlib

import pytest

import sys

from PyQt5.QtWidgets import QApplication
from mock import patch, call

# тестируемый метод draw_graph
from gui.mainwindow import MainWindow
from parameters import Parameters


class Closeable:
    def close(self):
        print('closed')


class TestDrawGraph:
    def setup(self):
        self.app = QApplication(sys.argv)
        self.mw = MainWindow()
        self.mw.show()

    def teardown(self):
        with pytest.raises(SystemExit):
            with contextlib.closing(Closeable()):
                sys.exit()

    @patch('graph.graph_3d.Canvas3dGraph')
    @patch('graph.contour_graph.CanvasContourGraph')
    @patch('graph.slice_graph.CanvasSliceGraph')
    @patch('gui.mainwindow.MainWindow.create_layout_with_graph')
    @patch('gui.mainwindow.MainWindow.delete_widget')
    @patch('gui.mainwindow.MainWindow.read_type')
    @patch('gui.mainwindow.MainWindow.read_parameters_function')
    def test_draw_graph(self, read_parameters_function, no_rt, no_dw, no_create_graph,
                        no_slice, no_contour, no_3d):

        # замена возвращаемого методом MainWindow.read_parameters_function значения
        coord = [[-2, 4], [0, 0], [4, 4], [4, 0], [-2, 0],[0, -2], [-4, 2], [2, -4], [2, 2], [-4, -2]]
        func_value = [0, 3, 5, 6, 7, 8, 9, 10, 11, 12]
        p = Parameters(1, "feldbaum_function", 10, coord, func_value,
                       [[0.6, 1.6], [1.6, 2], [0.6, 0.6], [1.1, 1.8], [0.5, 0.5], [1.3, 1.3], [0.8, 1.2], [0.9, 0.3], [1.1, 1.7], [1.2, 0.5]],
                       [[6, 6], [6, 7], [6, 7], [5, 5], [5, 5], [5, 5], [4, 3], [2, 4], [6, 4], [3, 3]],
                       [6, 6], [-6, -6], [-2, 4], [6, 6], min_f=0, max_f=23)
        read_parameters_function.return_value = p

        def f(): pass

        no_dw.return_value = f

        no_rt.return_value = "feldbaum_function"

        no_create_graph.return_value = f

        self.mw.draw_graph()

        assert read_parameters_function.called, "метод read_parameters_function не был вызван"

        calls = [call(self.mw.ui.v_box_3d_graph), call(self.mw.ui.v_box_contour_graph),
                 call(self.mw.ui.v_box_slice_graph1), call(self.mw.ui.v_box_slice_graph2)]
        no_dw.assert_has_calls(calls)

        assert no_rt.called, "метод read_type не вызван"

        for i in range(len(func_value)):
            assert self.mw.func(coord[i]) == func_value[i]

        no_create_graph.assert_called()
        no_create_graph.assert_called()
