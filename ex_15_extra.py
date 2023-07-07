'''
Скласти програму визначення номера століття с за номером  n(n>0)
деякого року (врахувати що, наприклад, початком 20 століття був 1901, а не 1900 рік).

'''

# Input - 2023
# Output_century - 21

year = int(input('Enter year : '))

century = int((year - 1) // 100 + 1 )

print('Century :', century)

