import os
import csv
import chardet
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from openpyxl import Workbook, load_workbook
from design import Ui_MainWindow
from openpyxl.utils import get_column_letter


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем кнопки к функциям
        self.ui.changeButton.clicked.connect(self.manage_employees)
        self.ui.fileButton2_3.clicked.connect(self.load_file)
        self.ui.fileButton1.clicked.connect(self.create_custom_excel)

        # Пути к файлам Excel
        self.excel_file = "Работники.xlsx"
        self.custom_excel_file = "ОБЩИЙ_ОТЧЕТ.xlsx"

    def manage_employees(self):
        if not os.path.exists(self.excel_file):
            # Если файл не существует, создаем новый
            self.create_new_excel()
            QMessageBox.information(self, "Информация", "Создан новый файл Работники.xlsx")

        # Открываем Excel файл с помощью стандартного приложения
        self.open_excel_file(self.excel_file)

    def create_new_excel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "Работники"

        # Добавляем заголовки
        headers = ["ФИО", "Номер", "Должность", "Сумма лимита руб. с НДС"]
        ws.append(headers)

        # Устанавливаем ширину столбцов на основе длины заголовков
        for col_idx, header in enumerate(headers, start=1):
            column_letter = get_column_letter(col_idx)
            column_width = max(len(str(header)) + 2, 10)  # минимальная ширина столбца 10
            ws.column_dimensions[column_letter].width = column_width

        wb.save(self.excel_file)


    def open_excel_file(self, file_path):
        try:
            if os.name == 'nt':  # для Windows
                os.startfile(file_path)
            elif os.name == 'posix':  # для macOS и Linux
                os.system(f"open {file_path}")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось открыть файл: {e}")

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "",
                                                   "CSV Files (*.csv);;Excel Files (*.xlsx *.xls)")
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

    def create_custom_excel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "Данные"

        # Добавляем заголовки
        headers = ["АБОНЕНТ", "Итого без НДС", "Сумма НДС", "Итого с НДС"]
        ws.append(headers)

        # Устанавливаем ширину столбцов на основе длины заголовков
        for col_idx, header in enumerate(headers, start=1):
            column_letter = get_column_letter(col_idx)
            column_width = max(len(str(header)) + 2, 10)  # минимальная ширина столбца 10
            ws.column_dimensions[column_letter].width = column_width

        wb.save(self.custom_excel_file)
        QMessageBox.information(self, "Информация", f"Создан новый файл {self.custom_excel_file}")

        # Открываем созданный файл
        self.open_excel_file(self.custom_excel_file)


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
                data = list(reader)

            # Записываем данные во временный лист
            for row in data:
                ws.append(row)

            # Определяем столбцы для удаления
            columns_to_delete = []
            for col in range(1, ws.max_column + 1):
                if all(ws.cell(row=row, column=col).value in (0, '0', None) for row in range(2, ws.max_row + 1)):
                    columns_to_delete.append(col)

            # Удаляем столбцы в обратном порядке
            for col in sorted(columns_to_delete, reverse=True):
                ws.delete_cols(col)

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
