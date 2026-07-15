import os
import random

# Theme
GAME_NAME = "Danger Dragon"
STORY_INTRO = "Navigate through the dangers of dragons to collect eggs."
PLAYER_EMOJI = "🤠"
ITEM_EMOJI = "🥚"
HAZARD_EMOJI = "🌋"
WIN_MESSAGE = "Wohoo!! You win!!"
LOSE_MESSAGE = "Oopsie! Dargon got you! You lose"

# Game state
player_pos = [0, 0]  # [row, col] starting at top-left
item_pos = [0, 0]    # [row, col] collectible position
hazard_pos = [0, 0]  # [row, col] hazard position
score = 0
WIN_SCORE = 10

def spawn_item():
    """Place the collectible at a random position that isn't the player's."""
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if [row, col] != player_pos:
            item_pos[0] = row
            item_pos[1] = col
            break

def spawn_hazard():
    """Place the hazard at a random position that isn't the player or item."""
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if [row, col] != player_pos and [row, col] != item_pos:
            hazard_pos[0] = row
            hazard_pos[1] = col
            break

def draw_grid():
    """Draw a 5x5 grid with the player, collectible, and hazard."""
    size = 5
    print(f"\n  Score: {score}/{WIN_SCORE}")
    print("+" + "---+" * size)

    for row in range(size):
        line = "|"
        for col in range(size):
            if row == player_pos[0] and col == player_pos[1]:
                line += f" {PLAYER_EMOJI} |"
            elif row == item_pos[0] and col == item_pos[1]:
                line += f" {ITEM_EMOJI} |"
            elif row == hazard_pos[0] and col == hazard_pos[1]:
                line += f" {HAZARD_EMOJI} |"
            else:
                line += "   |"
        print(line)
        print("+" + "---+" * size)

    print()

def move_player(direction):
    """Move the player one space in the given direction if within bounds."""
    row, col = player_pos
    new_row, new_col = row, col

    if direction == "w":
        new_row = row - 1
    elif direction == "s":
        new_row = row + 1
    elif direction == "a":
        new_col = col - 1
    elif direction == "d":
        new_col = col + 1

    if 0 <= new_row < 5 and 0 <= new_col < 5:
        player_pos[0] = new_row
        player_pos[1] = new_col

def reset_game():
    """Reset all game state for a new round."""
    global score
    player_pos[0] = 0
    player_pos[1] = 0
    score = 0
    spawn_item()
    spawn_hazard()

def show_intro():
    """Display the game name and story intro."""
    os.system("clear")
    print()
    print(f"  === {GAME_NAME} ===")
    print()
    print(f"  {STORY_INTRO}")
    print()
    input("  Press Enter to start... ")

def main():
    """Main game loop with play again support."""
    global score

    show_intro()

    while True:
        reset_game()

        # Active play loop
        while True:
            os.system("clear")
            draw_grid()

            if score >= WIN_SCORE:
                print(f"  {WIN_MESSAGE}")
                break

            print("  WASD to move | q to quit")
            command = input("  > ")

            if command == "q":
                print("  Thanks for playing!")
                return

            if command in "wasd":
                move_player(command)

                if player_pos == item_pos:
                    score += 1
                    spawn_item()

                if player_pos == hazard_pos:
                    print(f"  {LOSE_MESSAGE}")
                    break

        # Play again prompt
        while True:
            choice = input("\n  Play again? (y/n) ").lower()
            if choice == "y":
                break
            elif choice == "n":
                print("  Goodbye!")
                return

if __name__ == "__main__":
    main()
