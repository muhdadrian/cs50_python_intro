class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickels, {self.knuts} Knuts"


potter = Vault(100, 50, 25)
print(potter)

# def __str__(self): -- is used to remove the answer at below
# This is the answer: <__main__.Vault object at 0x10cafe390>