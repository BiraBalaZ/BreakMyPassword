from random import randrange
from os import system
system('cls')

def leftGame():
    system('cls')
    print('You decided to leave.')
    exit(1)

def checkHits():
    return sum(1 for i in range(4) if password[i] == userInput[i])

# Set difficult
print('What difficulty do you want to play?\n\n\033[32m[1] - Easy\033[m\n\033[33m[2] - Medium\033[m\n\033[31m[3] - Hard\033[m\n\033[34m[Other] - Exit\033[m')
difficult = str(input('>>>'))

if difficult == '1':
    digits = 4
elif difficult == '2':
    digits = 6
elif difficult == '3':
    digits = 8
else:
    leftGame()

password = [str(randrange(10)) for _ in range(digits)]

system('cls')
print(f'I thought of a {digits} digit password. Can you guess?')

if difficult == '3':
    print('\n\033[31mThe terminal will not save what you sent.\nYou´re fucked up.\033[35m >:)\033[m\n')

print('\033[33mSend any letter to leave.\033[m')

# Showing password for debug
print(password)

userInput = None

while True:
    suggest = str(input('>>>'))

    if not suggest.isdigit():  
        leftGame()

    while len(suggest) < digits:
        system('cls')

        if difficult != '3':
            if userInput != None:
                print(f'Last valid option entered: {userInput}')
                print(f'You got {checkHits()} hits')

        print(f'\033[31mYou must enter at least {digits} digits\033[m')

        # Getting user suggestion
        suggest = str(input('>>>'))

        if not suggest.isdigit():  
            leftGame()
    
    userInput = [suggest[i] for i in range(4)]

    # Checking the numbers
    checkHits()

    # If the difficulty is Hard, the game erase terminal so the player does not read the previous prompts
    if difficult == '3':
        system('cls')

    # Printing hit count
    print(f'{checkHits()} correct numbers')

    # If the hit count is equal to digits, the game ends
    if checkHits() == digits:
        print("\n🎉 Congratulations! All numbers are correct! 🎉")
        break
