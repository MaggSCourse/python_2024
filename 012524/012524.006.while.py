''''
006 while

'''
'''
iterador = 0
while iterador <= 5 :
    print(iterador)
    iterador += 1
    #iterador = iterador +1

print('Done!')
'''
option = 0 #El While se esta revisando y la variable option vale siempre
while option != 3: #mientras que option sea diferente de 3 haz el bucle
    print('1, revisa tu saldo')
    print('2, retirar')
    print('3, salir') 
    option = int(input('seleccione: ' '\n' ))
    if option == 3 :
       print('fin del bucle')
    elif option > 3:
        print('\n''Seleccion Invalida, vuelva a seleccionar')
   
    
      
      # option = 3  
        #break
        #pass
