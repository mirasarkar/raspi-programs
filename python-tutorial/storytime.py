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

actor_name = random.choice(names)
actor_role = random.choice(roles)
quest = random.choice(actions)
start_place = random.choice(places)
end_place = random.choice(places)

story = "In the " + start_place + " there was a " + \
        actor_role + " called " + actor_name + \
        " who did not want to go to the " + end_place + "."
print(story)

        
