import contextlib

import pytest

import sys

from PyQt5.QtWidgets import QApplication
from mock import patch, call

# тестируемый метод draw_graph
from gui.mainwindow import MainWindow


class Closeable:
    def close(self):
        print('closed')


type_f = ["", "method_min", "hyperbolic_potential", "exponential_potential"]
constraints = [[], [-6, 6]]
params = [True, None]
# constraints = [[], [-6], [-6, 6], [6, -6], [0, 0], [-1, 0, 1]]


@pytest.fixture(params=type_f)
def param_type_f(request):
    return request.param


@pytest.fixture(params=constraints)
def param_constraints(request):
    return request.param


@pytest.fixture(params=params)
def param_loop(request):
    return request.param


class TestDrawGraph:
    # @patch('gui.mainwindow.MainWindow.create_layout_with_graph')
    # @patch('gui.mainwindow.MainWindow.delete_widget')
    # @patch('gui.mainwindow.MainWindow.display_error_message')
    def setup(self):  # no_print_er, no_dw, no_create_graph
        # self.no_print_er = no_print_er
        # self.no_dw = no_dw
        # self.no_create_graph = no_create_graph

        self.app = QApplication(sys.argv)
        self.mw = MainWindow()
        self.mw.show()

    def teardown(self):
        with pytest.raises(SystemExit):
            with contextlib.closing(Closeable()):
                sys.exit()
        # sys.exit(self.app.exec_())

    @patch('graph.graph_3d.Canvas3dGraph')
    @patch('graph.contour_graph.CanvasContourGraph')
    @patch('graph.slice_graph.CanvasSliceGraph')
    @patch('gui.mainwindow.MainWindow.create_layout_with_graph')
    @patch('gui.mainwindow.MainWindow.delete_widget')
    @patch('gui.mainwindow.MainWindow.display_error_message')
    @patch('gui.mainwindow.MainWindow.read_type')
    @patch('parser_field.parse_number_list')
    @patch('gui.mainwindow.MainWindow.read_parameters_function')
    @patch('gui.mainwindow.MainWindow.get_func')
    def test_draw_graph(self, no_func, no_rpf, no_parser_field, no_rt, no_print_er, no_dw, no_create_graph,
                        no_slice, no_contour, no_3d,
                        param_type_f, param_constraints, param_loop):
        print(param_type_f)
        print(param_constraints)

        # замена возвращаемого функцией parser_field.parse_number_list значения
        no_parser_field.return_value = param_constraints

        # замена возвращаемого методом MainWindow.read_parameters_function значения
        no_rpf.return_value = param_loop

        def f(): pass
        # def log(s): print(s)

        no_dw.return_value = f

        no_rt.return_value = param_type_f

        no_func.return_value = f

        no_create_graph.return_value = f

        self.mw.draw_graph()

        assert no_rpf.called, "метод read_parameters_function не был вызван"
        assert no_parser_field.called, "функция parser_field.parse_number_list не была вызвана"

        if (not param_constraints) or (param_loop is None):  # param_constraints == []
            no_print_er.assert_called_once_with("Что-то пошло не так")
        else:
            calls = [call(self.mw.ui.v_box_3d_graph), call(self.mw.ui.v_box_contour_graph),
                     call(self.mw.ui.v_box_slice_graph1), call(self.mw.ui.v_box_slice_graph2)]
            no_dw.assert_has_calls(calls)

            assert no_rt.called, "метод read_type не вызван"
            if param_type_f:  # param_type_f != ""
                no_func.assert_called_once_with(param_type_f)
                no_create_graph.assert_called()
                # assert no_3d in no_create_graph.call_args_list, "некорректный вызов метода create_layout_with_graph"
                no_create_graph.assert_called()
                # assert no_contour in no_create_graph.call_args_list, "некорректный вызов метода create_layout_with_graph"

                # self.no_create_graph.assert_called()
                # assert no_slice in self.no_create_graph.call_args_list, "некорректный вызов метода create_layout_with_graph"
                # self.no_create_graph.assert_called()
                # assert no_slice in self.no_create_graph.call_args_list, "некорректный вызов метода create_layout_with_graph"
            else:
                no_print_er.assert_called_once_with("Выберите метод конструирования тестовой функции")


        # data = [('', {'uid': ['happy times']})]
        # search_s = Mock(return_value=data)
        # no_ldap.return_value = Mock(search_s=search_s)
        # count = 0
        # for i in find_users('', '', '', ''):
        #     count += 1
        #     assert i=='happy times'
        # assert count == 1


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
