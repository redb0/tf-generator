import json

from PyQt5.QtCore import Q_FLAGS
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QLineEdit, QDoubleSpinBox, QLabel

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
        # TODO: баг, если поля не заполнены и нажать построить графики, появляются сообщения о незаполненных полях поочереди
        # TODO: добавить кнопку сохранить как
        # TODO: добавить возможность сохранить тестовую функцию в базу (json-файл), при это сохранять инф. с максимумом и минимумом
        super().__init__(parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        self.idx_func = 1
        self.parameters = None
        self.func = None
        self.save_file_name = ""

        self.function_types = ["feldbaum_function", "hyperbolic_potential_abs", "exponential_potential"]

        # графики
        self.graph_3d = None
        self.contour_graph = None
        self.slice_graph_1 = None
        self.slice_graph_2 = None

        # кнопки
        self.ui.generate_code_python_func.clicked.connect(self.generate_code)
        self.ui.clear_field_btn.clicked.connect(self.clear_edits)
        self.ui.draw_graph_btn.clicked.connect(self.draw_graph)
        self.ui.find_func_btn.clicked.connect(
            lambda: self.get_func_value(self.ui.point, self.ui.point_label.text(), self.ui.func_value, show_message=True))
        self.ui.reset_plot.clicked.connect(self.reset_plot)
        self.ui.add_noise_btn.clicked.connect(self.add_noise)
        self.ui.save_min_max.clicked.connect(self.save_min_max)

        # действия
        self.ui.actionOpenJson.triggered.connect(self.import_json)
        self.ui.actionSave.triggered.connect(self.save_parameters_in_json)
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.open_about_dialog)

        self.ui.max_func_coord.editingFinished.connect(
            lambda: self.get_func_value(self.ui.max_func_coord, "", self.ui.max_func, show_message=False))
        self.ui.min_func_coord.editingFinished.connect(
            lambda: self.get_func_value(self.ui.min_func_coord, "", self.ui.min_func, show_message=False))

    def generate_code(self):
        # TODO: добавить комментарии
        if self.parameters is None:
            self.parameters = self.read_parameters_function()
        func_type = self.read_type()
        if not (self.parameters is None):
            if func_type == self.function_types[0]:
                method = MethodMinPython()
                file_name = service.get_file_name(self.parameters.idx, pattern="test_func", expansion=".py")
                method.generate_function(self.idx_func, file_name, self.parameters)
            elif func_type == self.function_types[1]:
                pass
            elif func_type == self.function_types[2]:
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
        constraints_high = parser_field.parse_field(self.ui.constraints_high.text(),
                                                    self.ui.constraints_x1_label.text(),
                                                    self.display_error_message)
        constraints_down = parser_field.parse_field(self.ui.constraints_down.text(),
                                                    self.ui.constraints_x2_label.text(),
                                                    self.display_error_message)
        global_min = parser_field.parse_field(self.ui.min_func_coord.text(), self.ui.min_label.text(),
                                              self.display_error_message)
        global_max = parser_field.parse_field(self.ui.max_func_coord.text(), self.ui.max_label.text(),
                                              self.display_error_message)
        if len(global_min) != len(global_max) or len(global_min) != len(coordinates[0]):
            error = "Поля координат глобального минимума или максимума заполенны некорректно!"
            self.display_error_message(error)
            return None
        if func_type != "":
            p = Parameters(self.idx_func, func_type, number_extrema, coordinates, function_values,
                           degree_smoothness, coefficients, constraints_high, constraints_down,
                           global_min, global_max, min_f=self.ui.min_func.value(), max_f=self.ui.max_func.value())
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
            func_type = self.function_types[0]
        elif self.ui.hyperbolic_potential.isChecked():
            func_type = self.function_types[1]
        elif self.ui.exponential_potential.isChecked():
            func_type = self.function_types[2]
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
        self.clear_edits()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Открыть json-файл ...", "/home", "Json-Files (*.json);;All Files (*)"
        )

        if file_name:
            self.save_file_name = file_name
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
        """Вывод параметров тестовой функции на экран"""
        del_square_brackets = slice(1, -1, 1)
        self.activate_radio_btn()
        self.ui.coefficients_abruptness_function.setText(
            str(self.parameters.coefficients_abruptness)[del_square_brackets])
        self.ui.number_extrema.setValue(self.parameters.number_extrema)
        self.ui.function_values.setText(str(self.parameters.func_values)[del_square_brackets])
        self.ui.degree_smoothness.setText(str(self.parameters.degree_smoothness)[del_square_brackets])
        self.ui.coordinates.setText(str(self.parameters.coordinates)[del_square_brackets])
        self.ui.constraints_high.setText(str(self.parameters.constraints_high)[del_square_brackets])
        self.ui.constraints_down.setText(str(self.parameters.constraints_down)[del_square_brackets])
        # if not (self.parameters.min_value is None):
        self.ui.min_func.setValue(self.parameters.min_value)
        # if not (self.parameters.Max_value is None):
        self.ui.max_func.setValue(self.parameters.Max_value)

        self.ui.min_func_coord.setText(str(self.parameters.global_min)[del_square_brackets])
        self.ui.max_func_coord.setText(str(self.parameters.global_max)[del_square_brackets])

    def activate_radio_btn(self):
        """При загрузке тестовой функции из json файла выбирает чекбокс, 
        который соответствует типу тестовой функции"""
        t = self.parameters.get_type()
        if t == self.function_types[0]:
            self.ui.method_min.setChecked(True)
        elif t == self.function_types[1]:
            self.ui.hyperbolic_potential.setChecked(True)
        elif t == self.function_types[2]:
            self.ui.exponential_potential.setChecked(True)

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
        self.ui.constraints_high.setText(self.ui.translate("MainWindow", ""))
        self.ui.constraints_down.setText(self.ui.translate("MainWindow", ""))
        self.ui.slice_expr_x1.setText(self.ui.translate("MainWindow", "0"))
        self.ui.slice_expr_x2.setText(self.ui.translate("MainWindow", "0"))

        self.ui.max_func.setValue(0)
        self.ui.min_func.setValue(0)
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
        self.save_file_name = None

        self.ui.statusBar.showMessage("Зло не дремлет. И мы не должны.", 5000)

    def save_parameters_in_json(self):
        """Метод сохранения параметров тестовой функции в json-файл посредством вызова диалогового окна"""
        # TODO: json поддерживает преобразование None в nill
        self.parameters = self.read_parameters_function()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Открыть json-файл ...", "/home", "Json-Files (*.json);;All Files (*)"
        )

        if file_name:
            self.save_file_name = file_name
            d = self.parameters.__dict__
            if d["min_value"] is None:
                d["min_value"] = 0
            if d["Max_value"] is None:
                d["Max_value"] = 0
            data = json.dumps(d, indent=4)
            with open(file_name, 'w') as f:
                f.write(data)

        self.ui.statusBar.showMessage("Сохранение параметров успешно завершено", 5000)

    def save_min_max(self):
        if self.save_file_name and (not (self.parameters is None)):
            self.parameters.set_min_f(self.ui.min_func.value())
            self.parameters.set_max_f(self.ui.max_func.value())
            with open(self.save_file_name, 'r') as f:
                js_data = json.load(f)
            with open(self.save_file_name, 'w') as f:
                js_data["min_value"] = self.parameters.get_min_f()
                js_data["Max_value"] = self.parameters.get_max_f()
                json.dump(js_data, f, indent=4)
        self.ui.statusBar.showMessage("Сохранение экстремумов успешно завершено", 5000)

    def draw_graph(self):
        self.parameters = self.read_parameters_function()
        # TODO: добавить комментарии
        constraints_high = parser_field.parse_number_list(self.display_error_message,
                                                          self.ui.constraints_high.text(),
                                                          self.ui.constraints_x1_label.text())
        constraints_down = parser_field.parse_number_list(self.display_error_message,
                                                          self.ui.constraints_down.text(),
                                                          self.ui.constraints_x2_label.text())

        expr_x1 = self.ui.slice_expr_x1.text()
        expr_x2 = self.ui.slice_expr_x2.text()

        # TODO: написать функцию validation для ограничений, != [], x[0]<x[1]
        if (constraints_high != []) and (constraints_down != []) and (self.parameters is not None):
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
                self.func = self.get_func(method_type)

                self.graph_3d = Canvas3dGraph()
                self.create_layout_with_graph(self.ui.v_box_3d_graph, self.graph_3d, constraints_high, constraints_down,
                                              h,
                                              title="F" + str(self.idx_func), legend_title="F" + str(self.idx_func))
                # graph_3d_toolbar = self.graph_3d.get_toolbar()
                # self.ui.v_box_3d_graph.addWidget(graph_3d_toolbar)
                # self.ui.v_box_3d_graph.addWidget(self.graph_3d)
                # self.graph_3d.create_graph(constraints_high, constraints_down, self.func, h=h)
                # self.graph_3d.set_labels(xlabel="x1",
                #                          ylabel="x2",
                #                          title="F" + str(self.idx_func),
                #                          legend_title="F" + str(self.idx_func))

                self.contour_graph = CanvasContourGraph()
                self.create_layout_with_graph(self.ui.v_box_contour_graph, self.contour_graph,
                                              constraints_high, constraints_down, h,
                                              title="F" + str(self.idx_func), legend_title="F" + str(self.idx_func))
                # contour_graph_toolbar = self.contour_graph.get_toolbar()
                # self.ui.v_box_contour_graph.addWidget(contour_graph_toolbar)
                # self.ui.v_box_contour_graph.addWidget(self.contour_graph)
                # self.contour_graph.create_graph(constraints_high, constraints_down, self.func, h=h, delta=delta)
                # self.contour_graph.set_labels("x1", "x2", "F" + str(self.idx_func), "F" + str(self.idx_func))

                if (expr_x1 != "") and (expr_x2 != ""):
                    self.slice_graph_1 = CanvasSliceGraph()  # self.ui.v_box_slice_graph1
                    self.create_layout_with_graph(self.ui.v_box_slice_graph1, self.slice_graph_1,
                                                  constraints_high, constraints_down, h,
                                                  expression=expr_x1, axes=0, amp_noise=0,
                                                  xlabel="x2", ylabel="F" + str(self.idx_func), title="x1=" + expr_x1, )

                    # slice_graph_1_toolbar = self.slice_graph_1.get_toolbar()
                    # self.ui.v_box_slice_graph1.addWidget(slice_graph_1_toolbar)
                    # self.ui.v_box_slice_graph1.addWidget(self.slice_graph_1)
                    # self.slice_graph_1.create_graph(constraints_high, constraints_down, self.func, expr_x=expr_x1, amp_noise=0)
                    # self.slice_graph_1.set_labels(xlabel="x2",
                    #                               ylabel="F" + str(self.idx_func),
                    #                               title="x1=" + expr_x1,
                    #                               legend_title="F" + str(self.idx_func))

                    self.slice_graph_2 = CanvasSliceGraph()  # self.ui.v_box_slice_graph2
                    self.create_layout_with_graph(self.ui.v_box_slice_graph2, self.slice_graph_2,
                                                  constraints_high, constraints_down, h,
                                                  expression=expr_x2, axes=1, amp_noise=0,
                                                  xlabel="x1", ylabel="F" + str(self.idx_func), title="x2=" + expr_x2, )
                    # slice_graph_2_toolbar = self.slice_graph_2.get_toolbar()
                    # self.ui.v_box_slice_graph2.addWidget(slice_graph_2_toolbar)
                    # self.ui.v_box_slice_graph2.addWidget(self.slice_graph_2)
                    # self.slice_graph_2.create_graph(constraints_high, constraints_down, self.func, expr_y=expr_x2, amp_noise=0)
                    # self.slice_graph_2.set_labels(xlabel="x1",
                    #                               ylabel="F" + str(self.idx_func),
                    #                               title="x2=" + expr_x2,
                    #                               legend_title="F" + str(self.idx_func))
                self.ui.statusBar.showMessage("Графики успешно построены", 5000)
            else:
                self.display_error_message("Выберите метод конструирования тестовой функции")
        else:
            self.display_error_message("Что-то пошло не так")

    def create_layout_with_graph(self, layout, graph_obj, constraints_high, constraints_down, h,
                                 xlabel="x1", ylabel="x2", title="F", legend_title="F",
                                 **kwargs):  # expr_x="", expr_y="", amp_noise=0, delta=0.3
        toolbar = graph_obj.get_toolbar()
        layout.addWidget(toolbar)
        layout.addWidget(graph_obj)
        graph_obj.create_graph(constraints_high, constraints_down, self.func, h=h,
                               **kwargs)  # expr_x=expr_x, expr_y=expr_y, amp_noise=amp_noise, delta=delta
        graph_obj.set_labels(xlabel=xlabel, ylabel=ylabel,
                             title=title,
                             legend_title=legend_title + str(self.idx_func))

    def add_noise(self):
        # TODO: добавить комментарии
        constraints_x = parser_field.parse_number_list(self.display_error_message,
                                                       self.ui.constraints_high.text(),
                                                       self.ui.constraints_x1_label.text())
        constraints_y = parser_field.parse_number_list(self.display_error_message,
                                                       self.ui.constraints_down.text(),
                                                       self.ui.constraints_x2_label.text())
        expr_x1 = self.ui.slice_expr_x1.text()
        expr_x2 = self.ui.slice_expr_x2.text()
        amp_noise = self.get_amp_noise()
        if (self.parameters is not None) and (self.func is not None) and (amp_noise >= 0):
            self.contour_graph = None
            method_type = self.read_type()
            # TODO: вынести h и delta в окно настроек
            h = 0.3
            delta = 3.5
            l = 6
            if method_type != "":
                if method_type == self.function_types[1]:
                    h = 0.05
                    delta = 0.05
                elif method_type == self.function_types[2]:
                    h = 0.1
                    delta = 0.1
            self.delete_widget(self.ui.v_box_contour_graph)
            self.contour_graph = CanvasContourGraph()
            contour_graph_toolbar = self.contour_graph.get_toolbar()
            self.ui.v_box_contour_graph.addWidget(contour_graph_toolbar)
            self.ui.v_box_contour_graph.addWidget(self.contour_graph)
            self.contour_graph.create_graph(constraints_x, constraints_y, self.func, h=h, delta=delta,
                                            amp_noise=amp_noise, l=l)
            self.contour_graph.set_labels("x1", "x2", "F" + str(self.idx_func), "F" + str(self.idx_func))

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
                self.slice_graph_1.create_graph(constraints_x, constraints_y, self.func, expression=expr_x1, h=0.01,
                                                amp_noise=amp_noise)
                self.slice_graph_1.set_labels(xlabel="x2",
                                              ylabel="F" + str(self.idx_func),
                                              title="x1=" + expr_x1,
                                              legend_title="F" + str(self.idx_func))

                self.slice_graph_2 = CanvasSliceGraph()
                slice_graph_2_toolbar = self.slice_graph_2.get_toolbar()
                self.ui.v_box_slice_graph2.addWidget(slice_graph_2_toolbar)
                self.ui.v_box_slice_graph2.addWidget(self.slice_graph_2)
                self.slice_graph_2.create_graph(constraints_x, constraints_y, self.func, expression=expr_x2, h=0.01,
                                                amp_noise=amp_noise)
                self.slice_graph_2.set_labels(xlabel="x1",
                                              ylabel="F" + str(self.idx_func),
                                              title="x2=" + expr_x2,
                                              legend_title="F" + str(self.idx_func))
                self.ui.statusBar.showMessage("На графики срезов добавлена аддитивная помеха", 5000)

    def get_func(self, method_type):
        f = None
        if method_type == self.function_types[0]:
            f = test_func.get_test_function_method_min(
                self.parameters.get_number_extrema(),
                self.parameters.get_coefficients_abruptness(),
                self.parameters.get_coordinates(),
                self.parameters.get_degree_smoothness(),
                self.parameters.get_function_values()
            )
        elif method_type == self.function_types[1]:
            f = test_func.get_tf_hyperbolic_potential_abs(
                self.parameters.get_number_extrema(),
                self.parameters.get_coefficients_abruptness(),
                self.parameters.get_coordinates(),
                self.parameters.get_degree_smoothness(),
                self.parameters.get_function_values()
            )
        elif method_type == self.function_types[2]:
            f = test_func.get_tf_exponential_potential(
                self.parameters.get_number_extrema(),
                self.parameters.get_coefficients_abruptness(),
                self.parameters.get_coordinates(),
                self.parameters.get_degree_smoothness(),
                self.parameters.get_function_values()
            )
        return f

    def get_amp_noise(self):
        """Метод расчета амплитуды шума.
        Считывает коэффициент шум/сигнал, минимум и максимум
        Амплитуда = коэффициент шум/сигнал * (максимум - минимум) / 2"""
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

    def get_func_value(self, field, name, res, show_message: bool = False):
        """расчитывает значение в точке, координаты которой введены пользователем"""
        x = parser_field.parse_number_list(self.display_error_message,
                                           field.text(),
                                           name)
        if not (self.func is None):
            if len(x) == self.parameters.get_dimension():
                y = self.func(x)
                if type(res) == QLineEdit or type(res) == QLabel:
                    res.setText(self.ui.translate("MainWindow", str(y)))
                elif type(res) == QDoubleSpinBox:
                    res.setValue(y)
                return y
            else:
                error = "Exterminate all the bugs!"
                if show_message:
                    self.display_error_message(error)
        else:
            error = "Ученик, магия тебя ждать не будет!"
            if show_message:
                self.display_error_message(error)

            # def translate(self, text, text_1):
            #     return QCoreApplication.translate(text, text_1)

            # def openAbout(self):
            #     self.about = About(flags=Q_FLAGS())
            #     self.about.show()
