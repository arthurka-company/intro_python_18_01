import csv


data = {
    'name': 'text'
}
users = [
    {
        'id': 1,
        'name': 'name_1'
    },
    {
        'id': 2,
        'name': 'name_2'
    }
]


for user in users:
    with open(f'{user["name"]}.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['test'])
        writer.writeheader()
        todos = requests.get(f'{url_todo}?userId={user["id"]}')
        for todo in todos:
            writer.writerow({''})
