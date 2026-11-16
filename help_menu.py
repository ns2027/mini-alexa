"""The complete command reference displayed inside the app."""
HELP = """Commands (case insensitive):
  hello / hi / hey          Greeting
  name / who am i          Show your session name
  date                     Computer's current local date
  time                     Computer's current local time
  calculate 12 + 8          Two-number arithmetic (+, -, *, /)
  calculate                Prompt for an expression; cancel returns
  quote / motivate         Random motivational quote
  joke                     Random joke
  fact                     Random fact
  game / play              Guess 1-20 in at most five attempts
  recommend / activity     Activity based on the current local hour
  perceptron / neuron      Fixed-weight artificial neuron demonstration
  concepts                 Explain AI, ML, and DL in this project
  help / commands / ?      Show this menu
  exit / quit / bye        End the session
You can also ask 'what is the time?' or 'tell me a joke'.
In the game or neuron demo, cancel returns; exit ends the session.
Ctrl+C or end-of-input also closes the assistant gracefully."""


def print_help():
    print(HELP)
