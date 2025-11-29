students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

# lambda means anonymous function -- no need to give name as it will call only once.
# lambda calls takes parameter of student to call everyone of the student in the list.
# lambda can be used more than one place.
# lambda has no parenthesis, keyword and function name but get similar result like get_name.