from game import player_pos, draw_grid


def test_player_starts_at_origin():
    """Player should start at position (0, 0)."""
    assert player_pos == [0, 0]


def test_grid_is_five_by_five():
    """Grid output should contain exactly 5 rows of cells."""
    # Capture what draw_grid prints to the terminal
    import io
    import sys

    captured = io.StringIO()
    sys.stdout = captured
    draw_grid()
    sys.stdout = sys.__stdout__  # Reset stdout back to normal

    output = captured.getvalue()

    # Count how many "+" border lines appear
    # A 5x5 grid has a top border for each of the 5 rows, plus a bottom
    # border after the last row — that's 6 border lines total
    plus_lines = [line for line in output.splitlines() if line.startswith("+")]
    assert len(plus_lines) == 6


def test_grid_shows_player():
    """Grid should display the player marker 'P'."""
    import io
    import sys

    captured = io.StringIO()
    sys.stdout = captured
    draw_grid()
    sys.stdout = sys.__stdout__

    output = captured.getvalue()
    assert "P" in output
