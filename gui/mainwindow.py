import json

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog

from gui.mainwindow_ui import UiMainWindow
import validation
from methods.method_min_python import MethodMinPython
from parameters import Parameters
import parser_field
from test_func import test_func

from graph.graph_3d import Canvas3dGraph
from graph.contour_graph import CanvasContourGraph
from graph.slice_graph import CanvasSliceGraph


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        # TODO: сделать на форме поле для ввода индекса функции, сделать автоматическую генерацию имени файла
        self.file_name = "testq.py"
        self.idx_func = 10
        self.parameters = None

        # кнопки
        self.ui.generate_code_python_func.clicked.connect(self.generate_code)
        self.ui.clear_btn.clicked.connect(self.clear_edits)
        self.ui.draw_graph_btn.clicked.connect(self.draw_graph)

        # действия
        self.ui.actionOpenJson.triggered.connect(self.import_json)
        self.ui.actionSave.triggered.connect(self.save_parameters_in_json)
        self.ui.actionQuit.triggered.connect(self.close)

        # TODO: сделать нормальное удаление графиков

    def generate_code(self):
        if self.parameters is None:
            self.parameters = self.read_parameters_function()
        func_type = self.read_type()
        if not (self.parameters is None):
            if func_type == "method_min":
                method = MethodMinPython()
                method.generate_function(self.idx_func, self.file_name, self.parameters)
            elif func_type == "hyperbolic_potential":
                pass
            elif func_type == "exponential_potential":
                pass
            self.ui.statusBar.showMessage("Генерация кода успешно завершена", 5000)
            # self.parameters = None
            # method = None

    def read_parameters_function(self):
        number_extrema = parser_field.parse_number_extrema(self.ui.number_extrema, self.display_error_message)
        coordinates = parser_field.parse_coordinates(self.ui.coordinates.text(), self.display_error_message)
        function_values = parser_field.parse_field(
            self.ui.function_values.text(),
            self.ui.function_values_label.text(),
            self.display_error_message)
        degree_smoothness = parser_field.parse_field(
            self.ui.degree_smoothness.text(),
            self.ui.degree_smoothness_label.text(),
            self.display_error_message)
        coefficients = parser_field.parse_field(
            self.ui.coefficients_abruptness_function.text(),
            self.ui.coefficients_abruptness_function_label.text(),
            self.display_error_message)
        func_type = self.read_type()
        if func_type != "":
            p = Parameters(number_extrema,
                           coordinates,
                           function_values,
                           degree_smoothness,
                           coefficients)
            ok = validation.validation_parameters(p, func_type)
            if not ok:
                error = "Одно или несколько полей заполнены некорректно!"
                self.display_error_message(error)
                return None
            else:
                return p

    def read_type(self):
        """
        Функция определения метода конструирования тестовой функции.
        :return: Если выбран чекбокс method_min - тип будет "method_min"
                 Если выбран чекбокс hyperbolic_potential - тип будет "hyperbolic_potential"
                 Если выбран чекбокс exponential_potential - тип будет "exponential_potential"
                 Если не выбран ни один чекбокс выведется сообщение об ошибке
        """
        func_type = ""
        if self.ui.method_min.checkState():
            func_type = "method_min"
        elif self.ui.hyperbolic_potential.checkState():
            func_type = "hyperbolic_potential"
        elif self.ui.exponential_potential.checkState():
            func_type = "exponential_potential"
        else:
            error = "Выберите метод конструирования тестовой функции!"
            self.display_error_message(error)
        return func_type

    def display_error_message(self, error: str):
        info = QMessageBox.information(
            self, 'Внимание!', error,
            QMessageBox.Cancel, QMessageBox.Cancel
        )

    def import_json(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Открыть json-файл ...", "/home", "Json-Files (*.json);;All Files (*)"
        )

        if file_name:
            with open(file_name, 'r', encoding="utf-8") as f:
                data = f.read()
            try:
                p = json.loads(data)
                self.parameters = self.dict_in_obj(p)
                self.print_parameters_in_edit()
            except ValueError:
                error = "Файл заполнен некорректно"
                self.display_error_message(error)

    def dict_in_obj(self, d):
        p = Parameters(d["num_extrema"],
                       d["coordinates"],
                       d["function_values"],
                       d["degree_smoothness"],
                       d["coefficients_abruptness"])
        return p

    def print_parameters_in_edit(self):
        self.ui.coefficients_abruptness_function.setText(str(self.parameters.coefficients_abruptness)[1:-1])
        self.ui.number_extrema.setValue(self.parameters.number_extrema)
        self.ui.function_values.setText(str(self.parameters.function_values)[1:-1])
        self.ui.degree_smoothness.setText(str(self.parameters.degree_smoothness)[1:-1])
        self.ui.coordinates.setText(str(self.parameters.coordinates)[1:-1])

    def delete_widget(self, layout):
        # print(layout.count())
        # import matplotlib
        # matplotlib.pyplot.close('all')
        for i in range(layout.count()):
            item = layout.itemAt(i).widget()
            if item is not None:
                item.close()
                item.deleteLater()
            else:
                layout.takeAt(i)

    # def delete_widget(self, widget):
    #     for i in range(widget.count()):
    #         item = widget.itemAt(0)
    #         widget.removeItem(item)

    def clear_edits(self):
        self.ui.coefficients_abruptness_function.setText("")
        self.ui.number_extrema.setValue(1)
        self.ui.function_values.setText("")
        self.ui.degree_smoothness.setText("")
        self.ui.coordinates.setText("")
        self.ui.constraints_x1.setText("")
        self.ui.constraints_x2.setText("")
        self.ui.slice_expr_x1.setText("")
        self.ui.slice_expr_x2.setText("")

        self.delete_widget(self.ui.v_box_3d_graph)
        self.delete_widget(self.ui.v_box_contour_graph)
        self.delete_widget(self.ui.v_box_slice_graph1)
        self.delete_widget(self.ui.v_box_slice_graph2)

    def save_parameters_in_json(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Открыть json-файл ...", "/home", "Json-Files (*.json);;All Files (*)"
        )

        if file_name:
            data = json.dumps(self.parameters.__dict__, indent=4)
            with open(file_name, 'w') as f:
                f.write(data)

        self.ui.statusBar.showMessage("Сохранение параметров успешно завершено", 2000)

    def draw_graph(self):
        constraints_x = parser_field.parse_number_list(self.display_error_message,
                                                       self.ui.constraints_x1.text(),
                                                       self.ui.constraints_x1_label.text())
        constraints_y = parser_field.parse_number_list(self.display_error_message,
                                                       self.ui.constraints_x2.text(),
                                                       self.ui.constraints_x2_label.text())

        expr_x1 = self.ui.slice_expr_x1.text()
        expr_x2 = self.ui.slice_expr_x2.text()

        if (constraints_x != []) and (constraints_y != []) and (not (self.parameters is None)):
            self.delete_widget(self.ui.v_box_3d_graph)
            self.delete_widget(self.ui.v_box_contour_graph)
            self.delete_widget(self.ui.v_box_slice_graph1)
            self.delete_widget(self.ui.v_box_slice_graph2)

            h = 0.2
            delta = 0.3
            method_type = self.read_type()
            if method_type != "":
                if method_type == "method_min":
                    f = test_func.get_test_function_method_min(
                        self.parameters.get_number_extrema(),
                        self.parameters.get_coefficients_abruptness(),
                        self.parameters.get_coordinates(),
                        self.parameters.get_degree_smoothness(),
                        self.parameters.get_function_values()
                    )
                elif method_type == "hyperbolic_potential":
                    f = test_func.get_tf_hyperbolic_potential_abs(
                        self.parameters.get_number_extrema(),
                        self.parameters.get_coefficients_abruptness(),
                        self.parameters.get_coordinates(),
                        self.parameters.get_degree_smoothness(),
                        self.parameters.get_function_values()
                    )
                    h = 0.05
                    delta = 0.05
                elif method_type == "exponential_potential":
                    f = test_func.get_tf_exponential_potential(
                        self.parameters.get_number_extrema(),
                        self.parameters.get_coefficients_abruptness(),
                        self.parameters.get_coordinates(),
                        self.parameters.get_degree_smoothness(),
                        self.parameters.get_function_values()
                    )
                    h = 0.1
                    delta = 0.1

                graph_3d = Canvas3dGraph()
                graph_3d_toolbar = graph_3d.get_toolbar()
                self.ui.v_box_3d_graph.addWidget(graph_3d_toolbar)
                self.ui.v_box_3d_graph.addWidget(graph_3d)
                graph_3d.graph_3d(constraints_x, constraints_y, f, h=h)
                graph_3d.set_labels(xlabel="x1",
                                    ylabel="x2",
                                    title="F" + str(self.idx_func),
                                    legend_title="F" + str(self.idx_func))

                contour_graph = CanvasContourGraph()
                contour_graph_toolbar = contour_graph.get_toolbar()
                self.ui.v_box_contour_graph.addWidget(contour_graph_toolbar)
                self.ui.v_box_contour_graph.addWidget(contour_graph)
                contour_graph.contour_graph(constraints_x, constraints_y, f, h=h, delta=delta)
                contour_graph.set_labels("x1", "x2", "F" + str(self.idx_func), "F" + str(self.idx_func))

                if (expr_x1 != "") and (expr_x2 != ""):
                    slice_graph_1 = CanvasSliceGraph()  # self.ui.v_box_slice_graph1
                    slice_graph_1_toolbar = slice_graph_1.get_toolbar()
                    self.ui.v_box_slice_graph1.addWidget(slice_graph_1_toolbar)
                    self.ui.v_box_slice_graph1.addWidget(slice_graph_1)
                    slice_graph_1.graph_slice(constraints_x, constraints_y, f, expr_x=expr_x1)
                    slice_graph_1.set_labels(xlabel="x2",
                                             ylabel="F" + str(self.idx_func),
                                             title="x1=" + expr_x1,
                                             legend_title="F" + str(self.idx_func))

                    slice_graph_2 = CanvasSliceGraph()  # self.ui.v_box_slice_graph2
                    slice_graph_2_toolbar = slice_graph_2.get_toolbar()
                    self.ui.v_box_slice_graph2.addWidget(slice_graph_2_toolbar)
                    self.ui.v_box_slice_graph2.addWidget(slice_graph_2)
                    slice_graph_2.graph_slice(constraints_x, constraints_y, f, expr_y=expr_x2)
                    slice_graph_2.set_labels(xlabel="x1",
                                             ylabel="F" + str(self.idx_func),
                                             title="x2=" + expr_x2,
                                             legend_title="F" + str(self.idx_func))
            else:
                self.display_error_message("Выберите метод конструирования тестовой функции")
        else:
            self.display_error_message("Что-то пошло не так")
