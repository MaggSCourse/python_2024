'''
0001. duplicates

'''
my_list = ['a','b','c','d','d','e','f','g','g','g','g']
'''
repetidos = [ ]
no_repetidos = [ ]

#print(my_list)

for item in my_list:
    #print(item)
    if my_list.count(item) > 1:
        #print(item)
        repetidos.append(item)
    else:
        #print(item)
        no_repetidos.append(item)
        print(no_repetidos)
#print(repetidos)
'''

repetidos = [ ]
for item in my_list:
    if my_list.count(item) > 1:
        repetidos.append(item)
        my_list.remove(item)
print(repetidos)
print(my_list)