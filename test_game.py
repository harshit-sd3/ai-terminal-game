import pytest
from game import player_pos, draw_grid, move_player


@pytest.fixture(autouse=True)
def reset_player():
    """Reset player to (0, 0) before every test."""
    player_pos[0] = 0
    player_pos[1] = 0


# --- Grid tests ---


def test_player_starts_at_origin():
    """Player should start at position (0, 0)."""
    assert player_pos == [0, 0]


def test_grid_is_five_by_five():
    """Grid output should contain exactly 5 rows of cells."""
    import io
    import sys

    captured = io.StringIO()
    sys.stdout = captured
    draw_grid()
    sys.stdout = sys.__stdout__

    output = captured.getvalue()

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


# --- Movement tests ---


def test_move_right():
    """D should move the player one space right."""
    move_player("d")
    assert player_pos == [0, 1]


def test_move_left():
    """A should move the player one space left."""
    player_pos[0] = 0
    player_pos[1] = 1
    move_player("a")
    assert player_pos == [0, 0]


def test_move_down():
    """S should move the player one space down."""
    move_player("s")
    assert player_pos == [1, 0]


def test_move_up():
    """W should move the player one space up."""
    player_pos[0] = 1
    player_pos[1] = 0
    move_player("w")
    assert player_pos == [0, 0]


# --- Boundary tests ---


def test_cannot_move_above_top():
    """Player at (0,0) should not move up off the grid."""
    move_player("w")
    assert player_pos == [0, 0]


def test_cannot_move_below_bottom():
    """Player at bottom row should not move down off the grid."""
    player_pos[0] = 4
    player_pos[1] = 0
    move_player("s")
    assert player_pos == [4, 0]


def test_cannot_move_left_of_grid():
    """Player at (0,0) should not move left off the grid."""
    move_player("a")
    assert player_pos == [0, 0]


def test_cannot_move_right_of_grid():
    """Player at right edge should not move right off the grid."""
    player_pos[0] = 0
    player_pos[1] = 4
    move_player("d")
    assert player_pos == [0, 4]
