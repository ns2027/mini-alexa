# Five-minute demonstration

1. Run `python main.py`, enter `Shubh`, then `hello` and `name` to show session memory.
2. Type `help`, then `date` and `time`.
3. Try `calculate 12 + 8`, `calculate -3 * 4`, `calculate 5 / 0`, and `calculate abc`.
4. Ask for `quote`, `joke`, and `fact` several times. Explain that random choices can repeat.
5. Start `game`, enter guesses and discuss the higher/lower hints and attempt limit.
6. Type `recommend`: explain the hour-based if/elif decision rules.
7. Run `perceptron` with `1 0`, then again with `0 1`. Explain inputs, fixed weights, bias, sum and activation.
8. Enter `concepts`, an unknown command, and `exit`.

Suggested project explanation: “I divided the assistant into small Python modules. The main loop normalizes a command and uses explicit rules to route it. Utilities use standard-library datetime and random. Input validation keeps invalid calculations and guesses from crashing the app. The educational neuron uses fixed arithmetic, so the project demonstrates foundational concepts without training or external services.”

For code review, begin with main.py, then calculator.py, game.py and ai_concepts.py. Be ready to explain each branch rather than describing this project as a general-purpose language model.
