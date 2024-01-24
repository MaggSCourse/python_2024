'''
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

'''


horas_trabajadas = input('Horas trabajadas: ')
#print(horas_trabajadas)
costo_hora = input('Cual es el costo por hora: ')
#print(costo_hora)
pago = int(costo_hora) * int(horas_trabajadas)
print(f"El monto a pagar : ${pago}.00")