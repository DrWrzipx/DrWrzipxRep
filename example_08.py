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


def dictionary_collection(dictionary):
    for key, value in dictionary.items():
        print("{key} => {value}".format(key=key, value=value))


def set_collection():
    blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack'}
    blond_hair = {'Olivia', 'Lily'}
    print(blue_eyes.intersection(blond_hair))


if __name__ == "__main__":
    urls = {'Google': 'www.google.com',
            'Pluralsight': 'www.pluralsight.com',
            'Yahoo': 'www.yahoo.com',
            'Sixt': 'www.sixt.de'}
    t = ("Norway", 4.56, 3)
    tuple_collection(t)
    string_collection("Anna is so beautiful.", "Matic", "USA")
    range_collection(20, 1000, 40)
    dictionary_collection(urls)
    set_collection()


