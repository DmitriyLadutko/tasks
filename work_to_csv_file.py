import csv
from typing import List

__all__ = [
    'read_csv_file',
    'write_csv_file',
]


def read_csv_file(*, file_name: str):
    rows = []
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return fields, rows


def write_csv_file(*, file_name: str, fields: List, rows: List[List]):
    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)


file_name = 'some_file.csv'
fields = ['Name', 'last_name', 'age']
rows = [['Dima', 'Ladutko', '29'],
        ['Dima', 'Ladutko', '29']]
write_csv_file(file_name=file_name, fields=fields, rows=rows)
print(read_csv_file(file_name=file_name))

