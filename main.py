m = int(input("Введите простое число: "))
i = 0
while i < m:
    i+=1
    if m % i == 0:
         print("Простое")
    else:
         print("Не простое")
    break
        