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

name = input("Welcome to Paithon's Gacha! What is your name, traveler? ")

while True:
    print("\n\n")
    print(" .-.---------------------------------.-.")
    print(" ((o))                                   )")
    print(" ( )_______          _____         ____/")
    print("  |             MAIN MENU            |")
    print("  |                                  |")
    print("  |  1. Start Game                   |")
    print("  |                                  |")
    print("  |  2. Go stargazing                |")
    print("  |                                  |")
    print("  |  3. View Inventory               |")
    print("  |                                  |")
    print("  |  4. How to Play                  |")
    print("  |                                  |")
    print("  |  5. Credits                      |")
    print("  |                                  |")
    print("  |  6. Quit                         |")
    print("  |                                  |")
    print("  |____    _______    __  ____    ___|")
    print(" / )                                  )")
    print("((o))                                  )")
    print(" '------------------------------------'")


    print("\n\n")
    menuChoice = ""
    while True:
        try:
            menuChoice = int(input("\nEnter choice (1-6): "))
            if 1 <= menuChoice <= 6:
                break
            else:
                print("Enter a number between 1 to 6.")
        except ValueError:
            print("Invalid input! Try again.")

    if menuChoice == 1:
        print(f"Paithon: Hello {name}! In this game, you must play Python-coding related minigames and answer questions"
            "\nto obtain a special currency called Primogems in order to wish on the current banner. You need 1,600 "
            "\nPrimogems to wish. Good luck!")

        while True:
            print("\nChoose an category (or 0 to quit):")
            print("1. Easy (Formative Assessment)")
            print("2. Medium (Alternative Assessment)")
            print("3. Hard (Summative Assessment)")

            categoryChoice = ""
            while True:
                try:
                    categoryChoice = int(input("\nChoose a category (0-3): "))
                    if 0 <= categoryChoice <= 3:
                        break
                    else:
                        print("Enter a number between 0 to 3.")
                except ValueError:
                    print("Invalid input! Try again.")

            if categoryChoice == 0:
                input("Press enter to go back to the main menu! ")
                break

            elif categoryChoice == 1:
                category = "Easy"
                reward = 60
            elif categoryChoice == 2:
                category = "Medium"
                reward = 110
            else:
                category = "Hard"
                reward = 150

            while True:
                matchingQuestion = [q for q in questions if not q["answered"] and q["category"] == category]

                if not matchingQuestion:
                    print(f"\nPaithon: All questions in {category} category have been answered! (˶ᵔ ᵕ ᵔ˶)")
                    break

                question = matchingQuestion[0]

                if isinstance(question["text"], list):
                    text = "\n".join(question["text"])
                else:
                    text = question["text"]

                print()
                print(text)
                print("\n" + "\n".join(question["choices"]))
                answer = input("\nEnter your answer: ")

                if answer.upper() == question["answer"]:
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
        print("You gaze upon the stars as you wish for a companion... ⋆˙⟡ ⋆.˚ ⊹₊⟡ ⋆")
        time.sleep(1.5)
        print("\nYou see a shooting star.")

        print("Make a wish? (1600 Primogems)")
        wChoice = ""
        while True:
            wChoice = input("\n(Yes/No): ").strip().lower()
            validWChoice = ["yes", "no"]
            if wChoice in validWChoice:
                break
            else:
                print("Enter (Yes/No):  ")

        if wChoice == "yes":
            if data[0]["primogems"] >= 1600:
                data[0]["primogems"] -= 1600

                for i in range(10):
                    newItem = ""
                    chance = random.randint(1, 100)
                    if chance in range(1, 50):
                        newItem = item[0]["3*"][random.randint(0, 4)]
                        input(f"You find a weapon, a unique kind... it's the {newItem}! ☆☆☆ ")
                        data[0]["inv"].append(newItem)

                    elif chance in range(51, 65):
                        newItem = item[1]["OB4*"][random.randint(0, 11)]
                        print("""   
                ⠀   ⠀⢀⠀⠀⠀⠀⠀⠀ ⠀   ⣀⣀⡠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⢸⢉⡗⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠈⡱⠖⠀⠀⠀⠀⠀ ⠀⠀⠀ ⣄⣠⠆⠀
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
                    ⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⣸⠤⡐⠁⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀\n""")
                        time.sleep(2)

                        input(f"You wished, and you received {newItem}! ☆☆☆☆ ")
                        data[0]["inv"].append(newItem)

                    elif chance in range(66, 85):
                        newItem = item[1]["B4*"][random.randint(0, 2)]

                        input(f"You find a new companion, it's {newItem}! ☆☆☆☆ ")
                        data[0]["inv"].append(newItem)

                    elif chance in range(86, 99):
                        fiftyF = random.randint(1, 100)
                        input(f"You find a very special companion...! ")

                        if fiftyF in range(1, 50):
                            newItem = item[2]["B5*"][0]

                            print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
                            input("You meet the limited 5-star character, Adeptus Xiao! ☆☆☆☆☆ ")
                            time.sleep(1)
                            print(r"""
                            ⠀⠀               ⠀⠀⢀⠀⠉⠀⠀⣀⣤⠖⠀⠀⠀⠀⠐⠢⠄⠒⠢⠀⠀⠉⠁⢲⣶⣶⣶⣶⣶⣦⣠⡿⠟⠉⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠋⠀⠀⣰⣿⠿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡿⠛⠛⠻⣿⣿⣿⣿⣿⣿⡟⠛⠛⠒⢦⣤⣀⡀⠞⠉⠉⠓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⣀⣄⣀⠀⣼⠋⠀⠀⠈⢻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠻⡆⠀⠀⠀⠈⣿⣿⣿⣿⣟⡀⠀⠀⠀⠀⠟⠛⠻⡆⠀⠀⠀⠀⠹⠟⢲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠄⠁⠀⠉⣿⣿⣠⡆⠀⠀⠀⢿⣷⡀⠀⠀⠀⠀⢠⣞⠃⢠⠟⠁⠀⠀⢹⣰⢄⣀⡰⠋⠉⠉⠀⠈⠙⠲⣀⠀⠠⠄⠀⠀⢹⡶⠦⣤⡖⠦⠄⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⣴⡿⠛⣿⡇⠀⠀⠀⠘⣿⣧⣤⣤⣦⣴⠟⠉⠛⠋⠀⠀⠀⢀⡼⢣⣌⣹⠃⠀⠀⠀⠀⢰⠀⠀⠈⠳⡂⠀⠀⠰⣾⠁⠀⠀⠻⣦⣤⣀⡀⢱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⢀⣼⣿⡶⣰⣿⣿⡀⠀⠀⠀⣼⣇⣴⣿⡟⢁⣤⣤⣤⣴⣷⣀⣒⣋⡸⠋⠈⠙⠦⣄⠀⠀⣠⣧⡴⠋⠀⠀⠘⣦⠀⠀⢸⣧⣀⠀⠀⠘⡆⠀⠉⠛⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⢀⠻⠏⢻⣿⣿⣿⣿⣧⠀⢀⢸⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠈⠁⠀⠈⣻⣆⠀⠀⠀⠀⣿⡿⠋⠁⠈⠛⠲⢤⣄⣸⣤⣤⣼⡿⢩⣿⠗⠒⠻⣄⠀⠀⡸⣧⠙⢷⡀⠀⠀⠀⠀⠀
                                        ⠀⢀⣥⣦⣘⣿⣿⣿⣿⣿⣀⣾⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠿⢿⣦⡀⣠⣾⣿⣷⡄⠀⠀⠀⠀⠀⠈⠉⠻⢿⣍⠀⠸⠃⠀⠀⠀⠈⠓⠂⠃⢹⠀⡜⠳⠀⠀⠀⠀⠀
                                        ⠀⠀⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠇⠀⠈⣿⣯⣿⣿⠟⠉⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢸⡇⠀⠀⠀⠀⠀⠀
                                        ⣄⠀⠀⢸⣿⣿⣿⣿⣿⣿⡛⠉⠛⢷⠀⠀⠀⠀⠀⢀⡄⠀⠀⡤⢠⠟⠀⠀⠀⠸⣿⡿⠁⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣤⣤⣄⣀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀
                                        ⣿⣇⣤⠞⠉⠛⠛⠛⠛⢛⣷⣄⣠⠿⠀⠀⠀⠀⢀⡼⠃⠀⣸⠃⣸⠀⠀⠀⠶⠤⠿⠁⠀⠠⢀⣀⡇⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣈⠙⠻⣦⡀⠀⢸⣦⡀⠀⠀⠀⠀⠀
                                        ⣿⠟⠁⠀⠀⠀⠀⠀⢀⣾⢿⣿⠁⠀⠀⠀⠀⢠⣾⡇⠀⢠⡿⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠘⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡉⠛⠿⠶⣬⣿⣦⣼⠅⠛⠶⠄⠀⠀⠀
                                        ⠃⠀⠀⠀⠀⠀⠀⢀⣼⠏⣾⡇⠀⠀⠀⠀⣠⣾⡿⠀⢀⣿⠃⣿⣿⠀⠀⠀⠀⢀⣾⠀⠀⠀⠀⠀⢹⡇⢸⣧⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⣤⣄⣉⣉⡤⠀⣠⠆⠀⠀⠉⠁
                                        ⠀⠀⠀⣤⣀⣀⣤⠞⠁⢰⣿⠀⠀⠀⠀⣠⣟⣿⠃⢀⣾⠏⠀⢸⣿⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢸⡇⠀⢻⣧⠘⣿⣆⠀⠀⠄⠀⠀⠀⠀⠀⠙⠛⢶⣥⣄⢀⣴⣿⣤⡤⠔⠚⠁
                                        ⠀⠀⠀⠙⢿⣯⣥⣤⣤⣾⡇⠀⠀⠀⠠⣿⡿⠃⢠⣾⣏⣀⣀⠈⣿⡆⣀⡀⠀⠈⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⢿⣧⣸⣝⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⠿⠤⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀⠀⣀⣾⠟⠁⣰⣿⣁⡉⠉⢉⠉⢿⣿⠋⠁⠀⠀⠀⠀⠈⠳⠶⠶⣿⡷⠖⠒⠚⢻⣿⣿⡎⠻⢶⣄⡀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⣰⣿⣯⣴⣾⡿⠿⢿⣿⣶⣦⣀⡈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⣀⣀⣿⣿⣿⣦⣄⡉⢻⣿⢿⣷⣦⣀⡤⡤⣄⣀⡀⠀⠙⣦⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣧⣼⠟⠀⣩⣿⣯⡀⠀⢸⡏⣂⣿⣟⣻⡿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣼⣣⣼⡿⢻⣯⡛⠻⣿⣿⣿⣿⣿⣿⣿⣦⣄⠅⠹⣿⣿⣿⣿⣿⣿⡙⢻⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠾⣿⣼⣿⡿⠏⢀⣠⣾⣿⢿⣏⠃⣀⢘⣿⣮⣻⣯⣿⣇⠈⠙⢦⡀⠀⠀⠀⠀⡼⠋⠀⢸⣿⣿⠿⣥⡼⠟⠈⢻⣿⣿⣼⣿⠋⠙⠳⣦⣈⡻⠿⣿⣿⣿⡿⣮⣄⡀⠀
                                        ⠀⠀⠐⠦⠤⠤⠤⠿⣿⣶⣾⣿⠿⠉⠀⢸⣿⡆⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠚⠁⠀⠀⠈⠉⠉⠉⠉⠰⠶⠒⠛⠛⢿⣿⣿⡀⠀⠀⣿⣿⣿⣷⣶⣿⠿⠁⢈⣉⣿⡶
                                        ⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⡀⡇⠀⠈⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⢿⣷⣦⣠⣿⣿⣿⡟⠛⠿⠶⠶⠛⢋⡥⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠛⠋⣿⣿⣿⣽⣿⠀⠀⢹⣯⠛⠳⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠈⣹⣿⣿⣯⣟⡳⠤⠔⣒⣾⠾⠋⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢻⣿⣿⣿⣦⣀⠀⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣎⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⡉⠉⠉⠁⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣯⡾⢿⡇⠻⣿⣿⣷⣼⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⠀⠈⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⣠⡾⡟⢸⣿⣿⡿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣋⡁⠀⠀⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣧⠀⢘⣻⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣯⣾⣇⣤⢻⣾⠄⠹⣧⠈⢿⣿⣿⣿⣿⣿⣿⣟⠛⠛⠛⠉
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⢀⣿⣯⠻⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠛⡿⣿⣿⡇⠙⠿⣆⣹⣧⠀⢹⣇⠀⠹⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣇⠹⣿⣿⣿⣿⣿⣏⠳⣄⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠁⠀⣼⠃⣿⡿⠀⠀⠀⠈⠉⢻⡆⠀⣿⢷⣤⡸⣿⡹⣿⣿⣿⣿⣿⣆⠀
                                        ⠀⠀⠀⠒⠒⠦⢤⣤⣀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣷⡸⣿⣿⣿⣿⣿⣦⡈⠳⢦⣤⣤⣤⠾⠛⠉⠀⠀⣠⣼⣿⠴⠋⠀⠀⠀⠀⠀⠀⠈⣿⠀⢻⠀⠈⠻⣾⣧⠈⢿⣿⣿⣿⣿⣧
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢳⠲⣤⣤⣤⣄⣀⣹⣿⣿⣷⣌⢿⣿⣟⣿⣿⣿⣷⣦⣄⠁⠀⠀⠀⠀⠀⣴⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⢸⠀⠀⠀⠈⢻⣧⠀⢻⣿⣿⣿⣿
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⣿⣿⣟⡿⣿⣿⣿⣎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⢸⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣾⠀⠀⠀⠀⠀⠙⣿⣄⢿⣿⡟⣿
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣧⠙⣿⣿⣿⣷⣻⣿⡟⢿⣿⣿⣿⣿⣿⣷⠀⢠⣿⣿⣿⣿⡟⢦⡀⠀⢀⣀⣀⠀⠀⠀⢀⣿⡏⠀⠀⠀⠀⠀⠀⢹⣿⣮⠹⠇⢻
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⣿⡀⠛⣿⣿⣿⣿⣆⢻⣿⣿⣿⣿⣿⣆⣾⣿⣿⣿⣿⣿⡄⢻⣶⣧⡀⢹⣷⣄⣀⣾⠛⠀⠀⠀⠀⠀⠀⣠⠾⠛⣿⣆⠁⢸
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡟⠛⠻⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⢸⣿⣿⣿⡀⠀⢸⡟⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⣿⣿⠀⠸
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠉⠻⣦⣀⣠⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣿⣿⣿⣿⣿⣷⠶⠞⢷⣶⣄⡀⠀⢀⣰⠏⠀⠀⠀⠀⡟⡏⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⢸⡏⠀⠀⢹⣿⣷⣬⣿⣿⠻⢿⣿⣿⣿⣿⣿⠏⣾⣿⣿⣿⣿⣿⣿⣄⠀⢀⣿⣿⣿⣷⣮⣅⡀⠀⠀⠀⣼⣽⠖⠀⠀
                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠠⣌⢷⣤⠔⠚⢿⣿⣿⣿⡟⠀⠀⠙⢿⣿⣿⣟⣼⣿⣿⠻⣿⣿⣿⡏⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣷⢦⣾⣿⣀⡀⠀⠀
                                        ⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠘⣯⡀⠀⢠⣿⡋⢹⣷⡀⠀⠀⢸⠟⡇⠁⣿⣿⣿⠀⠀⠈⣻⠧⣄⣰⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⠀⠀
                                        ⠉⢳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⢀⣽⣿⣿⠋⠀⠹⣾⣿⡿⢦⠀⢸⠀⡇⠀⣿⢿⣿⣧⠀⠀⡇⠀⠀⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠉⠉⠻⣄⠀
                                        ⠀⠀⢻⡟⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⢀⣴⣿⡿⠋⠘⢦⣤⠾⠛⣯⠀⠈⠳⣞⠀⣿⡼⠃⠀⠈⠛⢦⡤⠗⠢⣾⡏⠀⠈⠻⣿⣿⣿⣿⣿⣿⣀⡀⣀⠀⠀⢹⠀
                                        ⠀⠀⠀⣧⢻⡘⣄⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⣼⣿⡿⣻⠟⠁⠀⠀⠀⠀⢣⣄⠀⣸⣭⣄⠀⠈⠛⣿⢧⡀⠀⠀⢀⣨⣇⡀⢠⡟⠀⠀⠀⠀⣾⠻⣿⣿⣿⣿⣿⣿⡏⠀⠀⢸⣿
                                        ⠀⠀⠀⠹⣜⣧⠀⠳⣄⠀⠀⠰⡀⠀⠀⠀⠀⢰⣿⡏⡼⠋⠀⠀⠀⠀⠀⠀⠀⠙⣿⠁⠀⠈⢳⣄⡞⠃⠀⠹⣄⣼⠋⠀⠈⣿⡿⠀⠀⠀⠀⠀⠙⠳⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⡿
                                        ⠀⠀⠀⠀⢿⣿⡀⠀⠈⠳⣄⠀⢷⠀⠀⠀⢠⣿⣿⣿⣿⢞⡿⠀⠀⠀⠀⠀⠀⠀⢻⣀⣴⣶⣾⣏⡷⠻⣆⣰⣿⣿⣤⣴⣾⣿⡃⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⠀⠀⠀⢀⣁
                                        ⠀⠀⠀⠀⠈⣿⣧⠀⠀⠀⠈⢣⡈⣦⠀⢠⣿⣿⣿⣿⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⢰⣛⣿⣟⢿⡞⣇⢀⣾⣿⠉⢻⣿⣿⣻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡟⠀⠀⠀⢸⣿
                                        ⠀⠀⠀⠀⠀⠹⣿⡇⠀⠀⠀⠀⠉⠹⣤⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡿⠀⠙⢿⣿⣿⣿⣿⠟⠀⠛⡿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⢸⣿
                                        ⠀⠀⠀⠀⠀⠀⢻⣿⣄⠀⠀⡀⣀⣴⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠩⣿⡀⠀⢀⡼⠛⢹⣿⡅⠀⠀⠀⣧⣻⢵⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⢻""")
                            data[0]["inv"].append(newItem)

                        else:
                            print("""
                            ⠀⠀⢀⠀⠀⠀⠀ ⠀    ⣀⣀⡠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⢸⢉⡗⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠈⡱⠖⠀⠀⠀⠀⠀  ⠀⠀⠀⣄⣠⠆⠀
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
                            ⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⣸⠤⡐⠁⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀\n""")
                            newItem = item[2]["OB5*"][random.randint(0, 4)]
                            input(f"You find a new companion, it's {newItem}! ☆☆☆☆☆ ")
                            data[0]["inv"].append(newItem)

                with open("data.json", "w") as f:
                    json.dump(questions, f, indent=4)
                input("\nPress enter to return to main menu! ")

            else:
                print("You don't have enough Primogems... (¬_¬＂)")
                input("Press enter to go back to the main menu! ")

        elif wChoice == "no":
            print("You decide to save your wish for another day. ✧｡٩(ˊᗜˋ )و✧*｡")
            input("Press enter to go back to the main menu! ")

    elif menuChoice == 3:
        print(f"You currently own {data[0]["primogems"]} Primogems.")
        print("You currently own: ")
        owned = set(data[0]["inv"])
        for item in owned:
            print("-", item)
        input("\nPress enter to go back to the main menu! ")

    elif menuChoice == 4:
        print("Instructions (enter to continue):\n"
              "")

        input("Paithon: Welcome player! In this game, you can obtain many \n"
              "characters and weapons, however, you must first earn a currency called \"Primogems\".\n")

        input("Paithon: To earn Primogems, you have to answer quiz bee questions\n"
              "related to Python coding concepts. There’s 3 difficulties: \n"
              "Easy (Formative Assessment), Medium (Alternative Assessment), \n"
              "and lastly, Hard (Summative Assessment).\n ")

        print("Paithon:")
        print(" o Easy gives 60 Primogems per question")
        print(" o Medium gives 110 Primogems per question")
        print(" o Hard gives 150 Primogems per question")
        input(" o Each level contains five items!\n ")

        print("Paithon: So, you might be asking, \"What do I do with all these primogems..?\" \n"
              "Well, first..!")
        print(" o You can convert them into wishes when pulling on the current event wish banner.")
        print(" o Doing a pull gives you one guaranteed 4-star, that of either a weapon or character.")
        input(" o The 9 other wishes from one pull are random; usually a 3-star when you’re at low pity.\n ")

        input("Paithon: The pity system is a system in which after doing over 7 pulls \n"
              "(70 wishes) your chances of obtaining a 5-star are increased! ")
        print("This only heightens the 5-star character drop rate.\n")
        print("When a 5-star is available and a golden star is visible when wishing, \n"
              "you have a 50/50 chance of obtaining either Xiao (limited character) \n"
              "or a character from the permanent wish (standard 5-star characters).")

        input("\nPress enter to go back to the main menu! ")

    elif menuChoice == 5:
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

        input("\nPress enter to go back to the main menu! ")

    else:
        print(f"Paithon: Leaving already,{name}?")
        print("Paithon: Alright, byebye (˶ᵔᗜᵔ˶)ﾉﾞ!!")
        break