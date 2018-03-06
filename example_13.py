if __name__ == "__main__":
    sunday = [32, 54, 66, 65, 87, 79]
    monday = [23, 45, 66, 56, 78, 97]
    for sunday, monday in zip(sunday, monday):
        print("avarage =", (sunday + monday)/2)