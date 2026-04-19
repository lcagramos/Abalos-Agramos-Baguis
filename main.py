import json
import time
import random

with open("items.json", "r") as f:
    item = json.load(f)

with open("inventory.json", "r") as f:
    data = json.load(f)

with open("quizbee.json", "r") as f:
    questions = json.load(f)

for question in questions:
    question["answered"] = False
    with open("quizbee.json", "w") as f:
        json.dump(questions, f, indent=4)

newItem = ""

name = input("Welcome to Paithon's Gacha! What is your name, traveler? ")

print("\n\n")
print(" .-.---------------------------------.-.")
print(" ((o))                                   )")
print(" ( )_______          _____         ____/")
print("  |             MAIN MENU            |")
print("  |                                  |")
print("  |  1. Start Game                   |")
print("  |                                  |")
print("  |  2. How to Play                  |")
print("  |                                  |")
print("  |  3. Credits                      |")
print("  |                                  |")
print("  |  4. Quit                         |")
print("  |                                  |")
print("  |____    _______    __  ____    ___|")
print(" / )                                  )")
print("((o))                                  )")
print(" '------------------------------------'")


print("\n\n")
menuChoice = ""
while True:
    try:
        menuChoice = int(input("\nEnter choice (1-4): "))
        if 1 <= menuChoice <= 4:
            break
        else:
            print("Enter a number between 1 to 4.")
    except ValueError:
        print("Invalid input! Try again.")

