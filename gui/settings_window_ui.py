from PyQt5 import QtCore, QtWidgets

from settings import Settings


class UiSettingsWindow:
    def __init__(self):
        self.form = None
        self.save_btn = None

    def setup_ui(self, window):
        window.setObjectName("SettingsWindow")
        window.setMinimumSize(QtCore.QSize(300, 0))

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        self.form = QtWidgets.QFormLayout()
        self.save_btn = QtWidgets.QPushButton()

        for key in Settings.settings.keys():
            s = Settings.settings.get(key)
            t = s.type_setting
            label = QtWidgets.QLabel()
            label.setText(s.name)
            if t is int:
                field = QtWidgets.QSpinBox()
                field.setValue(s.value)
            elif t is float:
                field = QtWidgets.QDoubleSpinBox()
                field.setValue(s.value)
            elif t is str:
                field = QtWidgets.QLineEdit()
                field.setText(s.value)
            else:
                field = QtWidgets.QLineEdit()
            self.form.addRow(label, field)

        window.setLayout(v_box)
        h_box.addWidget(self.save_btn)
        v_box.addLayout(self.form)
        v_box.addLayout(h_box)

        self.retranslate(window)

    def retranslate(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("SettingsWindow", "Настройки"))
        self.save_btn.setText(_translate("SettingsWindow", "Сохранить"))
