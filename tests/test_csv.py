import csv
import os


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
path_resources = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources')
with open(os.path.join(path_resources, 'eggs.csv'), 'x') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])
    assert os.path.isfile(os.path.join(path_resources, 'eggs.csv'))

with open(os.path.join(path_resources, 'eggs.csv')) as csvfile:
    csvreader = csv.reader(csvfile)
    check_csv = []
    for row in csvreader:
        assert row in [['Anna', 'Pavel', 'Peter'],['Alex', 'Serj', 'Yana']]

# os.remove(os.path.join(path_resources, 'eggs.csv')) # Remove eggs.csv
# assert os.path.exists(os.path.join(path_resources, 'eggs.csv')) is False # check remove eggs.csv is done

