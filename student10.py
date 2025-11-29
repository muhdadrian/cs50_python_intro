class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")



def get_student():
    student = Student() # here we're creating an object of that class
    student.name = input("Name: ")
    student.house = input("House: ")
    return student



if __name__ == "__main__":
    main()

# a class is a blueprint for pieces of data (object)
# ... three dots -- valid placeholder for temporarily
# we create a class --  using that class keyword -- but anytime we use a class -- you're creating objects -- here is the word object for OOP.
# with classes unlike dict. we can standardize those attributes and what kind of values we can set them for.