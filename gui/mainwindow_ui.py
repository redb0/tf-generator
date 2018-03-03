from PyQt5 import QtWidgets, QtCore

from PyQt5.QtWidgets import QAction


class UiMainWindow:
    def __init__(self):
        self.menuBar = None
        self.menuFile = None
        self.menuSettings = None
        self.menuHelp = None

        self.statusBar = None

        self.actionOpenJson = None
        self.actionQuit = None
        self.actionSettings = None
        self.actionAbout = None
        self.actionHelp = None
        self.actionSave = None
        self.actionOpenDocker = None

        self.method_min = None
        self.hyperbolic_potential = None
        self.exponential_potential = None

        self.methods_title = None
        self.parameters_title = None

        self.number_extrema_label = None
        self.coordinates_label = None
        self.function_values_label = None
        self.degree_smoothness_label = None
        self.coefficients_abruptness_function_label = None

        self.number_extrema = None
        self.coordinates = None
        self.function_values = None
        self.degree_smoothness = None
        self.coefficients_abruptness_function = None

        self.generate_code_python_func = None
        self.draw_graph_btn = None
        self.clear_field_btn = None

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(900, 670)
        # main_window.setWindowTitle("TF_generator v0.1")

        central_wdg = QtWidgets.QWidget()
        main_window.setCentralWidget(central_wdg)

        self.menuBar = QtWidgets.QMenuBar(main_window)
        self.menuBar.setObjectName("menuBar")

        # Файл
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        # Настройки
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        # Помощь
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")

        main_window.setMenuBar(self.menuBar)

        self.statusBar = QtWidgets.QStatusBar(main_window)
        self.statusBar.setObjectName("statusBar")
        main_window.setStatusBar(self.statusBar)

        self.actionOpenJson = QAction(main_window)
        self.actionOpenJson.setObjectName("actionOpenJson")

        self.actionSave = QAction(main_window)
        self.actionSave.setObjectName("actionSave")

        self.actionQuit = QAction(main_window)
        self.actionQuit.setObjectName("actionQuit")

        self.actionSettings = QAction(main_window)
        self.actionSettings.setObjectName("actionSettings")

        self.actionAbout = QAction(main_window)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QAction(main_window)
        self.actionHelp.setObjectName("actionHelp")

        self.menuFile.addAction(self.actionOpenJson)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.menuSettings.addAction(self.actionSettings)
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.methods_title = QtWidgets.QLabel()
        self.methods_title.setMaximumHeight(20)

        # Методы построения функций
        self.method_min = QtWidgets.QRadioButton()
        self.hyperbolic_potential = QtWidgets.QRadioButton()
        self.exponential_potential = QtWidgets.QRadioButton()

        self.layout_methods = QtWidgets.QVBoxLayout()
        self.layout_methods.addWidget(self.methods_title)
        self.layout_methods.addWidget(self.method_min)
        self.layout_methods.addWidget(self.hyperbolic_potential)
        self.layout_methods.addWidget(self.exponential_potential)
        self.layout_methods.addStretch(1)

        scroll_methods = QtWidgets.QScrollArea()
        scroll_widget_1 = QtWidgets.QWidget()
        scroll_widget_1.setLayout(self.layout_methods)
        scroll_methods.setWidget(scroll_widget_1)
        scroll_methods.setWidgetResizable(True)
        scroll_methods.setMaximumWidth(275)

        # Параметры функци
        self.idx_func_label = QtWidgets.QLabel()
        self.number_extrema_label = QtWidgets.QLabel()
        self.coordinates_label = QtWidgets.QLabel()
        self.function_values_label = QtWidgets.QLabel()
        self.degree_smoothness_label = QtWidgets.QLabel()
        self.coefficients_abruptness_function_label = QtWidgets.QLabel()

        self.idx_func = QtWidgets.QSpinBox()
        self.idx_func.setMinimum(1)
        self.idx_func.setMaximum(1000)
        self.idx_func.setSingleStep(1)
        self.number_extrema = QtWidgets.QSpinBox()
        self.number_extrema.setMinimum(1)
        self.number_extrema.setMaximum(100)
        self.number_extrema.setSingleStep(1)
        self.coordinates = QtWidgets.QLineEdit()
        self.function_values = QtWidgets.QLineEdit()
        self.degree_smoothness = QtWidgets.QLineEdit()
        self.coefficients_abruptness_function = QtWidgets.QLineEdit()

        frame_1 = QtWidgets.QFrame()
        frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_2 = QtWidgets.QFrame()
        frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_3 = QtWidgets.QFrame()
        frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_4 = QtWidgets.QFrame()
        frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_4.setFrameShadow(QtWidgets.QFrame.Raised)

        self.parameters_title = QtWidgets.QLabel()
        form_1 = QtWidgets.QFormLayout(frame_1)
        form_1.addRow(self.parameters_title)
        form_1.addRow(self.idx_func_label, self.idx_func)
        form_1.addRow(self.number_extrema_label, self.number_extrema)
        form_1.addRow(self.coordinates_label, self.coordinates)
        form_1.addRow(self.function_values_label, self.function_values)
        form_1.addRow(self.degree_smoothness_label, self.degree_smoothness)
        form_1.addRow(
            self.coefficients_abruptness_function_label,
            self.coefficients_abruptness_function
        )

        # self.layout_methods.addLayout(self.form)

        # frame_2 = QtWidgets.QFrame()
        # frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # frame_2.setObjectName("frame_2")

        self.graph_title = QtWidgets.QLabel()
        self.constraints_x1_label = QtWidgets.QLabel()
        self.constraints_x1_label.setMinimumWidth(220)
        self.constraints_x1 = QtWidgets.QLineEdit()
        # self.constraints_x1.setMaximumWidth(100)
        self.constraints_x2_label = QtWidgets.QLabel()
        self.constraints_x2 = QtWidgets.QLineEdit()
        # self.constraints_x2.setMaximumWidth(100)
        self.slice_expr_x1_label = QtWidgets.QLabel()
        self.slice_expr_x1 = QtWidgets.QLineEdit()
        self.slice_expr_x2_label = QtWidgets.QLabel()
        self.slice_expr_x2 = QtWidgets.QLineEdit()

        form_2 = QtWidgets.QFormLayout(frame_2)
        form_2.addRow(self.graph_title)
        form_2.addRow(self.constraints_x1_label, self.constraints_x1)
        form_2.addRow(self.constraints_x2_label, self.constraints_x2)
        form_2.addRow(self.slice_expr_x1_label, self.slice_expr_x1)
        form_2.addRow(self.slice_expr_x2_label, self.slice_expr_x2)

        self.max_label = QtWidgets.QLabel()
        self.max_func = QtWidgets.QDoubleSpinBox()
        self.max_func.setMinimum(-2000)
        self.max_func.setMaximum(2000)
        self.max_func.setSingleStep(0.01)
        self.max_label.setMinimumWidth(220)
        # self.max_func.setMaximumWidth(100)
        self.min_label = QtWidgets.QLabel()
        self.min_func = QtWidgets.QDoubleSpinBox()
        self.min_func.setMinimum(-2000)
        self.min_func.setMaximum(2000)
        self.min_func.setSingleStep(0.01)
        # self.min_func.setMaximumWidth(100)
        self.amp_noise_label = QtWidgets.QLabel()
        self.amp_noise_label.setMinimumWidth(220)
        self.amp_noise = QtWidgets.QDoubleSpinBox()
        self.amp_noise.setMinimum(0)
        self.amp_noise.setMaximum(50)
        self.amp_noise.setSingleStep(0.1)
        # self.amp_noise.setMaximumWidth(100)
        self.add_noise_btn = QtWidgets.QPushButton()
        self.save_min_max = QtWidgets.QPushButton()
        # self.add_noise_btn.setMaximumWidth(150)

        self.point_label = QtWidgets.QLabel()
        self.point_label.setMinimumWidth(220)
        self.point = QtWidgets.QLineEdit()
        self.func_value_label = QtWidgets.QLabel()
        self.func_value = QtWidgets.QLabel()
        self.find_func_btn = QtWidgets.QPushButton()

        form_3 = QtWidgets.QFormLayout(frame_3)
        form_3.addRow(self.min_label, self.min_func)
        form_3.addRow(self.max_label, self.max_func)
        form_3.addRow(self.amp_noise_label, self.amp_noise)
        form_3.addRow(self.save_min_max, self.add_noise_btn)

        form_4 = QtWidgets.QFormLayout(frame_4)
        form_4.addRow(self.point_label, self.point)
        form_4.addRow(self.func_value_label, self.func_value)
        form_4.addRow(self.find_func_btn)

        layout_parameters = QtWidgets.QVBoxLayout()
        # layout_parameters.addLayout(form_1)
        # layout_parameters.addLayout(form_2)
        # layout_parameters.addLayout(form_3)
        layout_parameters.addWidget(frame_1)
        layout_parameters.addWidget(frame_2)
        layout_parameters.addWidget(frame_3)
        layout_parameters.addWidget(frame_4)
        layout_parameters.addStretch(1)

        scroll_parameters = QtWidgets.QScrollArea()
        scroll_widget_2 = QtWidgets.QWidget()
        scroll_widget_2.setLayout(layout_parameters)
        scroll_parameters.setWidget(scroll_widget_2)
        scroll_parameters.setWidgetResizable(True)

        # кнопки
        self.generate_code_python_func = QtWidgets.QPushButton()
        self.draw_graph_btn = QtWidgets.QPushButton()
        self.clear_field_btn = QtWidgets.QPushButton()
        self.reset_plot = QtWidgets.QPushButton()

        # расположение кнопок и всех остальных виджетов (сетка)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(scroll_methods)
        h_box.addWidget(scroll_parameters)

        h_box_button = QtWidgets.QHBoxLayout()
        h_box_button.addStretch(1)
        h_box_button.addWidget(self.generate_code_python_func)
        h_box_button.addWidget(self.draw_graph_btn)
        h_box_button.addWidget(self.clear_field_btn)
        h_box_button.addWidget(self.reset_plot)

        main_v_box = QtWidgets.QVBoxLayout()
        main_v_box.addLayout(h_box)
        main_v_box.addLayout(h_box_button)

        self.docker = QtWidgets.QDockWidget()

        self.actionOpenDocker = self.docker.toggleViewAction()
        self.menuSettings.addAction(self.actionOpenDocker)

        main_window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.docker)
        self.docker.setAllowedAreas(QtCore.Qt.RightDockWidgetArea | QtCore.Qt.LeftDockWidgetArea)

        central_widget_docker = QtWidgets.QWidget()
        self.docker.setWidget(central_widget_docker)

        l = QtWidgets.QVBoxLayout()
        h1 = QtWidgets.QHBoxLayout()
        h2 = QtWidgets.QHBoxLayout()

        l.addLayout(h1)
        l.addLayout(h2)
        central_widget_docker.setLayout(l)

        self.v_box_3d_graph = QtWidgets.QVBoxLayout()
        self.v_box_contour_graph = QtWidgets.QVBoxLayout()
        h1.addLayout(self.v_box_3d_graph)
        h1.addLayout(self.v_box_contour_graph)

        self.v_box_slice_graph1 = QtWidgets.QVBoxLayout()
        self.v_box_slice_graph2 = QtWidgets.QVBoxLayout()
        h2.addLayout(self.v_box_slice_graph1)
        h2.addLayout(self.v_box_slice_graph2)

        central_wdg.setLayout(main_v_box)

        # self.actionQuit.triggered.connect(main_window.close)
        self.retranslate_ui(main_window)

    def retranslate_ui(self, main_window):
        # _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(self.translate("MainWindow", "TFGenerator"))
        self.menuFile.setTitle(self.translate("MainWindow", "Файл"))

        self.actionOpenJson.setText(self.translate("MainWindow", "Импорт параметров"))
        self.actionOpenJson.setStatusTip(self.translate("MainWindow", "Импорт параметров из Json"))
        self.actionOpenJson.setShortcut(self.translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(self.translate("MainWindow", "Сохранить параметры"))
        self.actionSave.setStatusTip(self.translate("MainWindow", "Сохранить парметры тестовой функции в json файле"))
        self.actionQuit.setText(self.translate("MainWindow", "Выход"))
        self.actionQuit.setShortcut(self.translate("MainWindow", "Ctrl+Q"))

        # self.actionSettings.setText(self.translate("MainWindow", "Настройки"))

        # Справка
        self.menuHelp.setTitle(self.translate("MainWindow", "Справка"))
        self.actionHelp.setText(self.translate("MainWindow", "Справка"))
        self.actionHelp.setShortcut(self.translate("MainWindow", "F1"))
        self.actionAbout.setText(self.translate("MainWindow", "О программе"))

        # Настройки
        self.menuSettings.setTitle(self.translate("MainWindow", "Настройки"))
        self.actionSettings.setText(self.translate("MainWindow", "Настройки"))
        self.actionOpenDocker.setText(self.translate("MainWindow", "Показать докеры"))

        self.method_min.setText(self.translate("MainWindow", "Метод Фельдбаума (оператор min)"))
        self.hyperbolic_potential.setText(self.translate("MainWindow", "Гиперболическая потенциальная функция"))
        self.exponential_potential.setText(self.translate("MainWindow", "Экспоненциальная потенциальная функция"))
        self.methods_title.setText(self.translate("MainWindow", "Методы построения функций"))
        self.parameters_title.setText(self.translate("MainWindow", "Параметры функции"))

        self.idx_func_label.setText(self.translate("MainWindow", "Индекс тестовой функции"))
        self.number_extrema_label.setText(self.translate("MainWindow", "Количество экстремумов"))
        self.coordinates_label.setText(self.translate("MainWindow", "Координаты экстремумов"))
        self.function_values_label.setText(self.translate("MainWindow", "Значения функции"))
        self.degree_smoothness_label.setText(self.translate("MainWindow", "Степени гладкости функции"))
        self.coefficients_abruptness_function_label.setText(self.translate("MainWindow", "Коэффициенты крутости функции"))

        self.graph_title.setText(self.translate("MainWindow", "Параметры графиков функции"))
        self.constraints_x1_label.setText(self.translate("MainWindow", "Ограничения по оси X(x1) снизу и сверху"))
        self.constraints_x2_label.setText(self.translate("MainWindow", "Ограничения по оси Y(x2) снизу и сверху"))
        self.slice_expr_x1_label.setText(self.translate("MainWindow", "Выражение среза относительно оси X(x1)"))
        self.slice_expr_x2_label.setText(self.translate("MainWindow", "Выражение среза относительно оси Y(x2)"))

        self.constraints_x1.setText(self.translate("MainWindow", "-6, 6"))
        self.constraints_x2.setText(self.translate("MainWindow", "-6, 6"))
        self.slice_expr_x1.setText(self.translate("MainWindow", "0"))
        self.slice_expr_x2.setText(self.translate("MainWindow", "0"))

        self.generate_code_python_func.setText(self.translate("MainWindow", "Сгенерировать код функции (Python)"))
        self.draw_graph_btn.setText(self.translate("MainWindow", "Построить график"))
        self.clear_field_btn.setText(self.translate("MainWindow", "Очистить поля"))
        self.reset_plot.setText(self.translate("MainWindow", "Сбросить графики"))

        self.max_label.setText(self.translate("MainWindow", "Максимум функции"))
        self.max_func.setValue(0)
        self.min_label.setText(self.translate("MainWindow", "Минимум функции"))
        self.min_func.setValue(0)
        self.amp_noise_label.setText(self.translate("MainWindow", "Отношение шум/сигнал"))
        self.amp_noise.setValue(0)
        self.add_noise_btn.setText(self.translate("MainWindow", "Применить шум"))
        self.save_min_max.setText(self.translate("MainWindow", "Сохранить минимум и максимум"))
        self.func_value_label.setText(self.translate("MainWindow", "Значение функции в точке равно"))
        self.func_value.setText(self.translate("MainWindow", "42"))

        self.point_label.setText(self.translate("MainWindow", "Координаты точки"))
        self.point.setText(self.translate("MainWindow", "0, 0"))
        self.find_func_btn.setText(self.translate("MainWindow", "Получить значение функции"))

    def translate(self, text, text_1):
        return QtCore.QCoreApplication.translate(text, text_1)
