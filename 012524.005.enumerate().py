'''
005 enumerate
'''

'''
course = "Learning Python"
for index , character in enumerate(course):
    #print(index, character)
    if character == 'n':
       # print(index, character)
        print(f'index of {character} in position {index}')
'''

'''
Programa que liste los cursos, pregunte el index y despliegue
'''

my_course = ['Python', 'Scrum', 'Docker', 'NGINX']
for index, course in enumerate(my_course):
    print(index, course)
    select = index
    find = input('find: ')
    if find == index:     
        print(f'Course{course} found in index {index}')