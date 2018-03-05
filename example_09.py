"""Module for demonstrating exceptions
"""

def convert(s):
    """Convert to an integer
    """
    try:
        x = int(s)
        print("Conversion succeeded! x = ", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x

if __name__ == "__main__":
    convert("Burek")