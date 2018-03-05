# Tuple
def tuple_collection(tuple):
    print(tuple[0])
    print(type(tuple))
    for item in tuple:
        print(item)


def string_collection(string, name="Jose", country="Germany"):
    print(string)
    print(len(string))
    for char in string:
        print(char)
    print(string.partition("so"))
    print("{0} is my remote coworker in {1}".format(name, country))


def range_collection(start_number, stop_number, step):
    for i in range(start_number, stop_number, step):
        print(i)


if __name__ == "__main__":
    t = ("Norway", 4.56, 3)
    tuple_collection(t)
    string_collection("Anna is so beautiful.", "Matic", "USA")
    range_collection(20, 1000, 40)


