def read_lines(filename):
  
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []

def write_lines(filename, lines):

    with open(filename, 'w') as file:
        for line in lines:
            print(line, file = file)

def main():

    input_file1 = 'input1.txt'
    input_file2 = 'input2.txt'
    
    lines1 = read_lines(input_file1)
    lines2 = read_lines(input_file2)

    min_length = min(len(lines1), len(lines2))

    combined_lines = []

    for i in range(min_length):
        combined_lines.append(lines1[i] + lines2[i])

    if len(lines1) > len(lines2):
        for i in range(min_length, len(lines1)):
            combined_lines.append(lines1[i])
    elif len(lines2) > len(lines1):
        for i in range(min_length, len(lines2)):
            combined_lines.append(lines2[i])

    sorted_lines = sorted(combined_lines)

    output_file = 'output.txt'
    write_lines(output_file, sorted_lines)

main()
