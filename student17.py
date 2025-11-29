class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Tambunan", "Labuan", "Kota Kinabalu", "Keningau"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    student.house = "Lot 4, Taman Ruby 2" # to access those variable using this dot notation | setting the attribute inside class, read and change them latter
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # Student constructor is called here


if __name__ == "__main__":
    main()

# Classes do allow us to control the data we stored, but still can be changed using dot notation.
# Properties are going to be attribute that we can more control over.