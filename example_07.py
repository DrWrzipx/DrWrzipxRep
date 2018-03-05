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


def banner(message, border_1="*", border_2="<"):
    line_1 = border_1 * len(message)
    line_2 = border_2 * len(message)
    print(line_2)
    print(line_1)
    print(message)
    print(line_1)
    print(line_2)


if __name__ == "__main__":
    import time
    modify(m)
    replace(f)
    print("f = ", f)
    replace_correct(f)
    banner(time.ctime(), "+", "!")
