import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from openpyxl import Workbook, load_workbook
import pandas as pd
from design import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.changeButton.clicked.connect(self.manage_employees)

        self.excel_file = "employees.xlsx"

    def manage_employees(self):
        if not os.path.exists(self.excel_file):
            # Если файл не существует, создаем новый
            self.create_new_excel()
            QMessageBox.information(self, "Информация", "Создан новый файл employees.xlsx")
        else:
            # Если файл существует, открываем его
            self.open_existing_excel()
            QMessageBox.information(self, "Информация", "Открыт существующий файл employees.xlsx")

    def create_new_excel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "Список работников"

        # Добавляем заголовки
        ws['A1'] = "Имя"
        ws['B1'] = "Фамилия"
        ws['C1'] = "Должность"

        wb.save(self.excel_file)

    def open_existing_excel(self):
        wb = load_workbook(self.excel_file)
        ws = wb.active


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