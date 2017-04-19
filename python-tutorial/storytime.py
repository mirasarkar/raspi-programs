import random

print("Hello reader")

name = input("What is your name? ")
print("Hello " + name)
gender = input("Are you a boy or girl? ")
day = input("What is the day today? ")

if gender == "girl":
    pronoun = "she"
elif gender == "boy":
    pronoun = "he"
else:
    pronoun = "it"

names = ["Sybil", "Won-won", "Albus", "Hermione", "Minerva", "Luna", "Rita", "Rubeus", "Dude", "Filo"]
roles = ["seer", "wizard", "genius", "teacher", "editor", "cook", "gamekeeper", "programmer", "student", "servant"]
actions = ["find", "get", "learn", "buy", "travel", "hide", "cook", "predict", "raise", "code"]  
places = ["Green Palace", "Flying Academy", "Grinwald School of Magic", "Dungeon Kitchen", "Enchanted Computer Room", "Cleaner's Hut", "Grassy Grounds"]

story = "In the " + random.choice(places) + " there was a " + \
        random.choice(roles) + " called " + random.choice(names) + \
        " who did not want to go to the " + random.choice(places) + "."
print(story)

        
