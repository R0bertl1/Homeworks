def sum_of_num(n):
    if n % 9 == 0:
        print(9)
    else:
        print(n%9)

try:
    num = float(input("Введите число: "))
    if num != int(num):
        print("Нецелое число")
        num = None
    elif num < 0:
        num = -num
except ValueError:
    print("Некорректный ввод")
    num = None
if num != None:
    sum_of_num(int(num))
