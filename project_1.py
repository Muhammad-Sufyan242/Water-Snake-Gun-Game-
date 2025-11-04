# import the random module
import random
print("Welcome to the game of Water, Snake, Gun!")
random_string = random.choice(["water", "snake", "gun"])
# while true use because user select the invalid choice than ask again
while True:
    select=input("enter your choice(w=water,s=snake,g=gun):").lower()
# when user not enteer the input so ask again
    while not select:
        select=input("enter your choice(w=water,s=snake,g=gun):").lower()

    if "w"==select:
        print("you select : water")
        break
    # We use break to exit the loop immediately after the user enters a valid input. if not use of break  over all code under the loop will be executed
    elif "s"==select:
        print("you select : snake")
        break
    elif "g"==select:
        print("you select : gun")
        break
    else:
        print("Invalid selection")
# get the computer selection
print(f"computer select : {random_string}")
# main logic of the game
# for win
if random_string=="snake" and select=="g" or random_string=="water" and select=="s" or random_string=="gun" and select=="w":
    print("you win")
    print("computer lose")
# for lose
elif random_string=="gun" and select=="s" or random_string=="snake" and select=="w" or random_string=="water" and select=="g":
    print("you lose")
    print("computer win")
else:
    print("draw the match")

