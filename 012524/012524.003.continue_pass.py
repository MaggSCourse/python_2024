'''
003. 
- break
- continue
- pass : Es una exepcion para dejar un For o una funcion vacio

'''

students = ['Paulina', 'Octupus', 'Ulises','Ibra','Maggie']

for student in students:
    print(student)
    if student == 'Ulises' :
        break
        print('continue')
        input ('press enter to continue')
    continue
    pass