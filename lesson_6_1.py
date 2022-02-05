# словарь, dict

# my_dict = {}
# my_dict = {
#     'key': 'Value',
#     123: [123, 23],
#     []: 234  # error
# }
#
# print(type(my_dict))
# print(my_dict)
# print(my_dict[123])
# print(my_dict['key'])

# my_dict_2 = dict()
# my_dict_2 = dict(key=123, name='Ok')
# print(my_dict_2)

# my_dict_3 = dict.fromkeys(['a', 'b'])
# my_dict_3 = dict.fromkeys(['a', 'b'], 100)
# # print(my_dict_3)
#
# # my_dict_3 = {i: i for i in range(10) if i > 3}
# my_dict_3 = {str(i): i ** 2 for i in range(10) if i > 3}
# print(my_dict_3)
#
# # print(dir(my_dict_3))
#
# # print(list(my_dict_3.values()))
# # for v in my_dict_3.values():
# #     print(v)
#
# # print(my_dict_3.keys())
#
# # print(my_dict_3.items())
# # print(list(my_dict_3.items()))
# # for key, value in my_dict_3.items():
# #     print(key, value)
#
# print(my_dict_3['5'])
# # print(my_dict_3['color'])
# print(my_dict_3.get('color'))
# print(my_dict_3.get('5', '1000'))
# print()
#
#
# template = {
#     'name': '',
#     'type': '',
#     'text': '',
#     'category': '',
#     'color': '',
# }
#
# my_dict_3.update({'5': 1000, 'new_key': 100000})
# print(my_dict_3)
# del my_dict_3['5']
# print(my_dict_3)

# def func_name(arg):
#     pass
#     return None


text = 'John is the son of John second. Second son of John second is William second.'
text = text.lower().replace('.', '')
counts = {}
words = text.split()
for word in set(words):
    counts[word] = text.count(word)
print(counts)

counts = {}
for word in words:
    if word not in counts.keys():
        counts[word] = 1
    else:
        counts[word] += 1
print(counts)
result = sorted(counts.items(), key=lambda item: item[1], reverse=True)
print(result)
print(result[:3])
