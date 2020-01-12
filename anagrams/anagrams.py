import sys

if len(sys.argv) == 2:
    fname = sys.argv[1]

    f = open(fname, "r")
    f_content = f.readlines()
    f.close()
    anagrams = []
    for e in f_content:
        lst = []
        for x in f_content:
            if set(x) == set(e):
                lst.append(x.strip())
                f_content.remove(x)
        anagrams.append(lst)
    for x in anagrams:
        print(" ".join(x))
else:
    print("You should enter a file name first.")
