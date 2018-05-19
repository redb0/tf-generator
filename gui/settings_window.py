from PyQt5 import QtCore

from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QDoubleSpinBox

from gui.settings_window_ui import UiSettingsWindow

from settings import Settings


class SettingsWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent, QtCore.Qt.Window)

        self.ui = UiSettingsWindow()
        self.ui.setup_ui(self)

        self.ui.save_btn.clicked.connect(self.save)

    def closeEvent(self, e):
        self.parent().settings_window = None
        self.close()

    def init_settings(self):
        pass

    def save(self):
        for i in range(self.ui.form.count()):
            item = self.ui.form.itemAt(i).widget()
            if type(item) is QLabel:
                field_wdg = self.ui.form.itemAt(i + 1).widget()
                if type(field_wdg) is QSpinBox or type(field_wdg) is QDoubleSpinBox:
                    value = field_wdg.value()
                else:
                    value = field_wdg.text()
                for key in Settings.settings.keys():
                    s = Settings.settings.get(key)
                    if item.text() == s.name:
                        s.value = value
