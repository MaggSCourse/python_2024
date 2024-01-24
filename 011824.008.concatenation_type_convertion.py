'''
008 Concatenation & Type conversion
concatenar es unir variables o strings ( no numeros, ya que necesito convertirlos en 'str' para concatenar , si no los suma) y usamos el simbolo de +.

si quieres colocar la concatenacion en la misma linea va de la sig manera param1 + ' '  + param2

'''


first_name = 'Maggie'
last_name = 'Samano'

print(first_name + ' ' + last_name)

full_name = first_name + ' ' + last_name

print(full_name)

born_year = 1995

#print(full_name + ' ' + born_year)
print(full_name + ' ' + str(born_year))

current_year = 2024
#print(born_year + current_year)
print(str(born_year) + ' ' +str(current_year))