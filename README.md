# 🐉 Danger Dragon

Navigate through the dangers of dragons to collect eggs.

Danger Dragon is a terminal-based Python game where you play as a cowboy 🤠 traversing a 5x5 grid, collecting eggs 🥚 while avoiding volcanic hazards 🌋. Collect 10 eggs to win — but step on a volcano and it's game over!

Built as a learning project through iterative development with AI-assisted coding.

---

## Features

- **WASD Movement** — Move your character up (W), left (A), down (S), and right (D) across a 5x5 grid
- **Collectible Scoring** — Collect eggs scattered across the grid to increase your score
- **Hazard Tiles** — Avoid volcanoes that end the game on contact
- **Win & Lose Conditions** — Reach a score of 10 to win, or hit a volcano to lose
- **Play Again Support** — After each round, choose to play again or exit cleanly
- **Intro Screen** — Game name and story introduction displayed at startup
- **Themed Emojis** — Custom visuals for the player, collectibles, and hazards
- **Boundary Enforcement** — Player cannot move outside the grid

---

## How to Run

### Play the Game

```bash
python game.py
```

### Run the Tests

```bash
pytest
```

### Run Tests with Verbose Output

```bash
pytest -v
```

---

## What I Learned

### Iterative Development

This game was built step by step, starting with a bare grid and layering features one at a time: movement, then collectibles, then hazards, then scoring, then the play-again loop, and finally theming. Each step was small, testable, and self-contained — making it easy to verify that everything worked before moving on.

### Engineering Prompts to Prevent Regression

At each step, I wrote pytest tests *before* moving to the next feature. This created a safety net — when refactoring the game loop or swapping ASCII markers for emojis, the existing tests immediately caught broken behavior. Writing clear, specific prompts for each change ensured that new features didn't break old ones.

### Using Automated Tests

The test suite grew alongside the game. Every feature — grid rendering, WASD movement, boundary checks, spawning logic, collection, hazards, win/lose conditions, reset functionality, and theming — has dedicated tests. Running `pytest` after every change gave instant confidence that the game was still working correctly.

---

## Project Structure

```
ai-terminal-game/
├── game.py          # Main game logic and loop
├── test_game.py     # Pytest test suite (36 tests)
└── README.md        # This file
```

---

## Controls

| Key | Action |
|-----|--------|
| `W` | Move up |
| `A` | Move left |
| `S` | Move down |
| `D` | Move right |
| `q` | Quit the game |

---

## Requirements

- Python 3.10+
- pytest (for running tests)
