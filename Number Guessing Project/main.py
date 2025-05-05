import random
hidden_number = 0
difficulty = ""
guess = 0

def guess_the_number(ar):
    global guess
    while ar > 0 and guess != hidden_number:

        print(f"You have {ar} attempts to guess the number.")
        ar -= 1
        guess = int(input("Make a guess: "))

        if guess == hidden_number:
            print("You guessed the number correctly")
            end_game()
        elif guess < hidden_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    if ar == 0:
        print("You ran out of guesses. Game over.")

def end_game():
    print(f"You got it. The number is {hidden_number}.")
    print("Thank you for playing!")

def initiate_guessing_game():
    global hidden_number
    global difficulty
    hidden_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        guess_the_number(10)
    else:
        guess_the_number(5)

initiate_guessing_game()
