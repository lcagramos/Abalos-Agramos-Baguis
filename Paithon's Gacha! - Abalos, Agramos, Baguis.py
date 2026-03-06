import json
import time

with open("items.json", "r") as f:
    item = json.load(f)

with open("inventory.json", "r") as f:
    data = json.load(f)


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

    print("1. Easy (Formative Assessment)\n2. Medium (Alternative Assessment)\n3. Hard (Summative Assessment)")
    categoryChoice = ""
    while True:
        try:
            categoryChoice = int(input("Choose a category (1-3): "))
            if 1 <= categoryChoice <= 3:
                break
            else:
                print("Enter a number between 1 to 3.")
        except ValueError:
            print("Invalid input! Try again.")

    matchingQuestion = []
    for i in questions:
        if i["category"] == "easy":
            category = 1
            i["primogems"] == 60
        elif i["category"] == "medium":
            category = 2
            i["primogems"] == 110
        else:
            category = 3
            i["primogems"] == 150

        if not i["answered"] and i["category"] == category:
            matchingQuestion.append(i)

        if matchingQuestion:
            i["question_num"] = matchingQuestion[0]

        else:
            print("\nThat question was already answered, try again.")
            continue

    print("\n\n")
    print(matchingQuestion[0]["question"])
    print("\nChoices: ")
    print(matchingQuestion[0]["choices"])
    answer = input("\nEnter your answer: ")

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
    print("Leaving already?")
    print("Alright, byebye !!")