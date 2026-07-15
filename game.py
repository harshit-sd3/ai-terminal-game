import os

# Game state
player_pos = [0, 0]  # [row, col] starting at top-left

def draw_grid():
    """Draw a 5x5 grid with the player's position marked."""
    size = 5
    print("\n+" + "---+" * size)

    for row in range(size):
        line = "|"
        for col in range(size):
            if row == player_pos[0] and col == player_pos[1]:
                line += " P |"  # Player's position
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
    while True:
        os.system("clear")  # Clear the terminal
        draw_grid()
        print("WASD to move | q to quit")
        command = input("> ")

        if command == "q":
            print("Thanks for playing!")
            break

        if command in "wasd":
            move_player(command)

if __name__ == "__main__":
    main()
