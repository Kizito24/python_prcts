import random

print("=====================================")
print(" 🎯 WELCOME TO THE NUMBER-GUESS GAME ")
print("=====================================\n")

def game_brain():
    print("I'm thinking of a number between 1 and 100...")

    secret_number = random.randint(1,9)
    score=0
    user_guess = int(input("Guess the number: "))

    if user_guess == secret_number:
        score = score + 1
        print("Congrats! You were right.")
    else:
        print("Sorry, you were wrong")
        print(secret_number)
    contn = input("Do you want to continue? ")

    if contn == "y":
        game_brain()
    else:
        print("Thanks for playing, Goodbye!!")

if __name__ == "__main__":
    game_brain()
