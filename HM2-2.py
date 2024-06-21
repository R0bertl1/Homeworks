def read_lines(filename):

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None

def process_lines(lines, chars_to_remove):

    processed_lines = []
    for line in lines:
        line = line.rstrip()
        original_line = line
        while line and line[-1] in chars_to_remove + ";":
            line = line[:-1]
        if line != original_line:
            line += ';'
        
        reversed_line = line[::-1]
        processed_lines.append(reversed_line)
    return processed_lines

def write_lines(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')

def main():
    input_file = 'input.txt'
    lines = read_lines(input_file)

    if lines is not None:
        chars_to_remove = input("Введите символы для удаления с правого края строки: ")

        processed_lines = process_lines(lines, chars_to_remove)

        output_file = 'output.txt'
        write_lines(output_file, processed_lines)

main()