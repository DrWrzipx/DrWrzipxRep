m = [3, 56, 78]
f = [4, 64, 304]


def modify(k):
    k.append(39)
    print("k = ", k)


def replace(g):
    # g = [17, 28, 45]
    print("g = ", g)


if __name__ == "__main__":
    modify(m)
    replace(f)
