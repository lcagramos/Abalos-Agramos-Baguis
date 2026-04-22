# ----------Import libraries----------
import json
import time
import random

# ---------JSON file handling-----------
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
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def scrolling_credits():
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

def instructions():
    print("Instructions (enter to continue):\n"
          "")

    input(f"Paithon: Welcome {name}! In this game, you can obtain many \n"
          "characters and weapons, however, you must first earn a currency called \"Primogems\".\n")

    input("Paithon: To earn Primogems, you have to answer quiz bee questions\n"
          "related to Python coding concepts. There’s 3 difficulties: \n"
          "Easy (Formative Assessment), Medium (Alternative Assessment), \n"
          "and lastly, Hard (Summative Assessment).\n ")

    print("\nPaithon:")
    print(" o Easy gives 90 Primogems per question")
    print(" o Medium gives 140 Primogems per question")
    print(" o Hard gives 180 Primogems per question")
    input(" o Each level contains five items!\n ")

    print("Paithon: So, you might be asking, \"What do I do with all these primogems..?\" \n"
          "Well, first..!")
    print("\n o You can convert them into wishes when pulling on the current event wish banner.")
    print(" o Doing a pull gives you one guaranteed 4-star, that of either a weapon or character.")
    input(" o The 9 other wishes from one pull are random; usually a 3-star, as higher value items have lower drop rates!.\n ")

    print("When a 5-star is available and a golden star is visible when wishing, \n"
          "you have a 50/50 chance of obtaining either Xiao (limited character) \n"
          "or a character from the permanent wish (standard 5-star characters).")

name = ""
while name == "":
    name = input("Paithon: Welcome to Paithon's Gacha! What is your name, traveler? ").strip()
    if name == "": print("Please enter a name.")
print(f"Paithon: What a lovely name, {name}!")

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
            menuChoice = int(input("\nEnter menu choice (1-6): "))
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

        print("\nChoose a category (or 0 to quit):")
        print("0. Quit")
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

        print("You gaze upon the stars as you wish for a companion... ⋆˙⟡ ⋆.˚ ⊹₊⟡ ⋆")
        time.sleep(1)
        print("You see a shooting star.")

        print("Make a wish? (1600 primogems)")
        wChoice = input("(Yes/No): ").strip().lower()

        if wChoice == "yes":
            if data[0]["primogems"] >= 1600:
                 data[0]["primogems"] -= 1600

                 newItem = item[1]["4*"][random.randint(0,2)]

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
                 input(f"You find a formidable companion, a unique kind... it's {newItem}! ☆☆☆☆")
                 data[0]["inv"].append(newItem)

                 for i in range(9):
                     chance = random.randint(1, 100)


                     if 1 <= chance <= 50:
                         newItem = item[0]["3*"][random.randint(0,4)]
                         input(f"You find a weapon, a unique kind... it's the {newItem}! ☆☆☆")
                         data[0]["inv"].append(newItem)


                     elif 51 <= chance <= 65:
                         newItem = item[1]["4*"][random.randint(0,11)]

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

                         input(f"You wished, and you received {newItem}! ☆☆☆☆")
                         data[0]["inv"].append(newItem)


                     elif 66 <= chance <= 85:
                         newItem = item[1]["4*"][random.randint(0, 2)]

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

                         input(f"You find a new companion, it's {newItem}! ☆☆☆☆")
                         data[0]["inv"].append(newItem)

                     elif 86 <= chance <= 99:
                         fiftyF = random.randint(1,100)
                         print(f"You find a very special companion...!")

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

                         if 1 <= fiftyF <= 50:
                             newItem = item[2]["B5*"][0]

                             print("You meet the limited 5-star character..!")
                             time.sleep(0.3)
                             print("☆☆☆☆☆")
                             time.sleep(0.3)
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

                             data[0]["inv"].append(newItem)

                             time.sleep(0.5)
                             print(f"Paithon: Congratulations, {name}! You've reached the main goal of this game. \n"
                                   "Now, it's up to you. Would you like to continue playing?")
                             cont = input("Yes/No: ").strip().lower()
                             if cont == "yes":
                                  print("Paithon: Alrighty, have fun ! ✧｡٩(ˊᗜˋ )و✧*｡")
                             else:
                                  print(f"Paithon: Leaving,{name}?")
                                  print("Paithon: Alright, byebye!! (˶ᵔᗜᵔ˶)ﾉﾞ")
                                  exit()

                         else:
                              newItem = item[2]["OB5*"][random.randint(0,4)]
                              print("You find a 5-star from the permanent wish! A formidable companion indeed~")
                              print(f"You got...")
                              input(f"☆☆☆☆☆ {newItem}! ")
                     else:
                         print("You don't have enough primogems... (¬_¬＂)")

            elif wChoice == "no":
                print("You decide to save your wish for another day. ✧｡٩(ˊᗜˋ )و✧*｡")

    elif menuChoice == 3:
        print(f"You currently own {data[0]['primogems']} Primogems.")
        print("You currently own: ")
        owned = set(data[0]["inv"])
        for item in owned:
            print("-", item)
        input("\nPress enter to go back to the main menu! ")

    elif menuChoice == 4:
        instructions()
        input("\nPress enter to go back to the main menu! ")

    elif menuChoice == 5:
        scrolling_credits()
        input("\nPress enter to go back to the main menu! ")

    else:
        print(f"Paithon: Leaving alrady,{name}?")
        print("Paithon: Alright, byebye!! (˶ᵔᗜᵔ˶)ﾉﾞ")
        exit()