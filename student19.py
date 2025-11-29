class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Tambunan", "Labuan", "Kota Kinabalu", "Keningau"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    student._house = "Lot 4, Taman Ruby 2" # _ sign make this code work or 'slipped'.
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# Python allows certain instant variable public, protected or private.
# Refer to hat.py for the next class lesson.