## Задача 11
#Результат пошуку згенерував n записів (вводиться користувачем).
#Скільки сторінок потрібно для відображення цих записів, якщо на 1 сторінку виводиться 10 записів.

# Input - 64
# Output - 7

# Input - 10
# Output - 1

notes = int(input('Enter quantities of notes : '))

pages = (notes - 1)  // 10 + 1

print(f"Pages is equal to {pages}")
