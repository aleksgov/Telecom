from PyQt5 import QtWidgets, uic
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from design import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем кнопки к методам
        self.ui.fileButton2_3.clicked.connect(self.load_csv)

        self.data = None

    def load_csv(self):
        # Открываем диалоговое окно для выбора файла
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            try:
                self.data = pd.read_csv(file_name)
                QMessageBox.information(self, "Успех", "Файл загружен успешно")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {e}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())