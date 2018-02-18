from PyQt5 import QtWidgets, QtCore

from PyQt5.QtWidgets import QApplication, QAction


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
        self.clear_btn = None

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(900, 548)
        main_window.setWindowTitle("TF_generator v0.1")

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
        self.parameters_title = QtWidgets.QLabel()

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

        self.scroll_methods = QtWidgets.QScrollArea()
        self.scroll_methods.setLayout(self.layout_methods)
        self.scroll_methods.setWidgetResizable(True)
        self.scroll_methods.setMaximumWidth(275)

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

        self.form = QtWidgets.QFormLayout()
        self.form.addRow(self.idx_func_label, self.idx_func)
        self.form.addRow(self.number_extrema_label, self.number_extrema)
        self.form.addRow(self.coordinates_label, self.coordinates)
        self.form.addRow(self.function_values_label, self.function_values)
        self.form.addRow(self.degree_smoothness_label, self.degree_smoothness)
        self.form.addRow(
            self.coefficients_abruptness_function_label,
            self.coefficients_abruptness_function
        )

        self.layout_parameters = QtWidgets.QVBoxLayout()
        self.layout_parameters.addWidget(self.parameters_title)
        self.layout_parameters.addLayout(self.form)
        self.layout_parameters.addStretch(1)

        self.graph_title = QtWidgets.QLabel()
        self.constraints_x1_label = QtWidgets.QLabel()
        self.constraints_x1 = QtWidgets.QLineEdit()
        self.constraints_x2_label = QtWidgets.QLabel()
        self.constraints_x2 = QtWidgets.QLineEdit()
        self.slice_expr_x1_label = QtWidgets.QLabel()
        self.slice_expr_x1 = QtWidgets.QLineEdit()
        self.slice_expr_x2_label = QtWidgets.QLabel()
        self.slice_expr_x2 = QtWidgets.QLineEdit()

        self.form_graph = QtWidgets.QFormLayout()
        self.form_graph.addRow(self.constraints_x1_label, self.constraints_x1)
        self.form_graph.addRow(self.constraints_x2_label, self.constraints_x2)
        self.form_graph.addRow(self.slice_expr_x1_label, self.slice_expr_x1)
        self.form_graph.addRow(self.slice_expr_x2_label, self.slice_expr_x2)

        self.layout_parameters.addWidget(self.graph_title)
        self.layout_parameters.addLayout(self.form_graph)


        scroll_parameters = QtWidgets.QScrollArea()
        scroll_parameters.setLayout(self.layout_parameters)
        scroll_parameters.setWidgetResizable(True)

        # кнопки
        self.generate_code_python_func = QtWidgets.QPushButton()
        self.draw_graph_btn = QtWidgets.QPushButton()
        self.clear_btn = QtWidgets.QPushButton()

        # расположение кнопок и всех остальных виджетов (сетка)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.scroll_methods)
        h_box.addWidget(scroll_parameters)

        h_box_button = QtWidgets.QHBoxLayout()
        h_box_button.addStretch(1)
        h_box_button.addWidget(self.generate_code_python_func)
        h_box_button.addWidget(self.draw_graph_btn)
        h_box_button.addWidget(self.clear_btn)

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
        self.menuFile.setTitle(self.to_utf("Файл"))

        self.actionOpenJson.setText(self.to_utf("Импорт параметров"))
        self.actionOpenJson.setStatusTip(self.to_utf("Импорт параметров из Json"))
        self.actionOpenJson.setShortcut(self.to_utf("Ctrl+O"))
        self.actionSave.setText(self.to_utf("Сохранить параметры"))
        self.actionSave.setStatusTip(self.to_utf("Сохранить парметры тестовой функции в json файле"))
        self.actionQuit.setText(self.to_utf("Выход"))
        self.actionQuit.setShortcut(self.to_utf("Ctrl+Q"))

        self.actionSettings.setText(self.to_utf("Настройки"))

        # Справка
        self.menuHelp.setTitle(self.to_utf("Справка"))
        self.actionHelp.setText(self.to_utf("Справка"))
        self.actionHelp.setShortcut(self.to_utf("F1"))
        self.actionAbout.setText(self.to_utf("О программе"))

        # Настройки
        self.menuSettings.setTitle(self.to_utf("Настройки"))
        self.actionSettings.setText(self.to_utf("Настройки"))
        self.actionOpenDocker.setText(self.to_utf("Показать докеры"))

        self.method_min.setText("Метод Фельдбаума (оператор min)")
        self.hyperbolic_potential.setText("Гиперболическая потенциальная функция")
        self.exponential_potential.setText("Экспоненциальная потенциальная функция")
        self.methods_title.setText("Методы построения функций")
        self.parameters_title.setText("Параметры функции")

        self.idx_func_label.setText(self.to_utf("Индекс тестовой функции"))
        self.number_extrema_label.setText("Количество экстремумов")
        self.coordinates_label.setText("Координаты экстремумов")
        self.function_values_label.setText("Значения функции")
        self.degree_smoothness_label.setText("Степени гладкости функции")
        self.coefficients_abruptness_function_label.setText("Коэффициенты крутости функции")

        self.graph_title.setText(self.to_utf("Параметры графиков функции"))
        self.constraints_x1_label.setText(self.to_utf("Ограничения по оси X(x1) снизу и сверху"))
        self.constraints_x2_label.setText(self.to_utf("Ограничения по оси Y(x2) снизу и сверху"))
        self.slice_expr_x1_label.setText(self.to_utf("Выражение среза относительно оси X(x1)"))
        self.slice_expr_x2_label.setText(self.to_utf("Выражение среза относительно оси Y(x2)"))

        self.constraints_x1.setText("-6, 6")
        self.constraints_x2.setText("-6, 6")
        self.slice_expr_x1.setText("0")
        self.slice_expr_x2.setText("0")

        self.generate_code_python_func.setText("Сгенерировать код функции (Python)")
        self.draw_graph_btn.setText("Построить график")
        self.clear_btn.setText("Очистить поля")

    def to_utf(self, text):
        return QApplication.translate("MainWindow", text, None)
