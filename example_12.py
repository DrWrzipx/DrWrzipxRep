def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


if __name__ == "__main__":
    #for x in lucas():
        #print(x)

    million_squares = (x*x for x in range(1, 1000000))
    print(list(million_squares))