if menuChoice == 1:
    print("Paithon: Hello player! In this game, you must play Python-coding related minigames and answer questions"
        "\nto obtain a special currency called Primogems in order to wish on the current banner. You need 1,600 "
        "\nPrimogems to wish. Good luck!")

    while True:
        print("\nChoose a category (or 0 to wish):")
        print("0. Go stargazing")
        print("1. Easy (Formative Assessment)")
        print("2. Medium (Alternative Assessment)")
        print("3. Hard (Summative Assessment)")

        categoryChoice = ""
        while True:
            try:
                categoryChoice = int(input("Choose a category (1-3, 0 to quit): "))
                if 0 <= categoryChoice <= 3:
                    break
                else:
                    print("Enter a number between 0 to 3.")
            except ValueError:
                print("Invalid input! Try again.")

        if categoryChoice == 0:
            print("You gaze upon the stars as you wish for a companion... ⋆˙⟡ ⋆.˚ ⊹₊⟡ ⋆")
            time.sleep(2)
            print("You see a shooting star.")

            print("Make a wish? (1600 primogems)")
            wChoice = input("(Yes/No: ").strip().lower()

            if wChoice == "yes":
                if data["primogems"] >= 1600:
                    data["primogems"] -= 1600

                    for i in range(0,8):
                        chance = random.randint(1, 100)
                        if 1 <= chance <= 50:
                            newItem = item[0][random.randint(0,4)]
                            print(f"You find a weapon, a unique kind... it's the {newItem}! ☆☆☆")
                            data["inv"].append(newItem)


                        elif 51 <= chance <= 65:
                            newItem = item[1][1][random.randint(0,11)]
                            BLUE = "\033[94m"
                            RESET = "\033[0m"

                            print(BLUE + """⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⣀⣀⡠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                        ⠀⢸⢉⡗⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠈⡱⠖⠀⠀⠀⠀⠀ ⠀⠀⠀⣄⣠⠆⠀
                                                        ⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠰⠓⠒⢴⠀⠀⠀⠀ ⠀ ⠀⠀⣀⠀⠀⢨⠀⣰⠃
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⢀⠜⢹⡀⠀⠀⠀⠈⠀
                                                        ⠀⠀⠀⠀⢠⣀⣶⠀⠀⠀⠀⠀⠀  ⠀⢤⢀⣀⣀⣀⡠⠋⠀⠀⢇⠀⠀⠀⠀⠀
                                                        ⠀⠀⠀⠀⠀⡇⣄⠊⠁⠀⠀⠀⠀⠀⢀⡨⢦⠀⠀⠀⠀⠀⠀ ⠀⠘⠒⠤⣀⡀⠀
                                                        ⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⡀⠔⠊⠁⢀⡀⠳⡀⠀⠀⠀⠀ ⠀⠀⠀⠀⣀⠼⠋
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠈⡀⠄⠂⠉⢀⡀⢰⠁⠀⠀⠀ ⠀⠀⠀⡴⠊⠁⠀⠀
                                                        ⠀⠀⠀⠀⠀⠀⡠⢊⠠⠒⣁⠤⠐⣀⡁⠤⢤⠃⢀⣀⡠⢄⡀⠀⠀⡇⠀⠀⠀⠀
                                                        ⠀⠀⠀⠀⡠⡪⢐⡡⢐⠩⠐⠊⠁⠀⠀⠀⠚⠉⠉⠀⠀⠀⠙⠢⣀⡇⠀⠀⠀⠀
                                                        ⠀⠀⢠⡪⡪⡲⠕⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⠃⠀⠀⠀⠀
                                                        ⠀⣰⣿⠞⠉⠀⠀⠀⠀⠀⡄⡰⡆⠀⠀⠀⠀⠀⠀⢐⣌⡶⠀⠀⠀⠀⠀⠀⠀⠀
                                                        ⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⣸⠤⡐⠁⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀
                            """ + RESET)
                            time.sleep(0.5)

                            print(f"You wished, and you received {newItem}! ☆☆☆☆")
                            data["inv"].append(newItem)


                        elif 66 <= chance <= 85:
                            newItem = item[1][0][random.randint(0, 4)]

                            print(BLUE + """⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⣀⣀⡠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                        ⠀⢸⢉⡗⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠈⡱⠖⠀⠀⠀⠀⠀ ⠀⠀⠀⣄⣠⠆⠀
                                                        ⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠰⠓⠒⢴⠀⠀⠀⠀ ⠀ ⠀⠀⣀⠀⠀⢨⠀⣰⠃
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⢀⠜⢹⡀⠀⠀⠀⠈⠀
                                                        ⠀⠀⠀⠀⢠⣀⣶⠀⠀⠀⠀⠀⠀  ⠀⢤⢀⣀⣀⣀⡠⠋⠀⠀⢇⠀⠀⠀⠀⠀
                                                        ⠀⠀⠀⠀⠀⡇⣄⠊⠁⠀⠀⠀⠀⠀⢀⡨⢦⠀⠀⠀⠀⠀⠀ ⠀⠘⠒⠤⣀⡀⠀
                                                        ⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⡀⠔⠊⠁⢀⡀⠳⡀⠀⠀⠀⠀ ⠀⠀⠀⠀⣀⠼⠋
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠈⡀⠄⠂⠉⢀⡀⢰⠁⠀⠀⠀ ⠀⠀⠀⡴⠊⠁⠀⠀
                                                        ⠀⠀⠀⠀⠀⠀⡠⢊⠠⠒⣁⠤⠐⣀⡁⠤⢤⠃⢀⣀⡠⢄⡀⠀⠀⡇⠀⠀⠀⠀
                                                        ⠀⠀⠀⠀⡠⡪⢐⡡⢐⠩⠐⠊⠁⠀⠀⠀⠚⠉⠉⠀⠀⠀⠙⠢⣀⡇⠀⠀⠀⠀
                                                        ⠀⠀⢠⡪⡪⡲⠕⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⠃⠀⠀⠀⠀
                                                        ⠀⣰⣿⠞⠉⠀⠀⠀⠀⠀⡄⡰⡆⠀⠀⠀⠀⠀⠀⢐⣌⡶⠀⠀⠀⠀⠀⠀⠀⠀
                                                        ⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⣸⠤⡐⠁⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀
                            """ + RESET)
                            time.sleep(0.5)

                            print(f"You find a new companion, it's {newItem}! ☆☆☆☆")
                            data["inv"].append(newItem)

                        elif 86 <= chance <= 99:
                            fiftyF = random.randint(1,100)
                            print(f"You find a very special companion...!")
                            BLUE = "\033[94m"
                            RESET = "\033[0m"

                            print(BLUE + """⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⣀⣀⡠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                        ⠀⢸⢉⡗⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠈⡱⠖⠀⠀⠀⠀⠀ ⠀⠀⠀⣄⣠⠆⠀
                                                        ⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠰⠓⠒⢴⠀⠀⠀⠀ ⠀ ⠀⠀⣀⠀⠀⢨⠀⣰⠃
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⢀⠜⢹⡀⠀⠀⠀⠈⠀
                                                        ⠀⠀⠀⠀⢠⣀⣶⠀⠀⠀⠀⠀⠀  ⠀⢤⢀⣀⣀⣀⡠⠋⠀⠀⢇⠀⠀⠀⠀⠀
                                                        ⠀⠀⠀⠀⠀⡇⣄⠊⠁⠀⠀⠀⠀⠀⢀⡨⢦⠀⠀⠀⠀⠀⠀ ⠀⠘⠒⠤⣀⡀⠀
                                                        ⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⡀⠔⠊⠁⢀⡀⠳⡀⠀⠀⠀⠀ ⠀⠀⠀⠀⣀⠼⠋
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠈⡀⠄⠂⠉⢀⡀⢰⠁⠀⠀⠀ ⠀⠀⠀⡴⠊⠁⠀⠀
                                                        ⠀⠀⠀⠀⠀⠀⡠⢊⠠⠒⣁⠤⠐⣀⡁⠤⢤⠃⢀⣀⡠⢄⡀⠀⠀⡇⠀⠀⠀⠀
                                                        ⠀⠀⠀⠀⡠⡪⢐⡡⢐⠩⠐⠊⠁⠀⠀⠀⠚⠉⠉⠀⠀⠀⠙⠢⣀⡇⠀⠀⠀⠀
                                                        ⠀⠀⢠⡪⡪⡲⠕⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⠃⠀⠀⠀⠀
                                                        ⠀⣰⣿⠞⠉⠀⠀⠀⠀⠀⡄⡰⡆⠀⠀⠀⠀⠀⠀⢐⣌⡶⠀⠀⠀⠀⠀⠀⠀⠀
                                                        ⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⣸⠤⡐⠁⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀
                            """ + RESET)
                            if 1 <= fiftyF <= 50:
                                newItem = item[2][0]

                                YELLOW = "\033[93m"
                                RESET = "\033[0m"

                                print(YELLOW + """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠤⢤⣀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠐⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⢋⣉⣀⣠⣄⣀⣈⡇
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⣸⡆⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⣠⣴⣾⣯⠴⠚⠉⠉⠀⠀⠀⠀⣤⠏⣿
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣄⠀⠀⠀⠀⠀⠀⡿⡇⠁⠀⠀⠀⠀⠀⠀⠀⡀⠂⠀⠀⠀⠀⣠⣴⡿⠿⢛⠁⠁⣸⠀⠀⠀⠀⠀⣤⣾⠵⠚⠁
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⢄⠀⠀⣠⠀⡇⢧⠀⠀⠀⠀⠀⠀⠖⠁⠀⠀⠀⣠⣴⠿⠋⠁⠀⠀⠀⠀⠘⣿⠀⣀⡠⠞⠛⠁⠂⠁⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⣻⡦⣞⡿⣷⠸⣄⣠⢶⡟⠁⠀⠀⠀⣀⣴⠟⠋⠁⠀⠀⠀⠀⠐⠠⡤⣾⣙⣶⡶⠃⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣂⡷⠰⣔⣾⣖⣾⡷⢿⣀⣀⣀⣤⢾⣋⠁⠀⠀⠀⣀⢀⣀⣀⣀⣀⠀⢀⢿⠑⠃⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠠⡦⠴⠴⠤⠦⠤⠤⠤⠤⠤⠴⠶⢾⣽⣙⠒⢺⣿⣿⣿⣿⢾⠶⣧⡼⢏⠑⠚⠋⠉⠉⡉⡉⠉⠉⠹⠈⠁⠉⠀⠨⢾⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠂⠐⠀⠀⠀⠈⣇⡿⢯⢻⣟⣇⣷⣞⡛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣆⠀⠀⠀⠀⢠⡷⡛⣛⣼⣿⠟⢙⣧⠇⡄⠀⠀⠀⠀⠀⠀⠰⡆⠀⠀⠀⠀⢠⣾⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⢶⠏⠉⠀⠀⠀⠀⠀⠿⢠⣴⡟⡗⡾⡒⡿⠯⢏⡅⠀⠀⠀⠀⣀⢀⣠⣧⣀⣀⠀⠀⠀⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⣠⢴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⣠⣷⢿⣫⡽⡿⠿⠗⢷⠀⠀⠑⣗⡀⠀⠀⠀⠈⠙⣿⢭⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⢀⡴⢏⡵⠛⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠛⠀⠰⡟⣿⠀⡌⠀⠀⠀⠀⠀⠀⠁⠢⡀⠀⠀⠂⢿⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⣀⣼⠛⣲⡏⠁⠀⠀⠀⠀⠀⢀⣠⡾⠋⠉⠀⠀⠀⠀⣧⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⡴⠟⠀⢰⡯⠄⠀⠀⠀⠀⣠⢴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⡾⠁⠁⠀⠘⠧⠤⢤⣤⠶⠏⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠘⣇⠂⢀⣀⣀⠤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                """ + RESET)
                                print("You meet the limited 5-star character..!")
                                time.sleep(0.5)
                                print("☆☆☆☆☆")
                                time.sleep(0.5)
                                print("You got Adeptus Xiao!")
                                time.sleep(1)

                                print(r"⠀⠀⠀            ⠀⢀⠀⠉⠀⠀⣀⣤⠖⠀⠀⠀⠀⠐⠢⠄⠒⠢⠀⠀⠉⠁⢲⣶⣶⣶⣶⣶⣦⣠⡿⠟⠉⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"                ⠋    ⣰⣿⠿⣶⣤           ⠘⣿⡿⠛⠛⠻⣿⣿⣿⣿⣿⣿⡟⠛⠛⠒⢦⣤⣀⡀⠞⠉⠉⠓⢦⡀               ")
                                time.sleep(0.5)
                                print(r"               ⣀⣄⣀⠀⣼⠋⠀⠀⠈⢻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠻⡆⠀⠀⠀⠈⣿⣿⣿⣿⣟⡀⠀⠀⠀⠀⠟⠛⠻⡆⠀⠀⠀⠀⠹⠟⢲          ")
                                time.sleep(0.5)
                                print(r"            ⠀⠄⠁⠀⠉⣿⣿⣠⡆⠀⠀⠀⢿⣷⡀⠀⠀⠀⠀⢠⣞⠃⢠⠟⠁⠀⠀⢹⣰⢄⣀⡰⠋⠉⠉⠀⠈⠙⠲⣀⠀⠠⠄⠀⠀⢹⡶⠦⣤⡖⠦⠄⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⣴⡿⠛⣿⡇⠀⠀⠀⠘⣿⣧⣤⣤⣦⣴⠟⠉⠛⠋⠀⠀⠀⢀⡼⢣⣌⣹⠃⠀⠀⠀⠀⢰⠀⠀⠈⠳⡂⠀⠀⠰⣾⠁⠀⠀⠻⣦⣤⣀⡀⢱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⢀⣼⣿⡶⣰⣿⣿⡀⠀⠀⠀⣼⣇⣴⣿⡟⢁⣤⣤⣤⣴⣷⣀⣒⣋⡸⠋⠈⠙⠦⣄⠀⠀⣠⣧⡴⠋⠀⠀⠘⣦⠀⠀⢸⣧⣀⠀⠀⠘⡆⠀⠉⠛⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⢀⠻⠏⢻⣿⣿⣿⣿⣧⠀⢀⢸⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠈⠁⠀⠈⣻⣆⠀⠀⠀⠀⣿⡿⠋⠁⠈⠛⠲⢤⣄⣸⣤⣤⣼⡿⢩⣿⠗⠒⠻⣄⠀⠀⡸⣧⠙⢷⡀⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⢀⣥⣦⣘⣿⣿⣿⣿⣿⣀⣾⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠿⢿⣦⡀⣠⣾⣿⣷⡄⠀⠀⠀⠀⠀⠈⠉⠻⢿⣍⠀⠸⠃⠀⠀⠀⠈⠓⠂⠃⢹⠀⡜⠳⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠇⠀⠈⣿⣯⣿⣿⠟⠉⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢸⡇⠀⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⣄⠀⠀⢸⣿⣿⣿⣿⣿⣿⡛⠉⠛⢷⠀⠀⠀⠀⠀⢀⡄⠀⠀⡤⢠⠟⠀⠀⠀⠸⣿⡿⠁⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣤⣤⣄⣀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⣿⣇⣤⠞⠉⠛⠛⠛⠛⢛⣷⣄⣠⠿⠀⠀⠀⠀⢀⡼⠃⠀⣸⠃⣸⠀⠀⠀⠶⠤⠿⠁⠀⠠⢀⣀⡇⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣈⠙⠻⣦⡀⠀⢸⣦⡀⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⣿⠟⠁⠀⠀⠀⠀⠀⢀⣾⢿⣿⠁⠀⠀⠀⠀⢠⣾⡇⠀⢠⡿⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠘⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡉⠛⠿⠶⣬⣿⣦⣼⠅⠛⠶⠄⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠃⠀⠀⠀⠀⠀⠀⢀⣼⠏⣾⡇⠀⠀⠀⠀⣠⣾⡿⠀⢀⣿⠃⣿⣿⠀⠀⠀⠀⢀⣾⠀⠀⠀⠀⠀⢹⡇⢸⣧⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⣤⣄⣉⣉⡤⠀⣠⠆⠀⠀⠉⠁")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⣤⣀⣀⣤⠞⠁⢰⣿⠀⠀⠀⠀⣠⣟⣿⠃⢀⣾⠏⠀⢸⣿⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢸⡇⠀⢻⣧⠘⣿⣆⠀⠀⠄⠀⠀⠀⠀⠀⠙⠛⢶⣥⣄⢀⣴⣿⣤⡤⠔⠚⠁")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠙⢿⣯⣥⣤⣤⣾⡇⠀⠀⠀⠠⣿⡿⠃⢠⣾⣏⣀⣀⠈⣿⡆⣀⡀⠀⠈⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⢿⣧⣸⣝⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⠿⠤⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀⠀⣀⣾⠟⠁⣰⣿⣁⡉⠉⢉⠉⢿⣿⠋⠁⠀⠀⠀⠀⠈⠳⠶⠶⣿⡷⠖⠒⠚⢻⣿⣿⡎⠻⢶⣄⡀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⣰⣿⣯⣴⣾⡿⠿⢿⣿⣶⣦⣀⡈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⣀⣀⣿⣿⣿⣦⣄⡉⢻⣿⢿⣷⣦⣀⡤⡤⣄⣀⡀⠀⠙⣦⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣧⣼⠟⠀⣩⣿⣯⡀⠀⢸⡏⣂⣿⣟⣻⡿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣼⣣⣼⡿⢻⣯⡛⠻⣿⣿⣿⣿⣿⣿⣿⣦⣄⠅⠹⣿⣿⣿⣿⣿⣿⡙⢻⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠾⣿⣼⣿⡿⠏⢀⣠⣾⣿⢿⣏⠃⣀⢘⣿⣮⣻⣯⣿⣇⠈⠙⢦⡀⠀⠀⠀⠀⡼⠋⠀⢸⣿⣿⠿⣥⡼⠟⠈⢻⣿⣿⣼⣿⠋⠙⠳⣦⣈⡻⠿⣿⣿⣿⡿⣮⣄⡀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠐⠦⠤⠤⠤⠿⣿⣶⣾⣿⠿⠉⠀⢸⣿⡆⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠚⠁⠀⠀⠈⠉⠉⠉⠉⠰⠶⠒⠛⠛⢿⣿⣿⡀⠀⠀⣿⣿⣿⣷⣶⣿⠿⠁⢈⣉⣿⡶")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⡀⡇⠀⠈⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⢿⣷⣦⣠⣿⣿⣿⡟⠛⠿⠶⠶⠛⢋⡥⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠛⠋⣿⣿⣿⣽⣿⠀⠀⢹⣯⠛⠳⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠈⣹⣿⣿⣯⣟⡳⠤⠔⣒⣾⠾⠋⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢻⣿⣿⣿⣦⣀⠀⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣎⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⡉⠉⠉⠁⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣯⡾⢿⡇⠻⣿⣿⣷⣼⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⠀⠈⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⣠⡾⡟⢸⣿⣿⡿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣋⡁⠀⠀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣧⠀⢘⣻⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣯⣾⣇⣤⢻⣾⠄⠹⣧⠈⢿⣿⣿⣿⣿⣿⣿⣟⠛⠛⠛⠉")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⢀⣿⣯⠻⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠛⡿⣿⣿⡇⠙⠿⣆⣹⣧⠀⢹⣇⠀⠹⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣇⠹⣿⣿⣿⣿⣿⣏⠳⣄⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠁⠀⣼⠃⣿⡿⠀⠀⠀⠈⠉⢻⡆⠀⣿⢷⣤⡸⣿⡹⣿⣿⣿⣿⣿⣆⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠒⠒⠦⢤⣤⣀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣷⡸⣿⣿⣿⣿⣿⣦⡈⠳⢦⣤⣤⣤⠾⠛⠉⠀⠀⣠⣼⣿⠴⠋⠀⠀⠀⠀⠀⠀⠈⣿⠀⢻⠀⠈⠻⣾⣧⠈⢿⣿⣿⣿⣿⣧")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢳⠲⣤⣤⣤⣄⣀⣹⣿⣿⣷⣌⢿⣿⣟⣿⣿⣿⣷⣦⣄⠁⠀⠀⠀⠀⠀⣴⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⢸⠀⠀⠀⠈⢻⣧⠀⢻⣿⣿⣿⣿")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⣿⣿⣟⡿⣿⣿⣿⣎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⢸⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣾⠀⠀⠀⠀⠀⠙⣿⣄⢿⣿⡟⣿")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣧⠙⣿⣿⣿⣷⣻⣿⡟⢿⣿⣿⣿⣿⣿⣷⠀⢠⣿⣿⣿⣿⡟⢦⡀⠀⢀⣀⣀⠀⠀⠀⢀⣿⡏⠀⠀⠀⠀⠀⠀⢹⣿⣮⠹⠇⢻")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⣿⡀⠛⣿⣿⣿⣿⣆⢻⣿⣿⣿⣿⣿⣆⣾⣿⣿⣿⣿⣿⡄⢻⣶⣧⡀⢹⣷⣄⣀⣾⠛⠀⠀⠀⠀⠀⠀⣠⠾⠛⣿⣆⠁⢸")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡟⠛⠻⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⢸⣿⣿⣿⡀⠀⢸⡟⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⣿⣿⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠉⠻⣦⣀⣠⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣿⣿⣿⣿⣿⣷⠶⠞⢷⣶⣄⡀⠀⢀⣰⠏⠀⠀⠀⠀⡟⡏⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⢸⡏⠀⠀⢹⣿⣷⣬⣿⣿⠻⢿⣿⣿⣿⣿⣿⠏⣾⣿⣿⣿⣿⣿⣿⣄⠀⢀⣿⣿⣿⣷⣮⣅⡀⠀⠀⠀⣼⣽⠖⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠠⣌⢷⣤⠔⠚⢿⣿⣿⣿⡟⠀⠀⠙⢿⣿⣿⣟⣼⣿⣿⠻⣿⣿⣿⡏⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣷⢦⣾⣿⣀⡀⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠘⣯⡀⠀⢠⣿⡋⢹⣷⡀⠀⠀⢸⠟⡇⠁⣿⣿⣿⠀⠀⠈⣻⠧⣄⣰⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⠀⠀")
                                time.sleep(0.5)
                                print(r"            ⠉⢳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⢀⣽⣿⣿⠋⠀⠹⣾⣿⡿⢦⠀⢸⠀⡇⠀⣿⢿⣿⣧⠀⠀⡇⠀⠀⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠉⠉⠻⣄⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⢻⡟⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⢀⣴⣿⡿⠋⠘⢦⣤⠾⠛⣯⠀⠈⠳⣞⠀⣿⡼⠃⠀⠈⠛⢦⡤⠗⠢⣾⡏⠀⠈⠻⣿⣿⣿⣿⣿⣿⣀⡀⣀⠀⠀⢹⠀")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⣧⢻⡘⣄⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⣼⣿⡿⣻⠟⠁⠀⠀⠀⠀⢣⣄⠀⣸⣭⣄⠀⠈⠛⣿⢧⡀⠀⠀⢀⣨⣇⡀⢠⡟⠀⠀⠀⠀⣾⠻⣿⣿⣿⣿⣿⣿⡏⠀⠀⢸⣿")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠹⣜⣧⠀⠳⣄⠀⠀⠰⡀⠀⠀⠀⠀⢰⣿⡏⡼⠋⠀⠀⠀⠀⠀⠀⠀⠙⣿⠁⠀⠈⢳⣄⡞⠃⠀⠹⣄⣼⠋⠀⠈⣿⡿⠀⠀⠀⠀⠀⠙⠳⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⡿")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⢿⣿⡀⠀⠈⠳⣄⠀⢷⠀⠀⠀⢠⣿⣿⣿⣿⢞⡿⠀⠀⠀⠀⠀⠀⠀⢻⣀⣴⣶⣾⣏⡷⠻⣆⣰⣿⣿⣤⣴⣾⣿⡃⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⠀⠀⠀⢀⣁")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠈⣿⣧⠀⠀⠀⠈⢣⡈⣦⠀⢠⣿⣿⣿⣿⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⢰⣛⣿⣟⢿⡞⣇⢀⣾⣿⠉⢻⣿⣿⣻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡟⠀⠀⠀⢸⣿")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠹⣿⡇⠀⠀⠀⠀⠉⠹⣤⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡿⠀⠙⢿⣿⣿⣿⣿⠟⠀⠛⡿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⢸⣿")
                                time.sleep(0.5)
                                print(r"            ⠀⠀⠀⠀⠀⠀⢻⣿⣄⠀⠀⡀⣀⣴⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠩⣿⡀⠀⢀⡼⠛⢹⣿⡅⠀⠀⠀⣧⣻⢵⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⢻")

















                                data["inv"].append(newItem)
                            else:
                                print("You find a 5-star from the permanent wish! A formidable companion indeed~")
                                print(f"You got...")
                                time.sleep(0.5)
                                print(f"☆☆☆☆☆ {newItem}!")


                else:
                    print("You don't have enough primogems... (¬_¬＂)")

            elif wChoice == "no":
                print("You decide to save your wish for another day. ✧｡٩(ˊᗜˋ )و✧*｡")
            break

        if categoryChoice == 1:
            category = "Easy"
            reward = 60
        elif categoryChoice == 2:
            category = "Medium"
            reward = 110
        else:
            category = "Hard"
            reward = 150

        while True:
            matchingQuestion = [q for q in questions if q["category"] == category]

            if not matchingQuestion:
                print(f"No questions available for {category}.")
                break

            question = random.choice(matchingQuestion)

            if isinstance(question["text"], list):
                text = " ".join(question["text"])
            else:
                text = question["text"]

            print("\n" + text)
            print("Choices:", ", ".join(question["choices"]))
            answer = input("Enter your answer: ")

            if answer.lower() == question["answer"].lower():
                print(f"Paithon: Correct! You earned {reward} Primogems ദ്ദി(｡•̀,<)~✩‧₊\n")
                data[0]["primogems"] += reward
                with open("inventory.json", "w") as f:
                    json.dump(data, f, indent=4)
            else:
                print(f"Paithon: Wrong! (╥﹏╥) The correct answer is {question['answer']}.\n")

            question["answered"] = True

        # Save updated questions
        with open("quizbee.json", "w") as f:
            json.dump(questions, f, indent=4)

