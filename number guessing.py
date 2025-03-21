import random #bring in the random number
import time

number = random.randint(1, 200)  # pick the number between 1 and 200

def intro():
    print("May I ask you for your name?")
    name = input()  # asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")

def pick():
    guessesTaken = 0
    while guessesTaken < 6:  # limit to 6 guesses
        time.sleep(.25)
        enter = input("Guess: ")  # input for guess
        try:  # check if a number was entered
            guess = int(enter)  # convert input to integer

            if 1 <= guess <= 200:  # if in range
                guessesTaken += 1  # increment guess count
                if guessesTaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    if guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess == number:
                    break  # if guess is correct, exit loop

            if guess > 200 or guess < 1:  # if out of range
                print("Silly Goose! That number isn’t in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except:  # if input is not a number
            print("I don’t think that " + enter + " is a number. Sorry")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

# Game loop
playagain = "yes"
while playagain.lower() in ["yes", "y"]:
    intro()
    pick()
    print("Do you want to play again?")
    playagain = input()
