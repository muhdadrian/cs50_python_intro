class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Tambunan", "Labuan", "Kota Kinabalu", "Keningau"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "👞"
            case "Jack Russel terrrier":
                return "🐶"
            case _:
                return "🗡"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm()) # accessing the method inside of the student object even though the main function outside the class.


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()


# def __init__ and  def __str__ are methods and functions inside class
# the argument of self -- will be the reference of the current object of Harry's Object, Ron's Object etc.
# the convention must have at least an argument (self) inside a class -- to have access to the current object.
# def charm -- can use any name.