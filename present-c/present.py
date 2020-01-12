import sys

cons = ["b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
vow = ["a", "e", "i", "j", "o", "u", "y"]
verbs = []
i = 1
if len(sys.argv) > 1:
    while i < len(sys.argv):
        a = sys.argv[i]
        if a.isalpha() and a == "be":
            print("being")
        elif a.isalpha() and a.endswith("ie"):
            print(a.replace("ie", "y") + "ing")
        elif a.isalpha() and a.endswith("ee"):
            print(a.replace("ee", "eing"))
        elif a.isalpha() and a.endswith("e") and a[len(a) - 2] != "i":
            print(a.replace("e", "ing"))
        elif a.isalpha() and a[len(a) - 1] in cons and a[len(a) - 2] in vow and a[len(a) - 3] in cons:
            print(a + a[len(a) - 1] + "ing")
        elif a.isalpha():
            print(a + "ing")
        else:
            print("invalid value")
        i += 1
else:
    print("Enter a verb.")
