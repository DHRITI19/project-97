introString = input("Number Guessing Game")
while chances < 5:
    if guess == number:
        print("Congratulations YOU WON!!")
        break
        if not chances < 5:
            print("YOU LOOSE!! The number is'',number")