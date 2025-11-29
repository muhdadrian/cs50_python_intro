class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls): # call this class method without instantiating a student object first
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get() # move the same code inside get function above: name and house
    print(student)


if __name__ == "__main__":
    main()

"""
class Student -- everything related with the student.
def main() -- other thing in file
if __name__ == "__main__": -- conditional to avoid accidentally executing the main when making a module,
package etc. 
"""