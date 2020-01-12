import sys


def read():
    f = open("ideabank.txt", "r")
    print("Your idea bank:")
    for i, line in enumerate(f):
        i += 1
        print(f"{i}. " + line.rstrip())
    f.close()


f = open("ideabank.txt", "r")
new_list = f.readlines()
f.close()

if len(sys.argv) == 2 and sys.argv[1] == "--list":
    read()
elif len(sys.argv) == 1:
    f = open("ideabank.txt", "a+")
    idea = input("What is your new idea?: ")
    f.write(idea+"\n")
    f.close()
    read()
elif len(sys.argv) == 3 and sys.argv[1] == "--delete" and sys.argv[2].isdigit():
    if int(sys.argv[2]) > 0 and int(sys.argv[2]) <= len(new_list):
        del_item = int(sys.argv[2])
        f = open("ideabank.txt", "r")
        del new_list[del_item-1]
        f.close()
        f = open("ideabank.txt", "w")
        for e in new_list:
            f.write(e)
        f.close()
        read()
    else:
        print("Element doesn't exist.")
else:
    print("Invalid command, try again.")
