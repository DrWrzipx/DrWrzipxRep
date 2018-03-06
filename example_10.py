def gen123():
    yield 1
    yield 2
    yield 3

if __name__ == "__main__":
    words = "Why sometimes I have believed as many as " \
            "sixt impossible things before breakfast".split()
    print([len(word) for word in words])

    iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
    iterator = iter(iterable)
    print(next(iterator))
    for v in gen123():
        print(v)

    i = gen123()
    h = gen123()
    print(i is h) # Two generate generator are not same
