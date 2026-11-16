"""Capture a name in memory for the current session only."""
def get_user_name():
    return input("You (name): ").strip() or "Friend"


def build_greeting(name):
    return f"Nice to meet you, {name}! Type 'help' to see my commands."
