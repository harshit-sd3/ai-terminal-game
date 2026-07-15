import io
import sys

import pytest
from game import player_pos, item_pos, hazard_pos, score, draw_grid, move_player, spawn_item, spawn_hazard, reset_game, show_intro, WIN_SCORE, PLAYER_EMOJI, ITEM_EMOJI, HAZARD_EMOJI, GAME_NAME, STORY_INTRO, WIN_MESSAGE, LOSE_MESSAGE
import game


@pytest.fixture(autouse=True)
def reset_game_state():
    """Reset all game state before every test."""
    reset_game()


def capture_grid():
    """Helper: draw the grid and return the output as a string."""
    captured = io.StringIO()
    sys.stdout = captured
    draw_grid()
    sys.stdout = sys.__stdout__
    return captured.getvalue()


# --- Grid tests ---


def test_player_starts_at_origin():
    """Player should start at position (0, 0)."""
    assert player_pos == [0, 0]


def test_grid_is_five_by_five():
    """Grid output should contain exactly 6 border lines."""
    output = capture_grid()
    plus_lines = [line for line in output.splitlines() if line.startswith("+")]
    assert len(plus_lines) == 6


def test_grid_shows_player():
    """Grid should display the player emoji."""
    output = capture_grid()
    assert PLAYER_EMOJI in output


def test_grid_shows_collectible():
    """Grid should display the collectible emoji."""
    output = capture_grid()
    assert ITEM_EMOJI in output


def test_grid_shows_score():
    """Grid output should display the current score."""
    game.score = 5
    output = capture_grid()
    assert "Score: 5/10" in output


# --- Movement tests ---


def test_move_right():
    """D should move the player one space right."""
    move_player("d")
    assert player_pos == [0, 1]


def test_move_left():
    """A should move the player one space left."""
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
    move_player("s")
    assert player_pos == [4, 0]


def test_cannot_move_left_of_grid():
    """Player at (0,0) should not move left off the grid."""
    move_player("a")
    assert player_pos == [0, 0]


def test_cannot_move_right_of_grid():
    """Player at right edge should not move right off the grid."""
    player_pos[1] = 4
    move_player("d")
    assert player_pos == [0, 4]


# --- Spawn tests ---


def test_spawn_not_on_player():
    """Collectible should never spawn on the player's position."""
    player_pos[0] = 3
    player_pos[1] = 3
    for _ in range(100):
        spawn_item()
        assert [item_pos[0], item_pos[1]] != [3, 3]


def test_spawn_places_item_on_grid():
    """Collectible should always be within the 5x5 grid."""
    for _ in range(100):
        spawn_item()
        assert 0 <= item_pos[0] < 5
        assert 0 <= item_pos[1] < 5


# --- Collection tests ---


def test_collect_item_increments_score():
    """Score should increase by 1 when player moves onto the collectible."""
    item_pos[0] = 0
    item_pos[1] = 1  # place item to the right of player
    move_player("d")
    assert player_pos == item_pos
    game.score += 1
    assert game.score == 1


def test_collect_item_respawns():
    """After collection, the collectible should respawn at a new position."""
    item_pos[0] = 0
    item_pos[1] = 1
    move_player("d")
    game.score += 1
    spawn_item()
    # Item should now be somewhere else, not on the player
    assert [item_pos[0], item_pos[1]] != player_pos


# --- Win condition tests ---


def test_win_condition_at_score_10():
    """Game should detect win when score reaches WIN_SCORE."""
    game.score = WIN_SCORE
    assert game.score >= WIN_SCORE


def test_no_win_below_score_10():
    """Game should not end when score is below WIN_SCORE."""
    game.score = 9
    assert game.score < WIN_SCORE


# --- Hazard tests ---


def test_grid_shows_hazard():
    """Grid should display the hazard emoji."""
    output = capture_grid()
    assert HAZARD_EMOJI in output


def test_hazard_spawn_not_on_player():
    """Hazard should never spawn on the player's position."""
    player_pos[0] = 2
    player_pos[1] = 2
    item_pos[0] = 4
    item_pos[1] = 4
    for _ in range(100):
        spawn_hazard()
        assert [hazard_pos[0], hazard_pos[1]] != [2, 2]


def test_hazard_spawn_not_on_item():
    """Hazard should never spawn on the collectible's position."""
    player_pos[0] = 0
    player_pos[1] = 0
    item_pos[0] = 4
    item_pos[1] = 4
    for _ in range(100):
        spawn_hazard()
        assert [hazard_pos[0], hazard_pos[1]] != [4, 4]


def test_hazard_spawn_within_grid():
    """Hazard should always be within the 5x5 grid."""
    for _ in range(100):
        spawn_hazard()
        assert 0 <= hazard_pos[0] < 5
        assert 0 <= hazard_pos[1] < 5


def test_hazard_collision_ends_game():
    """Stepping on the hazard should trigger the game over condition."""
    hazard_pos[0] = 0
    hazard_pos[1] = 1  # place hazard to the right of player
    move_player("d")
    assert player_pos == hazard_pos


def test_no_game_over_away_from_hazard():
    """Game should not end when player is not on the hazard."""
    hazard_pos[0] = 4
    hazard_pos[1] = 4  # hazard far away
    move_player("d")
    assert player_pos != hazard_pos


# --- Reset tests ---


def test_reset_moves_player_to_origin():
    """Reset should move the player back to (0, 0)."""
    player_pos[0] = 3
    player_pos[1] = 4
    reset_game()
    assert player_pos == [0, 0]


def test_reset_sets_score_to_zero():
    """Reset should set the score back to 0."""
    game.score = 7
    reset_game()
    assert game.score == 0


def test_reset_spawns_item_on_grid():
    """Reset should place the collectible within the grid."""
    reset_game()
    assert 0 <= item_pos[0] < 5
    assert 0 <= item_pos[1] < 5


def test_reset_spawns_hazard_on_grid():
    """Reset should place the hazard within the grid."""
    reset_game()
    assert 0 <= hazard_pos[0] < 5
    assert 0 <= hazard_pos[1] < 5


def test_reset_hazard_not_on_player():
    """Reset should not place the hazard on the player."""
    reset_game()
    assert hazard_pos != player_pos


def test_reset_hazard_not_on_item():
    """Reset should not place the hazard on the collectible."""
    reset_game()
    assert hazard_pos != item_pos


def test_reset_after_scoring():
    """Reset after scoring should return everything to starting state."""
    game.score = 5
    player_pos[0] = 2
    player_pos[1] = 3
    reset_game()
    assert player_pos == [0, 0]
    assert game.score == 0


# --- Theme tests ---


def test_game_name():
    """Game name should be 'Danger Dragon'."""
    assert GAME_NAME == "Danger Dragon"


def test_story_intro():
    """Story intro should mention dragons and eggs."""
    assert "dragons" in STORY_INTRO.lower()
    assert "eggs" in STORY_INTRO.lower()


def test_win_message():
    """Win message should match the themed text."""
    assert "Wohoo" in WIN_MESSAGE


def test_lose_message():
    """Lose message should match the themed text."""
    assert "Oopsie" in LOSE_MESSAGE
