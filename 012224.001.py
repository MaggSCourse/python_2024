'''
001 List
- Se usan para guardar multiples datos en una variable
- Los datos que puede guardar la lista son: int, float, string, boolean, list
- Las listas usan los [square brakets]
- Las listas pueden ser ordenadas, cambiadas, y permiten duplicados
- Las listas son indexadas e inician con el 0
- Las listas pueden ser arreglos en otros lenguajes de programacion

'''

list_my_students = [
    'Maggie',   #0
    'Ibrahim',  #1
    'Paulina',  #2
    'Octavio',  #3
    'Ulises' ,  #4
    #2024,       #5
   # 2.50,       #6
    'Paulina'   #7
    ]   
'''
print(list_my_students)
print(list_my_students[0])
print(list_my_students[1])
print(list_my_students[2])
print(list_my_students[3])
print(list_my_students[4])
list_my_students.append("Luis")
list_my_students.insert(0,'Isela')
list_my_students.extend(['Javier', 'Isela', 'Limon'])
'''

#print(list_my_students)
#remove elements
#list_my_students.pop()
#list_my_students.pop(1)
list_my_students.remove("Paulina")
#list_my_students.clear()
#print(len(list_my_students))


'''
for student in list_my_students : 
    print(student)

'''

print(list_my_students)
list_my_students.sort()
print(list_my_students)

#ordenando una lista en python