print('Welcome to Treasure Island. Your Mission is to Find the Treasure')

direction = input("what are you choose the direction?, Right or Left").title()

if direction == 'Left':
    movement = input("what are you choose the movement, Swim or Wait").title()
    
    if movement == 'Wait':
        choice_door = input("What are you choose the door?, Red, Blue, Yellow, or other").title()

        if choice_door == 'Yellow':
            print("You Win")
        elif choice_door == 'Red':
            print("Burned by Fire. Game Over")
        elif choice_door == 'Blue':
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into a hole. game over")