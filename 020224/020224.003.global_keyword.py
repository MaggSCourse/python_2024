'''
003 Global keyword
- nos permite llamar a una variable global dentro de una funcion, donde la variable es local.

'''
#constante
USD = 20.34

#global
total =100



def print_total():
    total = 1 #variable local
    total += 1
    print (total)

print_total() #2


def print_total_2(): #2
    global total
    total += 1
    print(total)

print_total_2() #
    