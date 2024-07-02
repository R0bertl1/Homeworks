try:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        flag = True
except FileNotFoundError:
    print("Ошибка: Файл input.txt не найден.")
    flag = False

if flag:
    course_students = {}
    for line in lines:
        line = line.split(':')

        name = line[0].strip()
        courses = line[1].split(',')

        temp = 0

        for course in courses:
            courses[temp] = course.strip().lower()

            if course == '\n':
                courses.pop(temp)
                continue

            if '\n' in course:
                courses[temp] = course[:-1]

            if courses[temp] in course_students:
                course_students[courses[temp]].append(name)
            else:
                course_students[courses[temp]] = [name]
            temp += 1


    print(course_students)
        
course_name = input("Введите название курса: ").strip().lower()

if course_name.lower() in course_students:
    print(f"Студенты, записанные на курс {course_name}:")
    for student in course_students[course_name]:
        print(student)
else:
    print(f"На курс {course_name} никто не записан или курс не существует.")
