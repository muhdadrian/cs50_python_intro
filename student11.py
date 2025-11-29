class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # This name of Student class treated as function -- passing values of name and house
    return student



if __name__ == "__main__":
    main()

# __init__ -- instance method -- to initialize the content of an object from a class -- you define this method.
# This is the manifestation of OOP.
# Student(name, house) -- generally known as 'constructor call' -- to construct a student object.