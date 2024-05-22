import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os


def get_open_filename():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')],
                                           title='Выберите исходный файл')
    return file_path


def merge_values(grouped_table):
    output_rows = []

    for _, group in grouped_table:
        if len(group) == 1:
            output_rows.append(group.loc[group.index[0]])
            continue

        merged_row = {}
        not_merged_rows = []

        for _, row in group.iterrows():
            merge_success = True
            for column in group.columns:
                value = row[column]

                if pd.notnull(value):
                    if column not in merged_row:
                        merged_row[column] = value

                    elif value != merged_row[column]:
                        merge_success = False
                        break

            if not merge_success:
                not_merged_rows.append(row)

        output_rows.append(pd.Series(merged_row))

        for not_merged_row in not_merged_rows:
            output_rows.append(not_merged_row)

    return pd.DataFrame(output_rows)


exit_program = False

while True:
    # Загрузка таблицы из файла excel
    input_file = get_open_filename()

    if not input_file:
        print('Файл не выбран. Завершение программы.')
        break

    file_name, file_ext = os.path.splitext(input_file)
    output_file = f"{file_name}_FIXED{file_ext}"
    output_sheet_name = "Merged Sheet"

    # Чтение Excel-файла, пропускает первые две строки
    df = pd.read_excel(input_file, sheet_name=0, header=None, skiprows=2)

    # Чтение первых двух строк Excel-файла
    first_two_rows = pd.read_excel(input_file, sheet_name=0, header=None, nrows=2)

    # Группировка таблицы по первому столбцу
    grouped = df.groupby(df.columns[0])

    # Применение функции merge_values к каждой группе
    merged_df = merge_values(grouped)

    # Объединение первых двух строк с результирующей таблицей
    final_df = pd.concat([first_two_rows, merged_df], ignore_index=True)

    # Сохранение полученного результата в новой таблице excel
    final_df.to_excel(output_file, sheet_name=output_sheet_name, index=False, header=None)

print("Программа завершена.")
