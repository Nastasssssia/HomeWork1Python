# Task 10
n = int (input("Введите количество монет:"))
count = 0
count_1 = 0
for i in range(n):
    coin = int (input("Введите сторону монеты, где 1 - орел, 0 - решка:"))
    if coin == 0:
       count+= 1
    elif coin == 1:
        count_1 += 1
if count > count_1:
    print(f"Минимальное количество монет, которое необходимо перевернуть - {count_1}")
else:
    print(f"Минимальное количество монет, которое необходимо перевернуть - {count}")

# Task 12

s = int (input("Введите сумму чисел:"))
p = int(input("Введите произедение чисел:"))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f"Перрвое число {x}, второе число {y}")
            

# Task 14
n = int (input("Введите число:"))
k = 0
i = 2
while i ** k <= n:
    print(f"{i ** k}")
    k+= 1