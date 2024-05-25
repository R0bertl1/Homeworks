def triange(n):
    temp = -1
    for i in range(n):
        print(" "*(n-1-i) + "*"*(temp+2))
        temp += 2

try:
    N = float(input("Введите высоту: "))
    if N != int(N):
        print("Нецелое число")
        N = None
    elif int(N) < 0:
        print("Отрицательное число")
        N = None
        
except ValueError:
    print("Некорректная высота")
    N = None

if N != None:
    triange(int(N))
