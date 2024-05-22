Простой скрипт, который группирует таблицу по первому столбцу и удаляет дублирующиеся строки. 

Логика работы:

- пропускает первые две строки (в рамках текущей задачи там были заголовки);
- смотрит идентификаторы в первом столбце, встречая одинаковые идентификаторы проверяет содержимое все строки;
- если в строках с одинаковыми идентификаторами данные полностью совпадают, то будет оставлена только одна;
- если в строках с одинаковыми идентификаторами есть различия в объеме заполненности (в одной строке данные в ячейке заполнены, а в другой -- нет), то скрипт оставляет одну строку, ***объединяя данные*** с двух строк;
- если в строках с одинаковыми идентификаторами есть различия во внесенных данных (в обеих строках в соответствующую ячейку внесены данные и они различаются), то скрипт оставляет обе строки, для дальнейшей ***ручной проверки***.

----
A simple script that groups a table by the first column and removes duplicate rows.

Working logic:

- Skips the first two rows (in this particular task, they contain headers);
- Looks at the identifiers in the first column, and when it encounters identical identifiers, it checks the content of the entire row;
- If the data in rows with identical identifiers is completely the same, only one row will be kept;
- If there are differences in the level of completeness in rows with identical identifiers (one row has data in a cell while the other does not), the script will keep one row, ***merging the data*** from both rows;
- If there are differences in the entered data in rows with identical identifiers (both rows have data in the corresponding cell and the data differs), the script will keep both rows for further ***manual verification***.
