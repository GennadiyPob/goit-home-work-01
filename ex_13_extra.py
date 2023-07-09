# В Інтернет-магазині зроблено 4 покупки: на $34.34, $12.01, $17.42, $4.93.
# Зі скількох доларів і центів складатиметься підсумкова сума.

# Input - 34.34, 12.01, 17.42, 4.93
# Output_dollars - 68
# Outputs_cents - 70

price_1 = float(input('Enter price_1 :'))
price_2 = float(input('Enter price_2 :'))
price_3 = float(input('Enter price_3 :'))
price_4 = float(input('Enter price_4 :'))

sum = price_1 + price_2 + price_3 + price_4

dolars = int(sum)
#cents = int((sum - int(sum))*100) Variant 1
cents = int(sum % 1 * 100)         #Variant 2
 
print(f'Dolars : {dolars}, Cents : {cents}')
