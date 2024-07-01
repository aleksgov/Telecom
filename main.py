import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from openpyxl import Workbook, load_workbook
from design import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем кнопки к функциям
        self.ui.changeButton.clicked.connect(self.manage_employees)
        self.ui.fileButton2_3.clicked.connect(self.load_file)

        # Путь к файлу Excel
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


    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*.*)")
        if file_name:
            # Здесь вы можете обработать выбранный файл
            print(f"Выбран файл: {file_name}")
            # Например, отобразить имя файла в label
            self.ui.fileLabel.setText(f"Файл: {os.path.basename(file_name)}")

            # Если выбран Excel файл, можно его открыть
            if file_name.endswith(('.xlsx', '.xls')):
                try:
                    wb = load_workbook(file_name)
                    ws = wb.active
                    # Здесь можно обработать данные из Excel
                    print(f"Открыт Excel файл, листов: {len(wb.sheetnames)}")
                except Exception as e:
                    print(f"Ошибка при открытии Excel файла: {e}")
                    QMessageBox.warning(self, "Ошибка", f"Не удалось открыть файл Excel: {e}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())