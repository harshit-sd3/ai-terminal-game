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

def main():
    """Main game loop."""
    while True:
        os.system("clear")  # Clear the terminal
        draw_grid()
        print("Enter 'q' to quit.")
        command = input("> ")

        if command == "q":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
