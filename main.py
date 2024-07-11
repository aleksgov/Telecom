import os
import csv
import chardet
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.formula.translate import Translator
from design import Ui_MainWindow
from openpyxl.styles import Alignment


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
        self.report_excel_file = "ОТЧЕТ_ТЕЛЕКОМ.xlsx"

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
        ws.title = "Список работников"

        # Добавляем заголовки
        ws['A1'] = "ФИО"
        ws['B1'] = "Номер"
        ws['C1'] = "Должность"
        ws['D1'] = "Сумма лимита руб. с НДС"

        wb.save(self.excel_file)

    def open_excel_file(self, filename):
        try:
            if os.name == 'nt':  # для Windows
                os.startfile(filename)
            elif os.name == 'posix':  # для macOS и Linux
                os.system(f"open {filename}")
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

    def convert_csv_to_excel(self, csv_file):
        excel_file = "ОТЧЕТ_ТЕЛЕКОМ.xlsx"  # новое имя файла для сохранения в формате Excel

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

    def create_custom_excel(self):
        try:
            # Загружаем данные из файла ОТЧЕТ_ТЕЛЕКОМ.xlsx
            report_wb = load_workbook(self.report_excel_file, data_only=True)
            report_ws = report_wb.active

            # Создаем новый файл ОБЩИЙ_ОТЧЕТ.xlsx
            wb = Workbook()
            ws = wb.active
            ws.title = "Данные"

            # Добавляем заголовки
            headers = ["АБОНЕНТ", "Итого без НДС", "Сумма НДС", "Итого с НДС"]
            ws.append(headers)

            # Находим индексы нужных столбцов по их названиям
            columns = {cell.value: cell.column for cell in report_ws[1] if cell.value in headers}

            # Копируем данные из нужных столбцов
            for row in range(2, report_ws.max_row + 1):
                data_row = []
                for header in headers:
                    col = columns.get(header)
                    if col:
                        cell_value = report_ws.cell(row=row, column=col).value
                        if header == "Итого без НДС" and cell_value is not None:
                            try:
                                cell_value = float(str(cell_value).replace(',', '.'))
                            except ValueError:
                                cell_value = 0
                        data_row.append(cell_value)
                    else:
                        data_row.append(None)
                ws.append(data_row)

            # Добавляем формулы для столбцов "Сумма НДС" и "Итого с НДС"
            sum_nds_column = get_column_letter(headers.index("Сумма НДС") + 1)  # +1 for 1-based index
            total_with_nds_column = get_column_letter(headers.index("Итого с НДС") + 1)  # +1 for 1-based index
            for row_idx in range(2, ws.max_row + 1):
                sum_nds_cell = ws[f"{sum_nds_column}{row_idx}"]
                sum_without_nds_cell = ws[f"B{row_idx}"]  # Assuming "Итого без НДС" is in column B
                total_with_nds_cell = ws[f"{total_with_nds_column}{row_idx}"]

                sum_nds_cell.value = f"={sum_without_nds_cell.coordinate} * 0.2"
                total_with_nds_cell.value = f"={sum_without_nds_cell.coordinate} + {sum_nds_cell.coordinate}"

            last_row = ws.max_row + 1
            ws.cell(row=last_row, column=1, value="Сумма:")

            for col in range(2, ws.max_column + 1):
                col_letter = get_column_letter(col)
                ws.cell(row=last_row, column=col, value=f"=SUM({col_letter}2:{col_letter}{last_row - 1})")

            for row in ws.iter_rows(min_row=2, max_row=ws.max_row-1, min_col=1, max_col=ws.max_column):
                for cell in row:
                    cell.alignment = Alignment(horizontal='right')

            # Устанавливаем ширину столбцов на основе длины заголовков
            for col_idx, header in enumerate(headers, start=1):
                column_letter = get_column_letter(col_idx)
                column_width = max(len(str(header)) + 2, 10)  # минимальная ширина столбца 10
                ws.column_dimensions[column_letter].width = column_width

            ws.column_dimensions['A'].width = 15
            wb.save(self.custom_excel_file)

            QMessageBox.information(self, "Информация", f"Создан новый файл {self.custom_excel_file}")

            # Открываем созданный файл
            self.open_excel_file(self.custom_excel_file)

        except Exception as e:
            print(f"Ошибка при создании общего отчета: {e}")
            QMessageBox.warning(self, "Ошибка", f"Не удалось создать общий отчет: {e}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
