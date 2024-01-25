'''
004. and / or
- deben de ser en minusculas
- and, ambos deben de ser verdaderos  = True
- or, al menos uno debe de ser verdadero = True
'''
is_employee = True
is_developer = False

employee_area ='Eres de IT' if is_employee and is_developer else 'Eres administrativo'
print(employee_area)

employee_area ='Eres de IT' if is_employee or is_developer else 'Eres administrativo'
print(employee_area)