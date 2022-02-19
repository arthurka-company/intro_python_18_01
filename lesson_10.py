# csv, json

import csv
import json

#
# with open('report.csv', 'r') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
#     # for row in reader:
#     #     print(row)
#     data = [row for row in reader]
# print(data)
#
# with open('out.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';', quotechar='"')
#     writer.writerow(['id', 'order_sum'])
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
#
with open('report.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    # for row in reader:
    #     print(row['id'], row['order_sum'])
    data = [dict(row) for row in reader]
print(data)
#
# with open('out.csv', 'w') as csv_file:
#     fieldnames = ['id', 'order_sum', 'pay"ment']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)
#         # writer.writerow({'id': row['id'], 'order_sum': row['order_sum']})


json_data = [
    {'id': '1', 'order_sum': '250.0', 'pay"ment': '500.0'},
    {'id': '12', 'order_sum': '455.0', 'pay"ment': '500.0'}
]

with open('out.json', 'w') as out_file:
    json.dump(json_data, out_file)

# with open('out.json', 'w') as out_file:
#     json.dump({'id': '1', 'order_sum': '250.0', 'pay"ment': '500.0'}, out_file)

with open('out.json', 'r') as in_file:
    data = json.load(in_file)
print(data)

