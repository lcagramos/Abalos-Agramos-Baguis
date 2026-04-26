# ----------Import libraries----------
import json
import time
import random

# ---------JSON file handling---------
with open("items.json", "r") as f:
    item = json.load(f)

with open("inventory.json", "r") as f:
    data = json.load(f)

with open("quizbee.json", "r") as f:
    questions = json.load(f)

for question in questions:
    question["answered"] = False
    with open("quizbee.json", "w") as f:
        # noinspection PyTypeChecker
        json.dump(questions, f, indent=4)

# ----------Initialization-----------
newItem = ""
categoryChoice = ""
menuChoice = ""

BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[32m"
RESET = "\033[0m"

# --------Defining Functions---------
def save_data():
    with open("inventory.json", "w") as F:
        # noinspection PyTypeChecker
        json.dump(data, F, indent=4)
def main_menu():
    print(YELLOW + r"""                                                          .-'''-.                                                              _..._                             ___   
                                                             '   _    \                                                         .-'_..._''.                       .'/   \  
    _________   _...._              .--.           .       /   /` '.   \    _..._    ,.--.                                    .' .'      '.\  .                  / /     \ 
    \        |.'      '-.           |__|         .'|      .   |     \  '  .'     '. //    \                .--./)            / .'           .'|                  | |     | 
     \        .'```'.    '.         .--.     .| <  |      |   '      |  '.   .-.   .\\    |               /.''\\            . '            <  |                  | |     | 
      \      |       \     \   __   |  |   .' |_ | |      \    \     / / |  '   '  | `'-)/               | |  | |      __   | |             | |             __   |/`.   .' 
       |     |        |    |.:--.'. |  | .'     || | .'''-.`.   ` ..' /  |  |   |  |   /'  _              \`-' /    .:--.'. | |             | | .'''-.   .:--.'.  `.|   |  
       |      \      /    ./ |   \ ||  |'--.  .-'| |/.'''. \  '-...-'`   |  |   |  |     .' |             /("'`    / |   \ |. '             | |/.'''. \ / |   \ |  ||___|  
       |     |\`'-.-'   .' `" __ | ||  |   |  |  |  /    | |             |  |   |  |    .   | /           \ '---.  `" __ | | \ '.          .|  /    | | `" __ | |  |/___/  
       |     | '-....-'`    .'.''| ||__|   |  |  | |     | |             |  |   |  |  .'.'| |//            /'""'.\  .'.''| |  '. `._____.-'/| |     | |  .'.''| |  .'.--.  
      .'     '.            / /   | |_      |  '.'| |     | |             |  |   |  |.'.'.-'  /            ||     ||/ /   | |_   `-.______ / | |     | | / /   | |_| |    | 
    '-----------'          \ \._,\ '/      |   / | '.    | '.            |  |   |  |.'   \_.'             \'. __// \ \._,\ '/            `  | '.    | '.\ \._,\ '/\_\    / 
                            `--'  `"       `'-'  '---'   '---'           '--'   '--'                       `'---'   `--'  `"                '---'   '---'`--'  `"  `''--'  """ + RESET)
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
   print("Instructions (press enter to continue):\n"
         "")


   input(f"Paithon: Welcome {name}! In this game, you can obtain many \n"
         "characters and weapons, however, you must first earn a currency called \033[95m\"Primogems\"\033[0m.\n")


   input("Paithon: To earn Primogems, you have to answer quiz bee questions\n"
         "related to Python coding concepts. There’s 3 difficulties: \n"
         "\033[92mEasy (Formative Assessment)\033[0m, \033[93mMedium (Alternative Assessment)\033[0m, \n"
         "and lastly, \033[91mHard (Summative Assessment)\033[0m.\n ")


   print("\nPaithon:")
   print(" o \033[92mEasy\033[0m gives \033[95m\"90 Primogems\"\033[0m per question")
   print(" o \033[93mMedium\033[0m gives \033[95m\" 140 Primogems\"\033[0m per question")
   print(" o \033[91mHard\033[0m gives \033[95m\"180 Primogems\"\033[0m per question")
   input(" o Each level contains \033[4mfive items\033[0m!\n ")


   print("Paithon: So, you might be asking, \"What do I do with all these Primogems..?\" \n"
         "Well, first..!")
   print("\n o You can \033[4mconvert them into wishes\033[0m when pulling on the current event wish banner.")
   print(" o Doing a pull gives you one guaranteed 4-star, that of either a weapon or character.")
   input(" o The 9 other wishes from one pull are random; usually a 3-star, as higher value items have lower drop rates!\n ")


   print("When a 5-star is available and a golden star is visible when wishing, \n"
         "you have a 50/50 chance of obtaining either \033[96mXiao (limited character)\033[0m \n"
         "or a character from the permanent wish (standard 5-star characters).")

#----------------------------------ASCII ARTS-------------------------------------
def xiao_ascii():
    print( GREEN + r"⠀⠀⠀            ⠀⢀⠀⠉⠀⠀⣀⣤⠖⠀⠀⠀⠀⠐⠢⠄⠒⠢⠀⠀⠉⠁⢲⣶⣶⣶⣶⣶⣦⣠⡿⠟⠉⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"                ⠋    ⣰⣿⠿⣶⣤           ⠘⣿⡿⠛⠛⠻⣿⣿⣿⣿⣿⣿⡟⠛⠛⠒⢦⣤⣀⡀⠞⠉⠉⠓⢦⡀               " + RESET)
    time.sleep(0.5)
    print(GREEN + r"               ⣀⣄⣀⠀⣼⠋⠀⠀⠈⢻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠻⡆⠀⠀⠀⠈⣿⣿⣿⣿⣟⡀⠀⠀⠀⠀⠟⠛⠻⡆⠀⠀⠀⠀⠹⠟⢲          " + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠄⠁⠀⠉⣿⣿⣠⡆⠀⠀⠀⢿⣷⡀⠀⠀⠀⠀⢠⣞⠃⢠⠟⠁⠀⠀⢹⣰⢄⣀⡰⠋⠉⠉⠀⠈⠙⠲⣀⠀⠠⠄⠀⠀⢹⡶⠦⣤⡖⠦⠄⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⣴⡿⠛⣿⡇⠀⠀⠀⠘⣿⣧⣤⣤⣦⣴⠟⠉⠛⠋⠀⠀⠀⢀⡼⢣⣌⣹⠃⠀⠀⠀⠀⢰⠀⠀⠈⠳⡂⠀⠀⠰⣾⠁⠀⠀⠻⣦⣤⣀⡀⢱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⢀⣼⣿⡶⣰⣿⣿⡀⠀⠀⠀⣼⣇⣴⣿⡟⢁⣤⣤⣤⣴⣷⣀⣒⣋⡸⠋⠈⠙⠦⣄⠀⠀⣠⣧⡴⠋⠀⠀⠘⣦⠀⠀⢸⣧⣀⠀⠀⠘⡆⠀⠉⠛⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN+ r"            ⠀⢀⠻⠏⢻⣿⣿⣿⣿⣧⠀⢀⢸⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠈⠁⠀⠈⣻⣆⠀⠀⠀⠀⣿⡿⠋⠁⠈⠛⠲⢤⣄⣸⣤⣤⣼⡿⢩⣿⠗⠒⠻⣄⠀⠀⡸⣧⠙⢷⡀⠀⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⢀⣥⣦⣘⣿⣿⣿⣿⣿⣀⣾⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠿⢿⣦⡀⣠⣾⣿⣷⡄⠀⠀⠀⠀⠀⠈⠉⠻⢿⣍⠀⠸⠃⠀⠀⠀⠈⠓⠂⠃⢹⠀⡜⠳⠀⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠇⠀⠈⣿⣯⣿⣿⠟⠉⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢸⡇⠀⠀⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⣄⠀⠀⢸⣿⣿⣿⣿⣿⣿⡛⠉⠛⢷⠀⠀⠀⠀⠀⢀⡄⠀⠀⡤⢠⠟⠀⠀⠀⠸⣿⡿⠁⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣤⣤⣄⣀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⣿⣇⣤⠞⠉⠛⠛⠛⠛⢛⣷⣄⣠⠿⠀⠀⠀⠀⢀⡼⠃⠀⣸⠃⣸⠀⠀⠀⠶⠤⠿⠁⠀⠠⢀⣀⡇⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣈⠙⠻⣦⡀⠀⢸⣦⡀⠀⠀⠀⠀⠀"+ RESET)
    time.sleep(0.5)
    print(GREEN +r"            ⣿⠟⠁⠀⠀⠀⠀⠀⢀⣾⢿⣿⠁⠀⠀⠀⠀⢠⣾⡇⠀⢠⡿⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠘⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡉⠛⠿⠶⣬⣿⣦⣼⠅⠛⠶⠄⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠃⠀⠀⠀⠀⠀⠀⢀⣼⠏⣾⡇⠀⠀⠀⠀⣠⣾⡿⠀⢀⣿⠃⣿⣿⠀⠀⠀⠀⢀⣾⠀⠀⠀⠀⠀⢹⡇⢸⣧⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⣤⣄⣉⣉⡤⠀⣠⠆⠀⠀⠉⠁" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⣤⣀⣀⣤⠞⠁⢰⣿⠀⠀⠀⠀⣠⣟⣿⠃⢀⣾⠏⠀⢸⣿⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢸⡇⠀⢻⣧⠘⣿⣆⠀⠀⠄⠀⠀⠀⠀⠀⠙⠛⢶⣥⣄⢀⣴⣿⣤⡤⠔⠚⠁" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠙⢿⣯⣥⣤⣤⣾⡇⠀⠀⠀⠠⣿⡿⠃⢠⣾⣏⣀⣀⠈⣿⡆⣀⡀⠀⠈⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⢿⣧⣸⣝⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⠿⠤⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀⠀⣀⣾⠟⠁⣰⣿⣁⡉⠉⢉⠉⢿⣿⠋⠁⠀⠀⠀⠀⠈⠳⠶⠶⣿⡷⠖⠒⠚⢻⣿⣿⡎⠻⢶⣄⡀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⣰⣿⣯⣴⣾⡿⠿⢿⣿⣶⣦⣀⡈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⣀⣀⣿⣿⣿⣦⣄⡉⢻⣿⢿⣷⣦⣀⡤⡤⣄⣀⡀⠀⠙⣦⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣧⣼⠟⠀⣩⣿⣯⡀⠀⢸⡏⣂⣿⣟⣻⡿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣼⣣⣼⡿⢻⣯⡛⠻⣿⣿⣿⣿⣿⣿⣿⣦⣄⠅⠹⣿⣿⣿⣿⣿⣿⡙⢻⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠾⣿⣼⣿⡿⠏⢀⣠⣾⣿⢿⣏⠃⣀⢘⣿⣮⣻⣯⣿⣇⠈⠙⢦⡀⠀⠀⠀⠀⡼⠋⠀⢸⣿⣿⠿⣥⡼⠟⠈⢻⣿⣿⣼⣿⠋⠙⠳⣦⣈⡻⠿⣿⣿⣿⡿⣮⣄⡀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠐⠦⠤⠤⠤⠿⣿⣶⣾⣿⠿⠉⠀⢸⣿⡆⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠚⠁⠀⠀⠈⠉⠉⠉⠉⠰⠶⠒⠛⠛⢿⣿⣿⡀⠀⠀⣿⣿⣿⣷⣶⣿⠿⠁⢈⣉⣿⡶" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⡀⡇⠀⠈⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⢿⣷⣦⣠⣿⣿⣿⡟⠛⠿⠶⠶⠛⢋⡥⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠛⠋⣿⣿⣿⣽⣿⠀⠀⢹⣯⠛⠳⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠈⣹⣿⣿⣯⣟⡳⠤⠔⣒⣾⠾⠋⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢻⣿⣿⣿⣦⣀⠀⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣎⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⡉⠉⠉⠁⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣯⡾⢿⡇⠻⣿⣿⣷⣼⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⠀⠈⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⣠⡾⡟⢸⣿⣿⡿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣋⡁⠀⠀⠀⠀" + RESET)
    time.sleep(0.5)
    print( GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣧⠀⢘⣻⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣯⣾⣇⣤⢻⣾⠄⠹⣧⠈⢿⣿⣿⣿⣿⣿⣿⣟⠛⠛⠛⠉" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⢀⣿⣯⠻⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠛⡿⣿⣿⡇⠙⠿⣆⣹⣧⠀⢹⣇⠀⠹⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣇⠹⣿⣿⣿⣿⣿⣏⠳⣄⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠁⠀⣼⠃⣿⡿⠀⠀⠀⠈⠉⢻⡆⠀⣿⢷⣤⡸⣿⡹⣿⣿⣿⣿⣿⣆⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠒⠒⠦⢤⣤⣀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣷⡸⣿⣿⣿⣿⣿⣦⡈⠳⢦⣤⣤⣤⠾⠛⠉⠀⠀⣠⣼⣿⠴⠋⠀⠀⠀⠀⠀⠀⠈⣿⠀⢻⠀⠈⠻⣾⣧⠈⢿⣿⣿⣿⣿⣧" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢳⠲⣤⣤⣤⣄⣀⣹⣿⣿⣷⣌⢿⣿⣟⣿⣿⣿⣷⣦⣄⠁⠀⠀⠀⠀⠀⣴⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⢸⠀⠀⠀⠈⢻⣧⠀⢻⣿⣿⣿⣿" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⣿⣿⣟⡿⣿⣿⣿⣎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⢸⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣾⠀⠀⠀⠀⠀⠙⣿⣄⢿⣿⡟⣿" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣧⠙⣿⣿⣿⣷⣻⣿⡟⢿⣿⣿⣿⣿⣿⣷⠀⢠⣿⣿⣿⣿⡟⢦⡀⠀⢀⣀⣀⠀⠀⠀⢀⣿⡏⠀⠀⠀⠀⠀⠀⢹⣿⣮⠹⠇⢻" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⣿⡀⠛⣿⣿⣿⣿⣆⢻⣿⣿⣿⣿⣿⣆⣾⣿⣿⣿⣿⣿⡄⢻⣶⣧⡀⢹⣷⣄⣀⣾⠛⠀⠀⠀⠀⠀⠀⣠⠾⠛⣿⣆⠁⢸" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡟⠛⠻⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⢸⣿⣿⣿⡀⠀⢸⡟⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⣿⣿⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠉⠻⣦⣀⣠⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣿⣿⣿⣿⣿⣷⠶⠞⢷⣶⣄⡀⠀⢀⣰⠏⠀⠀⠀⠀⡟⡏⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⢸⡏⠀⠀⢹⣿⣷⣬⣿⣿⠻⢿⣿⣿⣿⣿⣿⠏⣾⣿⣿⣿⣿⣿⣿⣄⠀⢀⣿⣿⣿⣷⣮⣅⡀⠀⠀⠀⣼⣽⠖⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠠⣌⢷⣤⠔⠚⢿⣿⣿⣿⡟⠀⠀⠙⢿⣿⣿⣟⣼⣿⣿⠻⣿⣿⣿⡏⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣷⢦⣾⣿⣀⡀⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠘⣯⡀⠀⢠⣿⡋⢹⣷⡀⠀⠀⢸⠟⡇⠁⣿⣿⣿⠀⠀⠈⣻⠧⣄⣰⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⠀⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠉⢳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⢀⣽⣿⣿⠋⠀⠹⣾⣿⡿⢦⠀⢸⠀⡇⠀⣿⢿⣿⣧⠀⠀⡇⠀⠀⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠉⠉⠻⣄⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⢻⡟⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⢀⣴⣿⡿⠋⠘⢦⣤⠾⠛⣯⠀⠈⠳⣞⠀⣿⡼⠃⠀⠈⠛⢦⡤⠗⠢⣾⡏⠀⠈⠻⣿⣿⣿⣿⣿⣿⣀⡀⣀⠀⠀⢹⠀" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⣧⢻⡘⣄⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⣼⣿⡿⣻⠟⠁⠀⠀⠀⠀⢣⣄⠀⣸⣭⣄⠀⠈⠛⣿⢧⡀⠀⠀⢀⣨⣇⡀⢠⡟⠀⠀⠀⠀⣾⠻⣿⣿⣿⣿⣿⣿⡏⠀⠀⢸⣿" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠹⣜⣧⠀⠳⣄⠀⠀⠰⡀⠀⠀⠀⠀⢰⣿⡏⡼⠋⠀⠀⠀⠀⠀⠀⠀⠙⣿⠁⠀⠈⢳⣄⡞⠃⠀⠹⣄⣼⠋⠀⠈⣿⡿⠀⠀⠀⠀⠀⠙⠳⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⡿" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⢿⣿⡀⠀⠈⠳⣄⠀⢷⠀⠀⠀⢠⣿⣿⣿⣿⢞⡿⠀⠀⠀⠀⠀⠀⠀⢻⣀⣴⣶⣾⣏⡷⠻⣆⣰⣿⣿⣤⣴⣾⣿⡃⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⠀⠀⠀⢀⣁" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠈⣿⣧⠀⠀⠀⠈⢣⡈⣦⠀⢠⣿⣿⣿⣿⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⢰⣛⣿⣟⢿⡞⣇⢀⣾⣿⠉⢻⣿⣿⣻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡟⠀⠀⠀⢸⣿" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠹⣿⡇⠀⠀⠀⠀⠉⠹⣤⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡿⠀⠙⢿⣿⣿⣿⣿⠟⠀⠛⡿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⢸⣿" + RESET)
    time.sleep(0.5)
    print(GREEN + r"            ⠀⠀⠀⠀⠀⠀⢻⣿⣄⠀⠀⡀⣀⣴⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠩⣿⡀⠀⢀⡼⠛⢹⣿⡅⠀⠀⠀⣧⣻⢵⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⢻" + RESET)

def blue_wish():
    print(BLUE + """                                    ⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⡠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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

def gold_wish():
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

# --------------------------------------------------------------------------------------------------------------------------------

main_menu()
name = ""
while name == "":
   name = input("\nPaithon: Welcome to Paithon's Gacha! What is your name, traveler? ").strip()
   if name == "": print("Please enter a name.")
time.sleep(0.25)
print(f"Paithon: What a lovely name, {name}! ✧｡٩(ˊᗜˋ )و✧*｡")

# ---------------Main Menu loop-----------------
while True:
   time.sleep(1.5)
   print("\n\n")
   print("  .-.---------------------------------.-.")
   print("  ((o))                                  )")
   print("  ( )_______          _____         ____/")
   print("  |             MAIN MENU            |")
   print("  |                                  |")
   print("  |  1. Start Game                   |")
   print("  |                                  |")
   print("  |  2. Go Stargazing                |")
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
   print("  / )                                  )")
   print("  ((o))                                  )")
   print("  '------------------------------------'")

   print("\n")
   while True:
       try:
           time.sleep(1)
           menuChoice = int(input("  Enter menu choice (1-6): "))
           if 1 <= menuChoice <= 6:
               break
           else:
               print("Enter a number between 1 to 6.")
       except ValueError:
           print("Invalid input! Try again.")

    # Start Game
   if menuChoice == 1:
       print(
           f"\nPaithon: Hello {name}! In this game, you must play Python-coding related minigames and answer questions"
           "\nto obtain a special currency called \033[95mPrimogems\033[0m in order to wish on the current banner. You need \033[95m1,600\033[0m "
           "\n\033[95mPrimogems\033[0m to wish. Good luck!")

        print("\nChoose a category (or 0 to quit):")
        print("0. Quit")
        print("1. Easy (Formative Assessment)")
        print("2. Medium (Alternative Assessment)")
        print("3. Hard (Summative Assessment)")

        while True:
            try:
                categoryChoice = int(input("\nChoose a category (1-3, 0 to quit): "))
                if 0 <= categoryChoice <= 3:
                    break
                else:
                    print("Enter a number between 0 to 3.")
            except ValueError:
                print("Invalid input! Try again.")

        if categoryChoice == 0:
            print("Returning to main menu!")
            continue
        elif categoryChoice == 1:
            category = "Easy"
            reward = 90
        elif categoryChoice == 2:
            category = "Medium"
            reward = 140
        else:
            category = "Hard"
            reward = 190

        quiz_active = True
        while quiz_active:
            # We filter for questions that belong to the category AND haven't been answered
            matching = [q for q in questions if q["category"] == category and q["answered"] == False]

            if not matching:
                print(f"\nPaithon: No more {category} questions left! You've cleared this level!")
                quiz_active = False  # This breaks the quiz loop
                input("Press Enter to go to Main Menu...")
            else:
                question = random.choice(matching)

                # Handle text format
                text = " ".join(question["text"]) if isinstance(question["text"], list) else question["text"]

                print(f"\n--- {category} ---")
                if question["question_num"] >= 6:
                    print("\n" + text)
                else:
                    print("\n" + text)
                    print("Choices:", ", ".join(question["choices"]))

                answer = input("Answer: ").strip().lower()

                if answer == question["answer"].lower():
                    print(f"Paithon: Correct! You earned {reward} Primogems ദ്ദി(｡•̀,<)~✩‧₊\n")
                    data[0]["primogems"] += reward
                    save_data()
                else:
                    print(f"Paithon: Wrong! (╥﹏╥) The correct answer is {question['answer']}.\n")

                # Mark as answered and save questions
                question["answered"] = True
                with open("quizbee.json", "w") as f:
                    # noinspection PyTypeChecker
                    json.dump(questions, f, indent=4)

                # Ask to continue
                while True:
                    choice = input("\nNext question? 𝘕𝘰 𝘵𝘰 𝘳𝘦𝘵𝘶𝘳𝘯 𝘵𝘰 𝘮𝘦𝘯𝘶 \n"
                                   "(Yes/No): ").lower().strip()
                    if choice == "no" or choice == "yes":
                        break
                    else:
                        print("Invalid input! Try again.")

                if choice == "no":
                    quiz_active = False

            # Save updated questions
            with open("quizbee.json", "w") as f:
                # noinspection PyTypeChecker
                json.dump(questions, f, indent=4)

    # -------------------Go Stargazing--------------------
    elif menuChoice == 2:

        print("You gaze upon the stars as you wish for a companion... ⋆˙⟡ ⋆.˚ ⊹₊⟡ ⋆")
        time.sleep(1)
        print("You see a shooting star.")

        while True:
            wChoice = input("\nMake a wish? (1600 Primogems) \n"
                           "(Yes/No): ").lower().strip()
            if wChoice == "no" or wChoice == "yes":
                break
            else:
                print("Invalid input! Try again.")

        if wChoice == "yes":
            if data[0]['primogems'] >= 1600:
                 data[0]['primogems'] -= 1600
                 save_data()

                # GUARANTEED 4-STAR
                 newItem = item[1]["4*"][random.randint(0,2)]
                 blue_wish()
                 input(f"You find a formidable companion, a unique kind... it's {newItem}! ☆☆☆☆ ")
                 data[0]["inv"].append(newItem)
                 save_data()

                 for i in range(9):
                     # CHANCES
                     chance = random.randint(1, 100)

                     # 3-STAR WEAPON
                     if 1 <= chance <= 50:
                         newItem = item[0]["3*"][random.randint(0,4)]
                         input(f"You find a weapon, a unique kind... it's the {newItem}! ☆☆☆ ")
                         data[0]["inv"].append(newItem)
                         save_data()

                    # OFF-BANNER 4-STARS (Still includes on banners due to increased drop rates!)
                     elif 51 <= chance <= 65:
                         newItem = item[1]["4*"][random.randint(0,11)]
                         blue_wish()
                         input(f"You wished, and you received {newItem}! ☆☆☆☆ ")
                         data[0]["inv"].append(newItem)
                         save_data()

                     # ON BANNER 4-STARS
                     elif 66 <= chance <= 85:
                         newItem = item[1]["4*"][random.randint(0, 2)]
                         blue_wish()
                         input(f"You find a new companion, it's {newItem}! ☆☆☆☆ ")
                         data[0]["inv"].append(newItem)
                         save_data()

                     # 5-STAR DROP
                     elif 86 <= chance <= 100:
                         # 50-50 CHANCE
                         fiftyF = random.randint(1,100)
                         print(f"You find a very special companion...!")
                         gold_wish()

                # 50-50 BETWEEN LIMITED OR PERMANENT 5-STAR
                         # Limited (Xiao)
                         if 1 <= fiftyF <= 50:
                             newItem = item[2]["B5*"][0]

                             print("You meet the limited 5-star character..!")
                             time.sleep(0.3)
                             print("☆☆☆☆☆")
                             time.sleep(0.3)
                             print("You got Adeptus Xiao!")
                             time.sleep(1)
                             xiao_ascii()

                             data[0]["inv"].append(newItem)
                             save_data()

                             time.sleep(0.5)
                             print(f"Paithon: Congratulations, {name}! You've reached the main goal of this game. \n"
                                   "Now, it's up to you. Would you like to continue playing?")
                             while True:
                                 cont = input("(Yes/No): ").lower().strip()
                                 if cont == "no" or cont == "yes":
                                     break
                                 else:
                                     print("Invalid input! Try again.")

                             if cont == "yes":
                                  print("Paithon: Alrighty, have fun ! ✧｡٩(ˊᗜˋ )و✧*｡")
                             else:
                                  print(f"\nPaithon: Leaving,{name}?")
                                  print("Paithon: Alright, byebye!! (˶ᵔᗜᵔ˶)ﾉﾞ")
                                  exit()

                         # Permanent
                         else:
                              newItem = item[2]["OB5*"][random.randint(0,4)]
                              print("You find a 5-star from the permanent wish! A formidable companion indeed~")
                              print(f"You got...")
                              input(f"☆☆☆☆☆ {newItem}! ")
                              data[0]["inv"].append(newItem)
                              save_data()

                 # If Primogems aren't enough to wish
                 else:
                     print("You don't have enough Primogems... (¬_¬＂)")
                     input("Press enter to go back to the main menu! ")
                 # Ensures inventory is saved
                 save_data()

        else:
            print("You decide to save your wish for another day. ✧｡٩(ˊᗜˋ )و✧*｡")
            input("Press enter to go back to the main menu! ")

    # -------------------View Inventory------------------
    elif menuChoice == 3:
        print(f"You currently own {data[0]['primogems']} Primogems.")
        print("You currently own: ")
        owned = set(data[0]["inv"])

        for item in owned:
            print("-", item)
        input("\nPress enter to go back to the main menu! ")

    # --------------------How to Play---------------------
    elif menuChoice == 4:
        instructions()
        input("\nPress enter to go back to the main menu! ")

    # ---------------------Credits---------------------
    elif menuChoice == 5:
        scrolling_credits()
        input("\nPress enter to go back to the main menu! ")

    # -----------------------Quit------------------------
    else:
        print(f"Paithon: Leaving already, {name}?")
        print("Paithon: Alright, byebye!! (˶ᵔᗜᵔ˶)ﾉﾞ")
        exit()