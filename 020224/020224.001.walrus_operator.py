'''
001 Walrus
" := "
-permite asignar una variable y al mismo tiempo devolver el valor
-entra en 3.8

'''

lista = []
while (entra := input('escribe algo: ')) != 'fin' : 
    lista.append(entra)

print(lista)
