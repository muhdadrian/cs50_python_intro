def meow(n: int) -> str: #The return value
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows) #No value --- None


