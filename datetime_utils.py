"""Use the computer's local clock, with no network access."""
from datetime import datetime


def get_current_time():
    return datetime.now().strftime("%I:%M:%S %p")


def get_current_date():
    return datetime.now().strftime("%A, %d %B %Y")
