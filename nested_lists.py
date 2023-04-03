'''hackerrank "Nested Lists" challenge '''

students = list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

students.sort(key = lambda x: x[1])
min_score = min(students, key = lambda x: x[1])

start_index = students.index(min_score) + sum(min_score[1] in item for item in students)
count_of_second_lowest = sum(students[start_index][1] in item for item in students)

second_lowest_grades = [student[0] for student in students[start_index : start_index + count_of_second_lowest]]
second_lowest_grades.sort()

print(*second_lowest_grades, sep='\n')
