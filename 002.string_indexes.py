'''
002 String Indexes

'''

name = "Margarita"
#.......012345678

#position de izquierda a derecha iniciando con el 0

print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])


#[start : stop : stepover(brinca de 1 en 1, 2 en 2  y asi sucesivamentre)] El stop se detiene uno antes 
print(name[0:3]) #Mar
print(name[2:6]) #rgar

phone ="3315000807"
#.......012345678910
print(phone[0:10:2]) #31000
print(phone[:3]) #331
print(phone[::2]) #31000
print(phone[-1])
print(phone[-2])
print(phone[::-1])








