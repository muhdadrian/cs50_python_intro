import random

class Hat:

    houses = ["Tambunan", "Labuan", "Kota Kinabalu", "Keningau"] #class variable

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



Hat.sort("Adrian") # capitalize 'H' in hat.

"""
@classmethod -- use class for container for data and functionality.
@ self.houses changed to cls.house -- it's not an instant variable anymore, but a class variable.  
"""