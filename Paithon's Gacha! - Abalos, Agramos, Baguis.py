import json

with open("items.json", "r") as f:
    item = json.load(f)

with open("inventory.json.json", "r") as f:
    data = json.load(f)

name = input("Welcome to Paithon's Gacha! What is your name, traveler?")

print("\n\n")
print(" .-.---------------------------------.-.")
print(" ((o))                                   )")
print(" \o)_______          _____         ____/")
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
print(" /A\                                  )")
print("((o))                                  )")
print(" '-'----------------------------------'")

print("\n")