import random

class Hat:
    def __init__(self):
        self.houses = ["Tambunan", "Labuan", "Kota Kinabalu", "Keningau"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Adrian")
