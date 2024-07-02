try:
    with open('cities.txt', 'r') as file:
        cities = [line.strip().split(':') for line in file.readlines()]
        flag = True

except FileNotFoundError:
    print("Ошибка: Файл cities.txt не найден.")
    flag = False

if flag:
    min_population = int(input("Введите минимальное значение населения: "))


    filtered_cities = [city for city, population in cities if int(population) > min_population]


    filtered_cities.sort()


    with open('filtered_cities.txt', 'w') as file:
        for city in filtered_cities:
            file.write(f"{city}\n")
