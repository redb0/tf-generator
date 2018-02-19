import json

from PyQt5.QtCore import Q_FLAGS
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog

from gui.about_dialog import AboutDialog
from gui.mainwindow_ui import UiMainWindow
import validation
from methods.method_min_python import MethodMinPython
from parameters import Parameters
import parser_field
from test_func import test_func
import service

from graph.graph_3d import Canvas3dGraph
from graph.contour_graph import CanvasContourGraph
from graph.slice_graph import CanvasSliceGraph


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        # TODO: сделать на форме поле для ввода индекса функции, сделать автоматическую генерацию имени файла
        # self.file_name = "testq.py"
        self.idx_func = 1
        self.parameters = None
        self.func = None

        # графики
        self.graph_3d = None
        self.contour_graph = None
        self.slice_graph_1 = None
        self.slice_graph_2 = None

        # кнопки
        self.ui.generate_code_python_func.clicked.connect(self.generate_code)
        self.ui.clear_field_btn.clicked.connect(self.clear_edits)
        self.ui.draw_graph_btn.clicked.connect(self.draw_graph)
        self.ui.find_func_btn.clicked.connect(self.get_func_value)
        self.ui.reset_plot.clicked.connect(self.reset_plot)
        self.ui.add_noise_btn.clicked.connect(self.add_noise)

        # действия
        self.ui.actionOpenJson.triggered.connect(self.import_json)
        self.ui.actionSave.triggered.connect(self.save_parameters_in_json)
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.open_about_dialog)

    def generate_code(self):
        # TODO: добавить комментарии
        if self.parameters is None:
            self.parameters = self.read_parameters_function()
        func_type = self.read_type()
        if not (self.parameters is None):
            if func_type == "method_min":
                method = MethodMinPython()
                file_name = service.get_file_name(self.parameters.idx, pattern="test_func", expansion=".py")
                method.generate_function(self.idx_func, file_name, self.parameters)
            elif func_type == "hyperbolic_potential":
                pass
            elif func_type == "exponential_potential":
                pass
            self.ui.statusBar.showMessage("Генерация кода успешно завершена", 5000)
            # self.parameters = None
            # method = None

    def read_parameters_function(self):
        # TODO: добавить комментарии
        self.idx_func = parser_field.parse_number(self.ui.idx_func.value(),
                                                  self.ui.idx_func_label,
                                                  self.display_error_message)
        number_extrema = parser_field.parse_number(self.ui.number_extrema.value(),
                                                   self.ui.number_extrema_label,
                                                   self.display_error_message)
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
            p = Parameters(self.idx_func,
                           number_extrema,
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
        if self.ui.method_min.isChecked():
            func_type = "method_min"
        elif self.ui.hyperbolic_potential.isChecked():
            func_type = "hyperbolic_potential"
        elif self.ui.exponential_potential.isChecked():
            func_type = "exponential_potential"
        else:
            error = "Выберите метод конструирования тестовой функции!"
            self.display_error_message(error)
        return func_type

    def display_error_message(self, error: str):
        """
        Метод вывода сообщение об ошибке на экран
        :param error: текст ошибки
        :return: -
        """
        info = QMessageBox.information(
            self, 'Внимание!', error,
            QMessageBox.Cancel, QMessageBox.Cancel
        )

    def import_json(self):
        """Метод импорта параметров тестовой функции из json-файла посредством вызова диалогового окна,
        если считывание прошло неудачно, то выводится сообщение об ошибке"""
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Открыть json-файл ...", "/home", "Json-Files (*.json);;All Files (*)"
        )

        if file_name:
            with open(file_name, 'r', encoding="utf-8") as f:
                data = f.read()
            try:
                p = json.loads(data)
                self.parameters = service.dict_in_obj(p)
                self.print_parameters_in_edit()
            except ValueError:
                error = "Файл заполнен некорректно"
                self.display_error_message(error)
            self.ui.statusBar.showMessage("Данные импортированы", 5000)

    def print_parameters_in_edit(self):
        # TODO: добавить комментарии
        self.ui.coefficients_abruptness_function.setText(str(self.parameters.coefficients_abruptness)[1:-1])
        self.ui.number_extrema.setValue(self.parameters.number_extrema)
        self.ui.function_values.setText(str(self.parameters.function_values)[1:-1])
        self.ui.degree_smoothness.setText(str(self.parameters.degree_smoothness)[1:-1])
        self.ui.coordinates.setText(str(self.parameters.coordinates)[1:-1])

    def delete_widget(self, layout):
        """
        Метод удаления виджетов из лайаута (в основном графиков)
        :param layout: контейнер типя Layout
        :return: -
        """
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

    def reset_plot(self):
        self.graph_3d = None
        self.contour_graph = None
        self.slice_graph_1 = None
        self.slice_graph_2 = None
        self.delete_widget(self.ui.v_box_3d_graph)
        self.delete_widget(self.ui.v_box_contour_graph)
        self.delete_widget(self.ui.v_box_slice_graph1)
        self.delete_widget(self.ui.v_box_slice_graph2)

    def clear_edits(self):
        """Метод очистки текстовых полей и удаления открытых графиков"""
        self.ui.coefficients_abruptness_function.setText(self.ui.translate("MainWindow", ""))
        self.ui.number_extrema.setValue(1)
        self.ui.function_values.setText(self.ui.translate("MainWindow", ""))
        self.ui.degree_smoothness.setText(self.ui.translate("MainWindow", ""))
        self.ui.coordinates.setText(self.ui.translate("MainWindow", ""))
        self.ui.constraints_x1.setText(self.ui.translate("MainWindow", ""))
        self.ui.constraints_x2.setText(self.ui.translate("MainWindow", ""))
        self.ui.slice_expr_x1.setText(self.ui.translate("MainWindow", ""))
        self.ui.slice_expr_x2.setText(self.ui.translate("MainWindow", ""))

        self.ui.max_func.setText(self.ui.translate("MainWindow", "0"))
        self.ui.min_func.setText(self.ui.translate("MainWindow", "0"))
        self.ui.amp_noise.setValue(0)
        self.ui.func_value.setText(self.ui.translate("MainWindow", "42"))
        self.ui.point.setText(self.ui.translate("MainWindow", "0, 0"))

        self.graph_3d = None
        self.contour_graph = None
        self.slice_graph_1 = None
        self.slice_graph_2 = None

        self.delete_widget(self.ui.v_box_3d_graph)
        self.delete_widget(self.ui.v_box_contour_graph)
        self.delete_widget(self.ui.v_box_slice_graph1)
        self.delete_widget(self.ui.v_box_slice_graph2)

        self.idx_func = 1
        self.parameters = None
        self.func = None

        self.ui.statusBar.showMessage("Зло не дремлет. И мы не должны.", 5000)

    def save_parameters_in_json(self):
        """Метод сохранения параметров тестовой функции в json-файл посредством вызова диалогового окна"""
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Открыть json-файл ...", "/home", "Json-Files (*.json);;All Files (*)"
        )

        if file_name:
            data = json.dumps(self.parameters.__dict__, indent=4)
            with open(file_name, 'w') as f:
                f.write(data)

        self.ui.statusBar.showMessage("Сохранение параметров успешно завершено", 2000)

    def draw_graph(self):
        self.read_parameters_function()
        # TODO: добавить комментарии
        constraints_x = parser_field.parse_number_list(self.display_error_message,
                                                       self.ui.constraints_x1.text(),
                                                       self.ui.constraints_x1_label.text())
        constraints_y = parser_field.parse_number_list(self.display_error_message,
                                                       self.ui.constraints_x2.text(),
                                                       self.ui.constraints_x2_label.text())

        expr_x1 = self.ui.slice_expr_x1.text()
        expr_x2 = self.ui.slice_expr_x2.text()

        if (constraints_x != []) and (constraints_y != []) and (not (self.parameters is None)):
            self.graph_3d = None
            self.contour_graph = None
            self.slice_graph_1 = None
            self.slice_graph_2 = None
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

                self.func = f

                self.graph_3d = Canvas3dGraph()
                graph_3d_toolbar = self.graph_3d.get_toolbar()
                self.ui.v_box_3d_graph.addWidget(graph_3d_toolbar)
                self.ui.v_box_3d_graph.addWidget(self.graph_3d)
                self.graph_3d.graph_3d(constraints_x, constraints_y, self.func, h=h)
                self.graph_3d.set_labels(xlabel="x1",
                                         ylabel="x2",
                                         title="F" + str(self.idx_func),
                                         legend_title="F" + str(self.idx_func))

                self.contour_graph = CanvasContourGraph()
                contour_graph_toolbar = self.contour_graph.get_toolbar()
                self.ui.v_box_contour_graph.addWidget(contour_graph_toolbar)
                self.ui.v_box_contour_graph.addWidget(self.contour_graph)
                self.contour_graph.contour_graph(constraints_x, constraints_y, self.func, h=h, delta=delta)
                self.contour_graph.set_labels("x1", "x2", "F" + str(self.idx_func), "F" + str(self.idx_func))

                if (expr_x1 != "") and (expr_x2 != ""):
                    self.slice_graph_1 = CanvasSliceGraph()  # self.ui.v_box_slice_graph1
                    slice_graph_1_toolbar = self.slice_graph_1.get_toolbar()
                    self.ui.v_box_slice_graph1.addWidget(slice_graph_1_toolbar)
                    self.ui.v_box_slice_graph1.addWidget(self.slice_graph_1)
                    self.slice_graph_1.graph_slice(constraints_x, constraints_y, self.func, expr_x=expr_x1, amp_noise=0)
                    self.slice_graph_1.set_labels(xlabel="x2",
                                                  ylabel="F" + str(self.idx_func),
                                                  title="x1=" + expr_x1,
                                                  legend_title="F" + str(self.idx_func))

                    self.slice_graph_2 = CanvasSliceGraph()  # self.ui.v_box_slice_graph2
                    slice_graph_2_toolbar = self.slice_graph_2.get_toolbar()
                    self.ui.v_box_slice_graph2.addWidget(slice_graph_2_toolbar)
                    self.ui.v_box_slice_graph2.addWidget(self.slice_graph_2)
                    self.slice_graph_2.graph_slice(constraints_x, constraints_y, self.func, expr_y=expr_x2, amp_noise=0)
                    self.slice_graph_2.set_labels(xlabel="x1",
                                                  ylabel="F" + str(self.idx_func),
                                                  title="x2=" + expr_x2,
                                                  legend_title="F" + str(self.idx_func))
            else:
                self.display_error_message("Выберите метод конструирования тестовой функции")
        else:
            self.display_error_message("Что-то пошло не так")

    def add_noise(self):
        # TODO: добавить комментарии
        constraints_x = parser_field.parse_number_list(self.display_error_message,
                                                       self.ui.constraints_x1.text(),
                                                       self.ui.constraints_x1_label.text())
        constraints_y = parser_field.parse_number_list(self.display_error_message,
                                                       self.ui.constraints_x2.text(),
                                                       self.ui.constraints_x2_label.text())
        expr_x1 = self.ui.slice_expr_x1.text()
        expr_x2 = self.ui.slice_expr_x2.text()
        amp_noise = self.get_amp_noise()
        if (constraints_x != []) and (constraints_y != []) and (not (self.parameters is None)) and (not (self.func is None)):
            if (expr_x1 != "") and (expr_x2 != "") and (amp_noise >= 0):
                self.slice_graph_1 = None
                self.slice_graph_2 = None
                self.delete_widget(self.ui.v_box_slice_graph1)
                self.delete_widget(self.ui.v_box_slice_graph2)

                self.slice_graph_1 = CanvasSliceGraph()
                slice_graph_1_toolbar = self.slice_graph_1.get_toolbar()
                self.ui.v_box_slice_graph1.addWidget(slice_graph_1_toolbar)
                self.ui.v_box_slice_graph1.addWidget(self.slice_graph_1)
                self.slice_graph_1.graph_slice(constraints_x, constraints_y, self.func, expr_x=expr_x1, h=0.01, amp_noise=amp_noise)
                self.slice_graph_1.set_labels(xlabel="x2",
                                              ylabel="F" + str(self.idx_func),
                                              title="x1=" + expr_x1,
                                              legend_title="F" + str(self.idx_func))

                self.slice_graph_2 = CanvasSliceGraph()
                slice_graph_2_toolbar = self.slice_graph_2.get_toolbar()
                self.ui.v_box_slice_graph2.addWidget(slice_graph_2_toolbar)
                self.ui.v_box_slice_graph2.addWidget(self.slice_graph_2)
                self.slice_graph_2.graph_slice(constraints_x, constraints_y, self.func, expr_y=expr_x2, h=0.01, amp_noise=amp_noise)
                self.slice_graph_2.set_labels(xlabel="x1",
                                              ylabel="F" + str(self.idx_func),
                                              title="x2=" + expr_x2,
                                              legend_title="F" + str(self.idx_func))

    def get_amp_noise(self):
        # TODO: добавить комментарии
        k_noise = self.ui.amp_noise.value()
        min_f = self.ui.min_func.value()
        max_f = self.ui.max_func.value()
        amp = k_noise * abs(max_f - min_f) / 2
        if amp == 0:
            error = "Что-то пошло не так!"
            self.display_error_message(error)
            return -1
        else:
            return amp

    def open_about_dialog(self):
        # TODO: добавить комментарии
        self.about = AboutDialog(flags=Q_FLAGS())
        self.about.show()

    def get_func_value(self):
        # TODO: добавить комментарии
        x = parser_field.parse_number_list(self.display_error_message,
                                           self.ui.point.text(),
                                           self.ui.point_label.text())
        if not (self.func is None):
            if len(x) == self.parameters.get_dimension():
                y = self.func(x)
                # self.ui.function_values.setText(self.ui.translate("MainWindow", ""))
                self.ui.func_value.setText(self.ui.translate("MainWindow", str(y)))
                return y
            else:
                error = "Exterminate all the bugs!"
                self.display_error_message(error)
        else:
            error = "Ученик, магия тебя ждать не будет!"
            self.display_error_message(error)

    # def translate(self, text, text_1):
    #     return QCoreApplication.translate(text, text_1)

    # def openAbout(self):
    #     self.about = About(flags=Q_FLAGS())
    #     self.about.show()

