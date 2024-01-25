'''
002. Condicionales
- if
- else
- else if = elif

-and , ambas tienen que ser True
-or, al menos una de las 2 debe de ser True

'''
'''
is_old = True
licencia_conducir = False



#if is_old == True:
if is_old:
    print('Tienes edad para manejar')
elif licencia_conducir:
    print('Puedes conducir')
else:
    print('No tienes edad para manejar')
'''
'''
if is_old and licencia_conducir:
    print('Eres un buen ciudadano con licencia y la edad suficiente')
else:
    print('Lo siento, no puedes conducir')

edad = int(input('Cual es tu edad? '))

if edad >= 18 and edad <= 70:
    print('Eres mayor de edad y puedes manejar bien')
elif edad > 71:
    print('Aunque eres mayor de edad, dudamos que puedas manejar')
else:
    print('Que haces aqui? ')
'''
user = input('user: ')
password = input('password: ')

'''
if user == 'luis' and password == '123':
    print('Eres un usuario normal')
else:
    print('Usuario o Conrtasena incorrectos')
'''

if user == 'luis' and password == '123':
    print('Eres un usuario normal')
elif user == 'maggie' and password == '432':
    print('Eres usuario administrador')
elif user == 'octupus' and password == '678':
    print('Eres un super administrador')
elif user == 'paulina' and password == '456':
    print('Eres usuario super super administrador')
else:
    print('no eres un usuario registrado')
