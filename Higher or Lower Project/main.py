import random
import game_data
from art import logo, vs

first_run = True
score = 0
guess = ""
a = {}
b = {}

def show_contenders():
    print(logo)
    print(f"Contenders remaining: {len(game_data.data)}.")

    if len(game_data.data) == 1:
        print("You are the Boss!")
        return

    global a
    global b
    global first_run
    global guess
    global score

    if first_run:
        a = random.choice(game_data.data)
        game_data.data.remove(a)
        first_run = False

    b = random.choice(game_data.data)
    game_data.data.remove(b)

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ")

    if (guess == "A" and a['follower_count'] > b['follower_count']) or (guess == "B" and b['follower_count'] > a['follower_count']):
        correct_answer()
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")

def correct_answer():
    global score
    global guess
    global a
    global b

    score += 1
    print(f"You're right! Current score: {score}.")
    print("\n" * 100)

    if guess == "B":
        a = b

    show_contenders()

show_contenders()