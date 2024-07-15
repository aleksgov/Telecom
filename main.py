import os
import csv
import chardet
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from design import Ui_MainWindow
from openpyxl.styles import Alignment, Font


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

            # Загружаем данные из файла Работники.xlsx
            workers_wb = load_workbook('Работники.xlsx', data_only=True)
            workers_ws = workers_wb.active

            # Создаем новый файл ОБЩИЙ_ОТЧЕТ.xlsx
            wb = Workbook()
            ws = wb.active
            ws.title = "Отчет"

            # Добавляем заголовки
            headers = ["АБОНЕНТ", "Итого без НДС", "Сумма НДС", "Итого с НДС"]
            ws.append(headers)
            columns = {cell.value: cell.column for cell in report_ws[1] if
                       cell.value in ["АБОНЕНТ", "Итого без НДС", "Сумма НДС", "Итого с НДС"]}

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

            sum_nds_column = get_column_letter(headers.index("Сумма НДС") + 1)
            total_with_nds_column = get_column_letter(headers.index("Итого с НДС") + 1)
            for row_idx in range(2, ws.max_row + 1):
                sum_nds_cell = ws[f"{sum_nds_column}{row_idx}"]
                sum_without_nds_cell = ws[f"B{row_idx}"]
                total_with_nds_cell = ws[f"{total_with_nds_column}{row_idx}"]
                sum_nds_cell.value = f"={sum_without_nds_cell.coordinate} * 0.2"
                total_with_nds_cell.value = f"={sum_without_nds_cell.coordinate} + {sum_nds_cell.coordinate}"

            last_row = ws.max_row + 2
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
                column_width = max(len(str(header)) + 2, 10)
                ws.column_dimensions[column_letter].width = column_width
            ws.column_dimensions['A'].width = 15

            # Создаем вторую таблицу на новом листе
            second_ws = wb.create_sheet(title="Подробный отчет")

            data = [
                ["Сведения о расходовании денежных средств на мобильную связь Ухтинский филиал"],
                ["за период с 01 по 30 апреля 2024 г."],
                ["Номер телефона", "ФИО", "Должность", "Сумма лимита руб. с НДС",
                 "Фактическая сумма Руб. с НДС", "Фактическая сумма Руб.без НДС",
                 "Перерасход", "Счет затрат", " ", "Тариф"]
            ]

            # Добавляем данные в лист
            for row in data:
                second_ws.append(row)

            # Объединяем ячейки перед применением стилей
            second_ws.merge_cells('A1:J1')
            second_ws.merge_cells('A2:J2')
            second_ws.merge_cells('H3:I3')

            def apply_header_style(ws, cell):
                ws[cell].alignment = Alignment(horizontal='center')
                ws[cell].font = Font(name='Arial Cyr', bold=True, size=12)

            def apply_normal_cell_style(ws, cell):
                ws[cell].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
                ws[cell].font = Font(name='Calibri', size=10)

            apply_header_style(second_ws, 'A1')
            apply_header_style(second_ws, 'A2')

            for row in second_ws.iter_rows():
                for cell in row:
                    if cell.coordinate not in ['A1', 'A2']:  # Исключаем ячейки заголовков
                        apply_normal_cell_style(second_ws, cell.coordinate)

            for row in second_ws.iter_rows(min_row=4, min_col=1):
                for cell in row:
                    cell.font = Font(size=12)

            column_widths = [125, 135, 300, 80, 85, 85, 75, 65, 65, 65]  # Ширина столбцов
            for i, width in enumerate(column_widths, start=1):
                excel_width = width / 7  # Преобразуем пиксели в "экселевские" единицы
                second_ws.column_dimensions[get_column_letter(i)].width = excel_width

            # Настройка высоты строки
            second_ws.row_dimensions[3].height = 50

            # Копируем данные из столбца "АБОНЕНТ" на первом листе в столбец "Номер телефона" на втором листе
            abonents = []
            for row in report_ws.iter_rows(min_row=2, min_col=columns["АБОНЕНТ"], max_col=columns["АБОНЕНТ"], max_row=report_ws.max_row):
                abonents.append(row[0].value)

            for idx, abonent in enumerate(abonents, start=1):
                second_ws.cell(row=idx + 3, column=1, value=abonent)

            # Копируем данные из столбцов "ФИО" и "Должность" файла Работники в соответствующие столбцы на втором листе
            fio_column = None
            position_column = None
            limit_column = None
            for cell in workers_ws[1]:
                if cell.value == "ФИО":
                    fio_column = cell.column
                if cell.value == "Должность":
                    position_column = cell.column
                if cell.value == "Сумма лимита руб. с НДС":
                    limit_column = cell.column

            if fio_column is not None:
                for row_idx, row in enumerate(workers_ws.iter_rows(min_row=2, min_col=fio_column, max_col=fio_column, max_row=workers_ws.max_row), start=1):
                    second_ws.cell(row=row_idx + 3, column=2, value=row[0].value)

            if position_column is not None:
                for row_idx, row in enumerate(workers_ws.iter_rows(min_row=2, min_col=position_column, max_col=position_column, max_row=workers_ws.max_row), start=1):
                    second_ws.cell(row=row_idx + 3, column=3, value=row[0].value)

            if limit_column is not None:
                for row_idx, row in enumerate(workers_ws.iter_rows(min_row=2, min_col=limit_column, max_col=limit_column, max_row=workers_ws.max_row), start=1):
                    second_ws.cell(row=row_idx + 3, column=4, value=row[0].value)

            # Применяем стили к столбцам "Номер телефона", "ФИО" и "Должность"
            for row in second_ws.iter_rows(min_row=4, max_row=len(abonents) + 3, min_col=1, max_col=4):
                for cell in row:
                    apply_normal_cell_style(second_ws, cell.coordinate)

            # Сохранение файла
            wb.save(self.custom_excel_file)

            # Вывод информационного сообщения
            QMessageBox.information(self, "Информация", f"Создан новый файл {self.custom_excel_file}")

            # Открытие файла
            self.open_excel_file(self.custom_excel_file)

        except Exception as e:
            print(f"Ошибка при создании общего отчета: {e}")
            QMessageBox.warning(self, "Ошибка", f"Не удалось создать общий отчет: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
