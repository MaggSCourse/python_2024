'''
002 Matrix

'''

'''
matrix = [
    #0#1#2
    [1,2,3], #0
    [4,5,6], #1
    [7,8,9]  #2
]

print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])
#print(matrix[3])

print(matrix[0],[1])
'''
matrix = [

    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
#print(matrix)

for row in matrix:
    #print(row)
    for value in row:
        #print(value)
        if value == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')  
'''
for row in matrix:
    #print(row)
    for value in row:
        #print(value)
        if value == 1:
            print('1', end='')
        else:
            print(' ', end='')
    print('')  
'''