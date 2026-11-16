"""A bounded guessing game. Invalid guesses also consume an attempt."""
import random

LOW, HIGH, MAX_ATTEMPTS = 1, 20, 5


def play_guessing_game():
    secret = random.randint(LOW, HIGH)
    print(f"Mini Alexa: Guess a number from {LOW} to {HIGH}. You have {MAX_ATTEMPTS} tries.")
    print("Type cancel to return. Invalid entries count as a try.")
    for attempt in range(1, MAX_ATTEMPTS + 1):
        raw = input(f"Guess {attempt}/{MAX_ATTEMPTS}: ").strip().lower()
        if raw in {"cancel", "back"}:
            return "Game cancelled."
        if raw in {"exit", "quit", "bye"}:
            raise EOFError
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if not LOW <= guess <= HIGH:
            print(f"Please stay between {LOW} and {HIGH}.")
        elif guess == secret:
            return f"Correct! You won in {attempt} tries."
        elif guess < secret:
            print("Try higher.")
        else:
            print("Try lower.")
    return f"No tries left. The number was {secret}."
