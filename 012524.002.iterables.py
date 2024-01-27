'''
002. Iterables
cllections: list, tuple,sets and dictionaries are iterables.

'''

user_dict ={
    'name': 'Luis',
    'can drive': True,
    'phone' : 3315000807
}
'''
for item in user_dict:
    print(item)

for item in user_dict.items():
    print(item)

for item in user_dict.values():
    print(item)

for item in user_dict.Keys():
    print(item)
'''

for item in user_dict.items():
    key, values = item
    print(item)

for key, values in user_dict.items():
   print(key, ":", values)
