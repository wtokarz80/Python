print("Hello, welcome to our gym, but first I have to ask you some questions, before I'll tel you the price.")
q = ["Are you over 14 years old? [Y/N]", "Would you like to use the sauna? [Y/N]", "Are you a student? [Y/N]", "Are you a men? [Y/N]"]
a = "I'm sorry, but below the age of 14, usage of the gym is forbidden."
b = "Ok"
c = "Ok, the price is 1500 HUF"
d = "Ok, the price is 300 HUF"
e = "Ok, the price is 750 HUF"
f = "Ok, the price is 500 HUF"

keep_asking = True
go_on = 1
while keep_asking:
    ask_1 = input(q[0])
    if ask_1 in ["Y", "y", "N", "n"]:
        if ask_1 == "N".lower():
            print("I'm sorry, but below the age of 14, usage of the gym is forbidden.")
            go_on = 0
            keep_asking = False
        elif ask_1 == "Y".lower():
            go_on = 1
            keep_asking = False
    else:
        keep_asking
if go_on == 0:
    print("Bye.")
elif go_on == 1:
    keep_asking2 = True
    while keep_asking2:
        ask_2 = input(q[1])
        if ask_2 in ["Y", "y", "N", "n"]:
            if ask_2 == "Y".lower():
                print("Ok, the price is 1500 HUF")
                keep_asking2 = False
            elif ask_2 == "N".lower():
                keep_asking2 = False
                keep_asking3 = True
                while keep_asking3:
                    ask_3 = input(q[2])
                    if ask_3 in ["Y", "y", "N", "n"]:
                        if ask_3 == "Y".lower():
                            print("Ok, the price is 300 HUF")
                            keep_asking3 = False
                        elif ask_3 == "N".lower():
                            keep_asking3 = False
                            keep_asking4 = True
                            while keep_asking4:
                                ask_4 = input(q[3])
                                if ask_4 in ["Y", "y", "N", "n"]:
                                    if ask_4 == "Y".lower():
                                        print("Ok, the price is 750 HUF")
                                        keep_asking4 = False
                                    elif ask_4 == "N".lower():
                                        print("Ok, the price is 500 HUF")
                                        keep_asking4 = False
                                else:
                                    keep_asking4
                    else:
                        keep_asking3
        else:
            keep_asking2
