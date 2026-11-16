# Manual acceptance checklist

Run a fresh session and check the following. The date and time should match the computer running the program.

| Step | Input | Expected behavior |
|---|---|---|
| 1 | Shubh at name prompt | Personalized welcome |
| 2 | hello | Greets Shubh |
| 3 | name | Reports Shubh |
| 4 | time | Current local time |
| 5 | date | Current local date |
| 6 | calculate 12 + 8 | 20 |
| 7 | calculate 10 - 3 | 7 |
| 8 | calculate -2 * 4 | -8 |
| 9 | calculate 9 / 2 | 4.5 |
| 10 | calculate 5 / 0 | Friendly error |
| 11 | calculate abc | Usage hint |
| 12 | calculate 1 + 2 + 3 | Rejects extra operation |
| 13 | calculate, then cancel | Returns to main prompt |
| 14 | quote, repeated | Items from quote list; repeats possible |
| 15 | joke, repeated | Items from joke list |
| 16 | fact, repeated | Items from fact list |
| 17 | game | Five attempts; hints and win/loss outcome |
| 18 | game, then cancel | Returns to main prompt |
| 19 | recommend | Appropriate local-hour activity |
| 20 | perceptron, then 1 0 | Weighted sum 0.4; output 1 |
| 21 | perceptron, then 0 1 | Weighted sum -0.6; output 0 |
| 22 | perceptron, then abc | Friendly validation error |
| 23 | concepts | Honest explanation of conceptual scope |
| 24 | help | All commands and aliases |
| 25 | asdkfj | Friendly fallback |
| 26 | empty command | Friendly fallback |
| 27 | WHAT IS THE TIME? | Current time |
| 28 | exit | Personalized goodbye |

Restart with a blank name (defaults to Friend). Test quit, bye, Ctrl+C, and end-of-input in separate sessions, including during each subprompt. A restart must forget the previous name. Automated tests use controlled time inputs and random targets to verify boundaries and game outcomes reproducibly.
