import csv
# with open('countries.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print row
#
# i = [['sheng', 98], ['xiong', 95]]
# with open('countries2.csv', 'wb') as f:
#     writer = csv.writer(f)
#     writer.writerows(i)

with open('countries3.csv', 'wb') as filer:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(filer, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([{'first_name': 'bill', 'last_name': 'nono'}, {'first_name': 'bradely', 'last_name': 'nba'}])

with open('countries3.csv', 'rb') as file_reader:
    reader = csv.DictReader(file_reader)
    for row in reader:
        print {row['first_name']: row['last_name']}