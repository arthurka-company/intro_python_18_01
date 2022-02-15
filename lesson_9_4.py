'''
names.txt - для каждого человека создать папку и в нее положить файл info.txt с возрастом
человека
'''

import os


def get_list_of_persons_from_file(file_path: str) -> list:
    with open(file_path, 'r') as f:
        data = f.readlines()
    result = []
    for person in data:
        item = {
            'name': person.replace('\n', '').split(',')[0],
            'age': person.replace('\n', '').split(',')[1]
        }
        result.append(item)
    return result


def create_folder_and_file_for_person(person: dict, root_folder: str) -> None:
    person_folder = os.path.join(root_folder, person['name'])
    os.makedirs(person_folder, exist_ok=True)
    with open(os.path.join(person_folder, 'info.txt'), 'w') as f:
        f.write(person['age'])


file_path = 'names.txt'
root_folder = 'persons'
list_of_persons = get_list_of_persons_from_file(file_path)
print(list_of_persons)
for person in list_of_persons:
    create_folder_and_file_for_person(person, root_folder)