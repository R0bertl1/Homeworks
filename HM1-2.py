def numbers(num):    
    numbers = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    ten = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", 
             "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", 
            "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", 
                "семьсот", "восемьсот", "девятьсот"]
    
    h = num // 100
    t = (num % 100) // 10
    n = num % 10
    answer = ''

    if h > 0:
        answer += hundreds[h] + ' '
    
    if t > 1:
        answer += tens[t] + ' '
        if n > 0:
            answer += numbers[n] +  ' '
    elif t == 1:
        answer += ten[t] + ' '
    else:
        answer += numbers[n]

    return answer

try:
    num = float(input("Введите целое число от 1 до 999: "))
    if num != int(num):
        print("Число нецелое")
        num = None
    if num < 0:
        print("Отрицательное число")
        num = None
except ValueError:
    print("Неккоректный ввод")
    num = None

if num != None:
    print(numbers(int(num)))