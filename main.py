import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from openpyxl import Workbook, load_workbook
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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())