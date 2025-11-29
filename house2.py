name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": # | stands for or
        print("Gryffindor")
    # case "Harry":
    #     print("Gryffindor")
    # case "Harry":
    #     print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

    # _ (underscore) means whatever case is not yet handled