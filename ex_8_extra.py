#Скласти програму, яка вводить із клавіатури чотиризначне число і виводить на екран середнє арифметичне його цифр.

# Input - 2424
# Output - 3

num = int(input('Enter 4-digit number :'))

num_1 = num // 1000        #Spit first digit 
num_2 = (num // 100) % 10  #Spit second digit  
num_3 = (num // 10) % 10   #Spit third digit 
num_4 = num % 10           #Spit fourth digit   

print('num_1', num_1)
print('num_2', num_2)
print('num_3', num_3)
print('num_4', num_4)

average = (num_1 + num_2 + num_3 + num_4) / 4

print('Average number of digits', average)
