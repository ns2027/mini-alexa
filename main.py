"""Mini Alexa: an offline, rule-based assistant using the standard library."""
import re
from greetings import get_user_name, build_greeting
from datetime_utils import get_current_date, get_current_time
from calculator import parse_expression, calculate
from content import get_random_quote, get_random_joke, get_random_fact
from game import play_guessing_game
from ai_concepts import recommend_activity, perceptron_demo
from help_menu import print_help

EXIT_COMMANDS = {"exit", "quit", "bye"}


def normalize(text):
    return " ".join(text.lower().strip().split())


def respond(command, name):
    """Match whole-word keywords in a documented order, then call one feature."""
    words = set(re.findall(r"[a-z]+", command))
    if command.strip(".!?") in EXIT_COMMANDS:
        return False
    if command == "?" or words & {"help", "commands"}:
        print_help()
        return True
    if words & {"calculate", "calc"}:
        expression = re.sub(r"^.*?\b(?:calculate|calc)\b", "", command).strip()
        if not expression:
            expression = input("Expression (e.g. 12 + 8; or cancel): ").strip().lower()
            if expression in {"cancel", "back"}:
                print("Mini Alexa: Calculation cancelled.")
                return True
            if expression in EXIT_COMMANDS:
                return False
        try:
            response = f"The result is {calculate(*parse_expression(expression)):g}"
        except ValueError as error:
            response = str(error)
    elif words & {"perceptron", "neuron"}:
        response = perceptron_demo()
    elif words & {"concept", "concepts"}:
        response = ("AI: explicit rules match commands and choose responses. "
                    "ML analogy: activity labels resemble classification, but rules are hand-written. "
                    "Remembering your name is session memory, not machine learning. "
                    "DL foundation: the perceptron demonstrates weights, bias and activation. "
                    "A single fixed neuron is not deep learning; nothing is trained here.")
    elif words & {"recommend", "activity", "recommendation"}:
        response = recommend_activity() + " (Chosen using fixed time-of-day rules.)"
    elif words & {"game", "play"}:
        response = play_guessing_game()
    elif words & {"date", "today"}:
        response = f"{name}, today is {get_current_date()}."
    elif "time" in words:
        response = f"{name}, the current time is {get_current_time()}."
    elif words & {"quote", "motivate", "motivation"}:
        response = get_random_quote()
    elif "joke" in words:
        response = get_random_joke()
    elif "fact" in words:
        response = get_random_fact()
    elif command in {"name", "who am i", "what is my name", "what is my name?"}:
        response = f"Your name is {name}. I remember it for this session."
    elif words & {"hello", "hi", "hey"}:
        response = f"Hello, {name}! How can I help?"
    else:
        response = f"I'm not sure I understood that, {name}. Type 'help' to see my commands."
    print("Mini Alexa: " + response)
    return True


def main():
    """Keep only session-local state and handle interrupted input at every prompt."""
    name = "Friend"
    print("MINI ALEXA - VIRTUAL AI ASSISTANT")
    print("Offline | Text only | Rule based")
    print("Mini Alexa: Hi! What's your name?")
    try:
        name = get_user_name()
        print("Mini Alexa: " + build_greeting(name))
        while True:
            if not respond(normalize(input("You: ")), name):
                break
    except (EOFError, KeyboardInterrupt):
        print()
    print(f"Mini Alexa: Goodbye, {name}! Have a great day.")


if __name__ == "__main__":
    main()
