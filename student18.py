class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house #2nd to call the setter method

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter -- function for a class to get some attributes
    @property # to define the getter
    def house(self):
        return self._house

    # Setter -- function for a class to set some values
    @house.setter
    def house(self, house):
        if house not in ["Tambunan", "Labuan", "Kota Kinabalu", "Keningau"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    # student.house = "Lot 4, Taman Ruby 2"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

"""
error checking in one place in the setter -- it will get called either when I create the object for the first time 
because of init or even you try to circumvent that init method 
and change the value of the attribute 'student.house = "Lot 4, Taman Ruby 2"' -- the setter 
will get call when I access dot house.  
"""

"""
#self._house = house -- the underscore is being used as the self.house = house inside the class cannot 
collide with the setter and getter.
#you cannot collide instant variable 'self.house = house' with the 'return self.house' function without 
the underscore indicator.
"""

"""
#student.house = "Lot 4, Taman Ruby 2" --  To call the setter
#But, it got to be removed to protect the data through init method and even defending the data -- 
["Tambunan", "Labuan", "Kota Kinabalu", "Keningau"] -- if you try to overwrite it there. 
So the only solution, don't try to break my code as it not gonna work,
and the line of code has to be removed.
"""