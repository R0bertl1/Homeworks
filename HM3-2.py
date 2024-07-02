try:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Ошибка: Файл input.txt не найден.")
    lines = []

total_sales = {}


for line in lines:
    line = line.strip()
    if "}" in line or "{" in line:
        continue
    if line.endswith(','):
        line = line[:-1]
    product, amount = line.split(':')
    product = product.strip().strip('"')
    amount = int(amount.strip())

    if product in total_sales:
        total_sales[product] += amount
    else:
        total_sales[product] = amount


with open('output.txt', 'w') as file:
    for product, total in total_sales.items():
        file.write(f'"{product}": {total}\n')
