'''
У тризначному числі х закреслили його другу цифру. 
Коли до двозначного числа, що утворилося, ліворуч приписали другу цифру числа х,
то вийшло число y. Скласти програму знаходження числа y.

'''

# Input - 971
# Otput - 791

num = int(input('Enter three-digit number :'))
num_1 = num // 100
num_2 = (num // 10) % 10
num_3 = num % 10

print('num_1', num_1)
print('num_2', num_2)
print('num_3', num_3)

new_num = str(num_2) + str(num_1) + str(num_3)
print(new_num)

new_num = int(new_num) * 2
print(new_num)