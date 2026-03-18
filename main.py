import json
import time
import random

with open("items.json", "r") as f:
    item = json.load(f)

with open("inventory.json", "r") as f:
    inventory = json.load(f)

with open("quizbee.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

for question in questions:
    question["answered"] = False

with open("quizbee.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=4)

def get_menu_choice():
    while True:
        try:
            menu_choice = int(input("\nEnter choice (1-4): "))
            if 1 <= menu_choice <= 4:
                return menu_choice
            else:
                print("Enter a number between 1 to 4.")
        except ValueError:
            print("Invalid input! Try again.")

def get_category_choice():
    while True:
        try:
            category_choice = int(input("\nChoose a category (1-3): "))
            if 1 <= category_choice <= 3:
                return category_choice
            else:
                print("Enter a number between 1 to 3.")
        except ValueError:
            print("Invalid input! Try again.")

name = input("Welcome to Paithon's Gacha! What is your name, traveler? ")
print(f"Greetings {name}, welcome to Paithon's Gacha!")

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
menuChoice = get_menu_choice()

if menuChoice == 1:
    input("Paithon: Hello player! In this game, you must play Python-coding related minigames and answer questions"
        "\nto obtain a special currency called Primogems in order to wish on the current banner. You need 1,600 "
        "\nPrimogems to wish. Good luck! (Press Enter to continue) ")

    while True:
        print("\n1. Easy (Formative Assessment)\n2. Medium (Alternative Assessment)\n3. Hard (Summative Assessment)")

        categoryChoice = get_category_choice()

        category = ""
        if categoryChoice == 1:
            category = "Easy"
        elif categoryChoice == 2:
            category = "Medium"
        else: category = "Hard"

        matchingQuestions = []

        for question in questions:
            if category == question["category"] and not question["answered"]:
                matchingQuestions.append(question)

        if not matchingQuestions:
            print("\nYou've answered everything in this category! Choose another category.")
            continue

        random.shuffle(matchingQuestions)
        for question in matchingQuestions:
            print()
            for i in (question["text"]):
                print(i)
            print()
            for i in (question["choices"]):
                print(i)
            answer = input("\nEnter your answer: ")
            input(f"The correct answer is {question['answer']} (Press Enter to continue) ")

            if answer == question['answer'] and category == "Easy":
                inventory[0]['primogems'] += 60
            elif answer == question['answer'] and category == "Medium":
                inventory[0]['primogems'] += 110
            elif answer == question['answer'] and category == "Hard":
                inventory[0]['primogems'] += 160
            else:
                print("67")

            with open("inventory.json", "w", encoding="utf-8") as f:
                json.dump(inventory, f, indent=4)

            question["answered"] = True
            with open("quizbee.json", "w", encoding="utf-8") as f:
                json.dump(questions, f, indent=4)

elif menuChoice == 2:
    input("If a statement hasn't printed, press enter to continue.")
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
    print(" o Hard gives 160 Primogems per question")
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
    print("Leaving already?")
    print("Alright, byebye !!")
