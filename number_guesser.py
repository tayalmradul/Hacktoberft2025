"""
Number Guesser 🎯
A simple Python CLI game where the player guesses a random number.
Good for Hacktoberfest contributions!

Features:
- Random number between 1 and 100
- Tracks number of attempts
- Gives hints if guess is too high or too low
- Replay option
"""

import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    print("\n🎯 Welcome to Number Guesser!")
    print("I have selected a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("⬆️ Too low! Try again.")
            elif guess > number:
                print("⬇️ Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Please enter a valid integer.")
    
    replay = input("Do you want to play again? (y/n): ").strip().lower()
    if replay == 'y':
        play_game()
    else:
        print("👋 Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play_game()
