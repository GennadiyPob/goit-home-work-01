"""
Для кава-брейків на конференції закуплено: х круасанів, у стаканчиків, z упаковок кави.
Ціна круасана $1.04, ціна стаканчика - $0.34, ціна упаковки кави $4.42.
Скласти програму, яка обчислює, скільки повних доларів пішло на закупівлю
їжі для кава-брейків, і яка її вартість у доларах і центах.

"""


# Input_croissants - 4
# Input_cups - 5
# Input_coffee - 6
# Output_dollars - 32
# Output_cents - 3238

croissants = int(input('Enter q-ty of croissants :'))
cups = int(input('Enter q-ty of cups :'))
coffee = int(input('Enter q-ty of coffee :'))

sum = croissants * 1.04 + cups * 0.34 + coffee * 4.42

dollars = int(sum)
cents = int(sum * 100)
print('Dollars = ', dollars)
print('Cents = ', cents)
