import json

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QCheckBox, QFileDialog

from gui.mainwindow_ui import UiMainWindow
import validation
from methods.method_min_python import MethodMinPython
from parameters import Parameters


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        # TODO: сделать на форме поле для ввода индекса функции, сделать автоматическую генерацию имени файла
        self.file_name = "test.py"
        self.idx_func = 10
        self.parameters = None

        self.ui.construct_function.clicked.connect(self.construction_clicked)
        self.ui.actionOpenJson.triggered.connect(self.import_json)
        self.ui.clear.clicked.connect(self.clear_edits)

    def construction_clicked(self):
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
            self.parameters = None
            method = None

    def read_parameters_function(self):
        number_extrema = self.parse_number_extrema()
        coordinates = self.parse_coordinates()
        function_values = self.parse_function_values()
        degree_smoothness = self.parse_degree_smoothness()
        coefficients = self.parse_coefficients_abruptness()
        func_type = self.read_type()
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

    # TODO: вынести все методы parse в отдельный файл
    def parse_number_extrema(self):
        number = self.ui.number_extrema.value()
        ok = validation.validation_num_extrema(number)
        if ok:
            return number
        else:
            error = "Поле \"Количество экстремумов\" заполнено некорректно"
            self.display_error_message(error)
            return 0

    def parse_coordinates(self, separator=';'):
        """
        Функция разбора строки, содержащей координаты экстремумов
        :param separator: 
        :return: список с координатами, если преобразование успешно,
                 сообщение об ошибке и пустой список в противном случае
        """
        text = self.ui.coordinates.text()
        text = text.replace(' ', '')
        if len(text) == 0:
            error = "Поле \"Координаты экстремумов\" не заполнено"
            self.display_error_message(error)
            return []
        text = '[' + text + ']'
        # coordinates = text.split(separator)
        try:
            coordinates_array = json.loads(text)
            return coordinates_array
        except ValueError:
            error = "Поле \"Координаты экстремумов\" заполнено некорректно"
            self.display_error_message(error)
        # except:
        #     error = "Exterminate all the bugs!"
        #     self.display_error_message(error)

        return []

    def parse_function_values(self, separator=';'):
        text = self.ui.function_values.text()
        field_name = self.ui.function_values_label.text()
        array = self.parse_number_list(text, field_name)
        return array

    def parse_degree_smoothness(self, separator=';'):
        text = self.ui.degree_smoothness.text()
        field_name = self.ui.degree_smoothness_label.text()
        array = self.parse_number_list(text, field_name)
        return array

    def parse_coefficients_abruptness(self, separator=';'):
        text = self.ui.coefficients_abruptness_function.text()
        field_name = self.ui.coefficients_abruptness_function_label.text()
        array = self.parse_number_list(text, field_name)
        return array

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

    def parse_number_list(self, s: str, field_name: str):
        """
        Метод разбора строки.
        Преобразует строку состоящую из чисел разделенных запятой в одномерный список.
        :param s         : строка, содержащая числа
        :param field_name: имя поля из которого считывалась строка
        :return          : возвращает одномерный список, если введена корректная строка, 
                           иначе возвращает пустой список
        """
        s = s.replace(' ', '')
        if len(s) == 0:
            error = "Поле \"" + field_name + "\" не заполнено"
            self.display_error_message(error)
            return []
        s = '[' + s + ']'
        try:
            values = json.loads(s)
            return values
        except ValueError:
            error = "Поле \"" + field_name + "\" заполнено некорректно"
            self.display_error_message(error)
        return []

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

    def clear_edits(self):
        self.ui.coefficients_abruptness_function.setText("")
        self.ui.number_extrema.setValue(1)
        self.ui.function_values.setText("")
        self.ui.degree_smoothness.setText("")
        self.ui.coordinates.setText("")

    # def equality_check(self):
    #     pass
