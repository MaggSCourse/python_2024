'''
001. For loops
- iteration


'''

'''
course = 'Learning Python'

for letter in course:
    print(letter)

my_student_list = ['Paulina','Ulises','Maggie','Octavio','Ibrahim','Luis']
for student in my_student_list:
    print(student)

my_numbers_set = {10,20,30,40,50}
for number in my_numbers_set:
    print(number)

my_numbers_tuple = (10,20,30,40,50)
for number in my_numbers_tuple:
    print(number)
'''
#nested loop
my_number_list = [1,2,3,4,5]
my_letters_list = ['a', 'b', 'c','d', 'e']

for number in  my_number_list:
   # print(number)
    for letter in my_letters_list:
       # print(letter)
        print('-----')
        print(number,letter)