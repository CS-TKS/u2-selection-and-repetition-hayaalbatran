#Tree Planting Education Game

import random

#Welcome Message
print("Welcome to the Tree Planting Education Game!")

#Different environments and suitable trees
environments = ["desert", "rainforest", "urban", "mountain"]
tree_types = {
    "desert": ["Acacia", "Date Palm"]
    "rainforest": ["Mahogany", "Kapok"]
    "urban": ["Maple", "Oak",]
    "mountain":["Pine", "Fir"]
}

#Player score
score = 0

#Game loop
play = True

while play:
    #Randomly choose an evironment
    current_env = random.choice(environments)
    print("\nEnvironment:", current_env.capitalize())

    #Show tree options
    print("Choose a tree to plant in this environment")
    options = random.sample(tree_type[current_env], 1)
    wrong_envs = [env for env in environments if env != current_env]
    wrong_tree = random.choice(tree_types[random.choice(wrong_envs)])
    options.append(wrong_tree)
    random.shuffle(options)

    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

    choice = input("Enter the number of your choice (or type 'exit' to stop):")


    if choice.lower() == 'exit'
        play = False
        print("\nThanks for playing! Your final score is:", score)
        break

    #Validate input
    choice = int(choice)

    if seleced_tree in tree_types [current_env]
        print("Great choice! That tree fits the environments")
        score += 1
    else:
        print("Oops! That tree doesn't grow well here.")
else:
    print("Please choose a valid option from the list")

print("Current score", score)

print("Game Over. Keep planting trees and saving the planet!")

