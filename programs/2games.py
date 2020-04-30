import time, sys
print('What would you like to do?')
time.sleep(0.1)
print('Type "g" for a Guessing game')
time.sleep(0.1)
print('or "c" for some fun math')

x = input()

if x == 'g':
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

elif x == 'c':

    import sys
    print('Please enter a number')
    time.sleep(0.1)
    print('Whether even or odd, you have to guess the pattern')
    number = int(input())
    def collatz(number):
        while number != 1:
            if number%2 == 0:
                number = number//2
                print(number)
                if number == 1:
                    sys.exit()
            if number%2 !=0:
                number = 3*number+1
                print(number)
                if number ==1:
                    sys.exit()
    collatz(number)

else:
    print('Not valid. Bye')
    sys.exit()
