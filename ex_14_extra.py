'''
Скласти програму визначення номера під'їзду та поверху квартири за заданим номером квартири.
У будинку 5 поверхів і 4 квартири на поверсі.

'''


# Input - 54

# Output_entrance - 3
# Output_floor - 4

flat_number = int(input('Enter flat number : '))
entrance_number = int((flat_number-1)// 20 + 1) # Devide flat_number on quantity flats in one entrance
print('Entrance number = ', entrance_number) 

floor_number = int(( (flat_number - 1) % 20) // 4 + 1) 
print('Floor number = ', floor_number) 
print(f"Flat : {flat_number}, Entrance : {entrance_number}, Floor : {floor_number}") 

'''
num = int(input("Enter flat number :"))
entrance_number = (num-1) // 20 + 1
floor_number = ((num-1) % 20) // 4 + 1

print(f"Flat : , {num}, Entrance : , {entrance_number}, Floor : , {floor_number}") 

'''

