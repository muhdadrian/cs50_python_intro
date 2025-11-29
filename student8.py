def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}



if __name__ == "__main__":
    main()

# refined version from student7.py by getting rid the dictionary.
