from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You are greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")

    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear slaps.")
        elif choice == "taunt bear" and not bear_moved:
            print("You can go through the door")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear chew your leg")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

def cthulhu_room():
    print("here lives the great evil cthulhu")
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You are in the sark room.")
    print("There is a door to your left, another in right.")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stucked in the room and starved to death.")

start()
