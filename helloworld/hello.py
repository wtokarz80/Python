import sys


def hello():
    if len(sys.argv) == 1:
        print("Hello World")
    else:
        print(f"Hello {sys.argv[1]}")


hello()
