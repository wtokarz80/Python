import random
import time
import datetime
import os
import grafika


def hangman():
    hangman = ['''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
     =========''']
    print(hangman[0])


def write_score():
    f = open("scores.txt", "a+")
    name = input("Enter your name: ")
    time = round(stop_time)
    d = datetime.datetime.today()
    date = d.strftime("%d-%m-%Y")
    win_word = (cant_cap[1])
    scores = []
    scores.insert(0, name)
    scores.insert(1, str(time))
    scores.insert(2, str(date))
    scores.insert(3, win_word)
    f.write("|".join(scores)+"\n")
    f.close()


def read_score():
    f = open("scores.txt", "r")
    scores_list = f.readlines()
    f.close()
    global scores_list_list
    scores_list_list = []
    for e in scores_list:
        x = e.split("|")
        scores_list_list.append(x)
    return scores_list_list


def Sort(scores_list_list):
    scores_list_list.sort(key=lambda x: int(x[1]))
    return scores_list_list


def main():
    f = open("capitals.txt", "r")
    file_content = f.readlines()
    f.close()
    lifes = 10
    for e in file_content:
        file_element = random.choice(file_content)
    new_list = file_element.split("|")
    global cant_cap
    cant_cap = []
    for x in new_list:
        cant_cap.append(x.strip())
    capital = cant_cap[1].lower()
    start_time = time.time()
    letters = []
    word = []
    used_letters = []
    for e in capital:
        if e == " ":
            word.append(" ")
        else:
            word.append("_ ")
    while lifes > 0:
        os.system('clear')
        print(grafika.big_one)
        print(capital)
        print('''Hello, welcome to hangman :)
Guess the capital's name.''')
        print("".join(word)+"\n")
        print(f"Your life points: {lifes}  |  not in word: " + ", ".join(used_letters) + "\n")
        if lifes in range(1, 3):
            print(f"I see you need a little help...this is capitol of {cant_cap[0]}.")
        ask = input("Enter a letter or guess the answer: ").lower()
        if len(ask) > 1:
            if ask.lower() == capital:
                print("\n" + capital.upper())
                global stop_time
                stop_time = (time.time() - start_time)
                print(f"\nBravo! :) you guessed the capital after {len(letters)} letters. It took you {round(stop_time)} seconds.\n")
                write_score()
                read_score()
                new_game_ask = input("\nDo you want to play again? [Y] or press any key to exit: ").lower()
                if new_game_ask == "y":
                    main()
                else:
                    break
            else:
                print("\nYou did not guess.")
                lifes -= 2
        elif len(ask) == 1:
            guest_corretly = False
            for i, e in enumerate(capital):
                if e == ask:
                    word.insert(i, ask.upper())
                    word.pop(i+1)
                    letters.append(ask)
                    guest_corretly = True
            print("\n" + "".join(word) + "\n")
            if guest_corretly:
                if ("".join(word)).lower() == capital:
                    stop_time = (time.time() - start_time)
                    print(f"Bravo! :) you guessed the capital after {len(letters)} letters. It took you {round(stop_time)} seconds.\n")
                    write_score()
                    read_score()
                    new_game_ask = input("Do you want to play again? [Y] or press any key to exit: ").lower()
                    if new_game_ask == "y":
                        main()
                    else:
                        print("\nThank you and bye.")
                        break
            else:
                print("Letter doesn't exist in name.\n")
                lifes -= 1
                letters.append(ask)
                used_letters.append(ask)
    else:
        print("You die.\n")
        hangman()
        new_game_ask = input("\nDo you want to play again? [Y] or press any key to exit: ").lower()
        if new_game_ask == "y":
            main()
        else:
            print("\nThank you and bye.")


main()

result_score_list = read_score()

Sort(result_score_list)
ala = result_score_list
# print(result_score_list)
dash = '-' * 43
print("Ten best scores:")
print(dash)
print('{:<5s}{:<9s}{:>3s}{:>8s}{:>14s}'.format("No.", "Name", "Time(s)", "Date", "Capitol"))
print(dash)
i = 0
for i, e in enumerate(result_score_list):
    e = '{:<5s}{:<12s}{:^2s}{:>13s}{:^17s}'.format(f"{i+1}.", ala[i][0], ala[i][1], ala[i][2], ala[i][3])
    i += 1
    print(e)
    # print(f"{i}. " + "  |  ".join(e))
    if i == 10:
        break
