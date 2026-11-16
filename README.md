# Virtual AI Assistant (Mini Alexa)

A beginner-friendly offline terminal application implementing the supplied Nexbridge Technologies PRD (AI-INT-P1-VAA). Uses only the Python standard library. No pip installation, API key or internet connection is needed. Python 3.8 or later is recommended.

## Run on Windows / VS Code

1. Extract the ZIP.
2. Open the extracted `virtual-ai-assistant` folder in VS Code.
3. Select Terminal > New Terminal.
4. Run `python main.py` (or `py main.py` on Windows).
5. Enter your name, then type `help`.

On macOS / Linux use `python3 main.py`. If Python is not recognized, install Python 3 and enable its PATH option on Windows. Run from a terminal, not VS Code's noninteractive Output panel.

## Commands

| Command | Result |
|---|---|
| hello / hi / hey | Personalized greeting |
| name / who am i | Remembered session name |
| date | Current computer-local date |
| time | Current computer-local time |
| calculate 12 + 8 | Addition; also supports -, *, / |
| calculate | Prompt for two-number expression |
| quote / motivate | Motivational quote |
| joke | Random joke |
| fact | Random fact |
| game / play | Guess a number 1–20 in five attempts |
| recommend / activity | Time-based activity recommendation |
| perceptron / neuron | Two-input artificial neuron demo |
| concepts | Explanation of AI, ML and DL concepts |
| help / commands / ? | Complete command menu |
| exit / quit / bye | Goodbye and clean exit |

Natural phrasings like `what is the time?` and `tell me a joke` work through whole-word keyword matching. Input is case insensitive. One command is processed per turn; if multiple keywords occur, the first matching rule in `respond()` wins. Compound requests are not supported.

The calculator supports signed decimals and scientific notation, with exactly two numbers and one operator. It never uses eval. Type `cancel` in a calculator prompt, game or neuron demo to return. Exit, Ctrl+C and end-of-input close gracefully from subprompts too. The game counts invalid entries toward its five attempts and reveals the answer on a loss. Random content may repeat by chance.

## Architecture and approach

`main.py` captures a session name, normalizes commands, matches keyword rules, calls a feature and prints its response. All state is in memory and disappears when the program ends. Independent modules handle greetings, date/time, arithmetic, content, the game, help and educational concepts.

| Requirement | Implementation |
|---|---|
| FR-01, FR-02 | greetings.py and main.py: startup greeting and reused name |
| FR-03, FR-04 | datetime_utils.py: local system date and time |
| FR-05 | calculator.py: validated arithmetic and friendly errors |
| FR-06, FR-07, FR-08 | content.py: predefined lists and random.choice |
| FR-09 | game.py: random target, hints and five attempts |
| FR-10 | help_menu.py: all commands |
| FR-11, FR-12 | main.py: exit, interrupted input and fallback |
| FR-13 | ai_concepts.py: hour-based decision rules |
| FR-14 | ai_concepts.py: fixed weights, bias and step activation |

## AI, ML and DL explanation for your presentation

- **AI:** Explicit rules recognize intents and choose responses. Whole-word matching avoids matching `time` inside `sometimes`.
- **ML analogy:** The recommendation assigns an activity label to an hour, resembling classification. Its decision boundaries are written by a person; no model learns them. Remembering a name is session storage, not training.
- **DL foundation:** A perceptron shows a single neuron's forward calculation. Weights are `(0.6, -0.4)`, bias is `-0.2`, and output is 1 when the weighted sum is strictly greater than 0; otherwise 0. Inputs `1 0` yield sum `0.4`, output `1`. Inputs `0 1` yield sum `-0.6`, output `0`. This is not a trained model or deep network.

## Verification

Run `python -m unittest discover -s tests -v` from the project folder. Tests cover arithmetic and malformed input, zero division, overflow, recommendation boundaries, neuron outputs, content selection, game hints/win/loss/cancellation, routing, a session with more than 20 inputs, and interrupted prompts. The randomness test verifies list selection deterministically; it does not claim that every five live draws must be different.

See TESTING.md for a manual acceptance checklist and DEMO.md for a mentor walkthrough.
