def read_grades(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    name, grade = line.split(',')
                    students.append((name.strip(), int(grade.strip())))
                except ValueError:
                    print(f"Некорректные данные в строке: {line.strip()}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None
    return students

def calculate_average(students):
    total = sum(grade for name, grade in students)
    count = len(students)
    return total / count

def write_above_average(students, average, filename):
    with open(filename, 'w') as file:
        for name, grade in students:
            if grade > average:
                file.write(f"{name}, {grade}\n")

def main():
    input_file = 'input.txt'
    students = read_grades(input_file)

    if students is not None:

        average = calculate_average(students)
        output_file = 'output.txt'
        write_above_average(students, average, output_file)

main()