elif menuChoice == 2:
    print("Instructions (enter to continue):\n"
          "")

    input("Paithon: Welcome player! In this game, you can obtain many \n"
          "characters and weapons, however, you must first earn a currency called \"Primogems\".\n")

    input("Paithon: To earn Primogems, you have to answer quiz bee questions\n"
          "related to Python coding concepts. There’s 3 difficulties: \n"
          "Easy (Formative Assessment), Medium (Alternative Assessment), \n"
          "and lastly, Hard (Summative Assessment).\n\n")

    print("Paithon:")
    print(" o Easy gives 60 Primogems per question")
    print(" o Medium gives 110 Primogems per question")
    print(" o Hard gives 150 Primogems per question")
    input(" o Each level contains five items!\n\n")

    print("Paithon: So, you might be asking, \"What do I do with all these primogems..?\" \n"
          "Well, first..!")
    print(" o You can convert them into wishes when pulling on the current event wish banner.")
    print(" o Doing a pull gives you one guaranteed 4-star, that of either a weapon or character.")
    input(" o The 9 other wishes from one pull are random; usually a 3-star when you’re at low pity.\n\n")

    input("Paithon: The pity system is a system in which after doing over 7 pulls \n"
          "(70 wishes) your chances of obtaining a 5-star are increased!")
    print("This only heightens the 5-star character drop rate.\n")
    print("When a 5-star is available and a golden star is visible when wishing, \n"
          "you have a 50/50 chance of obtaining either Xiao (limited character) \n"
          "or a character from the permanent wish (standard 5-star characters).")
