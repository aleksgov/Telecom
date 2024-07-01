import os
import csv
import chardet
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
        ws['A1'] = "ФИО"
        ws['B1'] = "Номер"
        ws['C1'] = "Должность"
        ws['D1'] = "Лимит"

        wb.save(self.excel_file)

    def open_existing_excel(self):
        wb = load_workbook(self.excel_file)
        ws = wb.active

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "CSV Files (*.csv);;Excel Files (*.xlsx *.xls)")
        if file_name:
            # Обработка выбранного файла
            print(f"Выбран файл: {file_name}")
            self.ui.fileLabel.setText(f"Файл: {os.path.basename(file_name)}")

            try:
                if file_name.endswith('.csv'):
                    self.convert_csv_to_excel(file_name)
                elif file_name.endswith(('.xlsx', '.xls')):
                    wb = load_workbook(file_name)
                    ws = wb.active
                    print(f"Открыт Excel файл, листов: {len(wb.sheetnames)}")
            except Exception as e:
                print(f"Ошибка при обработке файла: {e}")
                QMessageBox.warning(self, "Ошибка", f"Не удалось обработать файл: {e}")

    def convert_csv_to_excel(self, csv_file):
        excel_file = csv_file.replace('.csv', '.xlsx')
        wb = Workbook()
        ws = wb.active

        try:
            with open(csv_file, 'rb') as f:
                result = chardet.detect(f.read())
            encoding = result['encoding']

            with open(csv_file, newline='', encoding=encoding) as f:
                reader = csv.reader(f, delimiter=';')
                for row in reader:
                    ws.append(row)

            wb.save(excel_file)
            QMessageBox.information(self, "Информация", f"CSV файл преобразован в Excel: {excel_file}")

        except Exception as e:
            print(f"Ошибка при чтении CSV файла: {e}")
            QMessageBox.warning(self, "Ошибка", f"Не удалось прочитать CSV файл: {e}")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
