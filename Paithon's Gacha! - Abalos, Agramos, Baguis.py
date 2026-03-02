import json

with open("items.json.json", "r") as f:
    item = json.load(f)

with open("inventory.json", "r") as f:
    data = json.load(f)

name = input("Welcome to Paithon's Gacha! What is your name, traveler?")