elif menuChoice == 3:
    print("╔╦╗╔═╗╦╔╗╔  ╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗╔═╗ O")
    time.sleep(1)
    print("║║║╠═╣║║║║  ╠═╝╠╦╝║ ║║ ╦╠╦╝╠═╣║║║║║║║╣ ╠╦╝╚═╗ ")
    time.sleep(1)
    print("╩ ╩╩ ╩╩╝╚╝  ╩  ╩╚═╚═╝╚═╝╩╚═╩ ╩╩ ╩╩ ╩╚═╝╩╚═╚═╝ O")
    print("\n")
    time.sleep(1)
    print("╔╦╗╔═╗╔╗╔╦╔═╗╔═╗  ╔═╗╔╗ ╔═╗╦  ╔═╗╔═╗   ")
    time.sleep(1)
    print("║║║║ ║║║║║║  ╠═╣  ╠═╣╠╩╗╠═╣║  ║ ║╚═╗      ")
    time.sleep(1)
    print("╩ ╩╚═╝╝╚╝╩╚═╝╩ ╩  ╩ ╩╚═╝╩ ╩╩═╝╚═╝╚═╝     ")
    print("\n")
    time.sleep(1)
    print("╦  ╦╔═╗╔╗╔╔╗╔╔═╗  ╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╔═╗  ")
    time.sleep(1)
    print("║  ║╠═╣║║║║║║║╣   ╠═╣║ ╦╠╦╝╠═╣║║║║ ║╚═╗   ")
    time.sleep(1)
    print("╩═╝╩╩ ╩╝╚╝╝╚╝╚═╝  ╩ ╩╚═╝╩╚═╩ ╩╩ ╩╚═╝╚═╝     ")
    print("\n")
    time.sleep(1)
    print(" ╦╔═╗╔═╗╦ ╦  ╔╗ ╔═╗╔═╗╦ ╦╦╔═╗    ")
    time.sleep(1)
    print(" ║╠═╣║  ╚╦╝  ╠╩╗╠═╣║ ╦║ ║║╚═╗    ")
    time.sleep(1)
    print("╚╝╩ ╩╚═╝ ╩   ╚═╝╩ ╩╚═╝╚═╝╩╚═╝    ")

else:
    print("Paithon: Leaving already?")
    print("Paithon: Alright, byebye (˶ᵔᗜᵔ˶)ﾉﾞ!!")