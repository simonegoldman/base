import random
import sys
mynumber = random.randint(1,10)

print('What is your name?')
name = input()
print('Hi,' + name)

while True:
    print('')
    print(name + ', I am thinking of a number 1-10')
    print('Take a guess')

    try:
        guess = int(input())
        if guess > mynumber:
            print('')
            print('Too high, try lower')
            continue
        elif guess < mynumber:
            print('')
            print('Too low, try higher')
            continue
        elif guess == mynumber:
            print('')
            print('Spot on! ' + str(mynumber) + ' is correct')
        break

    except (ValueError, NameError) as error:
        print('')
        print('Not a valid input. Please try again')
        continue
