m = [3, 56, 78]
f = [4, 64, 304]



def modify(k):
    k.append(39)
    print("k = ", k)


def replace(g):  # Wrong function
    # g = [17, 28, 45]
    print("g = ", g)


def replace_correct(g):
    g[0] = 23
    g[1] = 11
    g[2] = 23
    print("g = ", g)


if __name__ == "__main__":
    modify(m)
    replace(f)
    print("f = ", f)
    replace_correct(f)
