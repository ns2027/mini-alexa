"""Predefined offline content selected with Python's random module."""
import random

QUOTES = ["Small steps every day lead to progress.", "Practice makes difficult things familiar.",
          "Start where you are and keep learning.", "Mistakes are opportunities to learn.",
          "Consistency matters more than speed."]
JOKES = ["Why did the developer go broke? They used up all their cache.",
         "Why do programmers prefer dark mode? Light attracts bugs.",
         "What is a computer's favourite snack? Microchips.",
         "Why did the computer get cold? It left its Windows open.",
         "Why was the math book sad? It had too many problems."]
FACTS = ["An octopus has three hearts.", "The Sun is a star.",
         "A triangle has three sides.", "A byte contains eight bits.",
         "Python lists can hold values of different types."]


def get_random_quote():
    return random.choice(QUOTES)


def get_random_joke():
    return random.choice(JOKES)


def get_random_fact():
    return random.choice(FACTS)
