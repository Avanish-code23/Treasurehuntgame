def game_over():
    print("\nGame Over!")
    lets_play_again()

def lets_play_again():
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        start()
    else:
        print("Thank you for playing!")

def snake_room():
    print("\nThere is a snake here.")
    print("Behind the Snake is another door.")
    print("The snake is having eggs!")
    print("What would you do? (1 or 2)")
    print("1). Take the eggs.")
    print("2. Taunt the snake")
    
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("\nYou want eggs not the treasure !! Thats why the snake killed you.")
        game_over()
    elif choice == '2':
        print("\nThe snake is now your friend!")
        treasure_room()
    else:
        print("\nInvalid choice! The game is over.")
        game_over()

def monster_room():
    print("\nNow you enered the room of a monster!")
    print("Do you:")
    print("1. Go through the door silenly")
    print("2. Kill the monster and show your courage")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("\nYour scream echoes through the dungeon. The monster runs away.")
        treasure_room()
    elif choice == '2':
        print("\nThe monster was hungry , he/it ate you")
        game_over()
    else:
        print("\nInvalid choice! The game is over.")
        game_over()

def treasure_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("\nTake some diamonds and go through the door.")
    elif choice == '2':
        print("\n Just go through the door.")
        game_over()
    else:
        print("\nInvalid choice! The game is over.")
        game_over()
    lets_play_again()

def start():
    print("You are standing in a dark room.")
    print("There is a door to your left and right.")
    choice = input("Which one do you take? (l or r): ").lower()
    if choice == 'l':
        snake_room()
    elif choice == 'r':
        monster_room()
    else:
        print("\nInvalid choice! The game is over.")
        game_over()

# Starting the game
start()
