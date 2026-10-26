# Roadmap.sh Beginner Projects

This repository contains small projects based on the beginner project ideas
from [roadmap.sh](https://roadmap.sh/projects). Each project is intended to
provide practical experience with programming fundamentals through a focused,
working application.

## Projects

### Number Guessing Game

A command-line game where the computer chooses a number from 1 to 100 and the
player tries to guess it before running out of chances. Choose a difficulty to
set the number of guesses:
https://roadmap.sh/projects/number-guessing-game
| Difficulty | Chances |
| --- | ---: |
| Easy | 10 |
| Medium | 5 |
| Hard | 3 |

Run it with Python 3:

```bash
python3 Number-guessing-game/main.py
```

The game gives higher-or-lower hints after incorrect guesses, validates
difficulty selections and guesses, and reports the result when the game ends.

## Project Guidelines

These guidelines apply to the projects in this repository:

- Keep each project focused on the original beginner-level idea and its core
  requirements.
- Give each project its own directory and include clear instructions for
  running it.
- Prefer simple, readable implementations that demonstrate fundamentals over
  unnecessary frameworks or abstractions.
- Validate user input and provide helpful feedback for invalid entries.
- Avoid adding dependencies unless they are needed; document any dependencies
  and setup steps when they are introduced.
- Test the main success and failure paths before considering a project
  complete.
- Update this README's project list and usage instructions as new projects are
  added.
