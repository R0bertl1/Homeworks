def is_balanced(s: str) -> bool:
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
    
    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if stack and brackets[stack[-1]] == char:
                stack.pop()
            else:
                return False
    return True

def process_file(input_filename: str, output_filename: str):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            line = line.strip()
            result = is_balanced(line)
            outfile.write(f"{result}\n")


input_filename = 'input.txt'
output_filename = 'output.txt'
process_file(input_filename, output_filename)
