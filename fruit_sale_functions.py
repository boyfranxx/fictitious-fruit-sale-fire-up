import pyodbc

conn = pyodbc.connect\
    (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=N:\Fruit Sale Project\2018AnthisFruit.accdb;')
cursor = conn.cursor()
cursor.execute('select * from FruitSale')
rows = []
for row in cursor.fetchall():
    rows.append(row)


def column_names_indexes(table):
    """Returns a dictionary with column names and their respective indexes."""
    count = 0
    columns = {}
    for name in cursor.columns(table=table):
        count += 1
        column_name = name.column_name
        column_index = count - 1
        columns[column_name] = column_index
    return columns


def find_sum_column_index(item_type):
    """Finds index for column."""
    fruit_columns = column_names_indexes('FruitSale')
    # Search for column with matching name as inputted and set the sum index to that index.
    sum_index = None
    for name, index in fruit_columns.items():
        if name == item_type:
            sum_index = index
    if sum_index is None:
        print(f"Could not find '{item_type}' in the column headers.")
    return sum_index


def find_sum_list(item_type):
    """Find total sum of one column."""

    # Initialize index for item type.
    sum_index = int(find_sum_column_index(item_type))

    # Add each value in column to a list.
    sum_list = []
    for row in rows:
        for info in row:
            if row[sum_index] is not None:
                row_total = row[sum_index]
                sum_list.append(int(row_total))

    # Return list.
    return sum_list

