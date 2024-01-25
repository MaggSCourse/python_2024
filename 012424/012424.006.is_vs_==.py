'''
006 is vs ==
'''

print('-------- == ---------')
print(True == 1) #T
print(' ' == 1) #F
print([] == []) #T
print(10.0 == 10) #T
print([1,2,3] == [1,2,3]) #T

print('--------- is --------')
print(True is 1) #F
print('' is 1) #F
print([] is []) #F
print(10.0 is 10) #T
print([1,2,3] is [1,2,3]) # F
print(10 is 10) #T


