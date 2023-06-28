import csv
import os


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
path_resources = os.path.join(os.path.dirname(os.path.dirname( os.path.abspath(__file__))), 'resources')
with open(os.path.join(path_resources, 'eggs.csv'), 'x') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])

# with open('resources/eggs.csv') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         print(row)
