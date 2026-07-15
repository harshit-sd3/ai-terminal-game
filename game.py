import os
import random

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
    """Draw a 5x5 grid with the player and collectible."""
    size = 5
    print(f"\n  Score: {score}/{WIN_SCORE}")
    print("+" + "---+" * size)

    for row in range(size):
        line = "|"
        for col in range(size):
            if row == player_pos[0] and col == player_pos[1]:
                line += " P |"
            elif row == item_pos[0] and col == item_pos[1]:
                line += " * |"  # Collectible
            elif row == hazard_pos[0] and col == hazard_pos[1]:
                line += " X |"  # Hazard
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

def main():
    """Main game loop."""
    global score

    spawn_item()  # Place the first collectible
    spawn_hazard()  # Place the first hazard

    while True:
        os.system("clear")  # Clear the terminal
        draw_grid()

        if score >= WIN_SCORE:
            print("You win! Thanks for playing!")
            break

        print("WASD to move | q to quit")
        command = input("> ")

        if command == "q":
            print("Thanks for playing!")
            break

        if command in "wasd":
            move_player(command)

            # Check if player landed on the collectible
            if player_pos == item_pos:
                score += 1
                spawn_item()

            # Check if player landed on the hazard
            if player_pos == hazard_pos:
                print("Game Over!")
                break

if __name__ == "__main__":
    main()
