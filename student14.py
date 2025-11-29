class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Tambunan", "Labuan", "Kota Kinabalu", "Keningau"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return "a student"

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()


"""
def __str__(self):
    return "a student"
    
# The code above is to get rid the: <__main__.Student object at 0x10476e190>,
after the 'print(f"{student.name} from {student.house}")' changed to 'print(student)'
# The result above will produce string of 'a student'
"""
