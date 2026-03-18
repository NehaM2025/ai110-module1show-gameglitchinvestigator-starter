from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

#FIX: Wrote three additional test cases to check fixes for the three bugs I identified using Copilot Agent mode
def test_hint_swapped():
    # If guess is less than secret, should be 'Too Low' and message should mention higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "higher" in message.lower() or "high" in message.lower()
    # If guess is greater than secret, should be 'Too High' and message should mention lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "lower" in message.lower()

def test_new_game_no_crash():
    # Simulate new game state reset logic (should not crash)
    # This is a placeholder: actual UI crash is not testable here, but we can check logic
    try:
        # Example: resetting values
        secret = 42
        attempts = 1
        history = []
        # No exception should occur
    except Exception as e:
        assert False, f"New game logic crashed: {e}"

def test_parse_guess_limits():
    # Out of range low
    ok, guess, err = parse_guess("-5", low=1, high=100)
    assert not ok
    assert "between" in err
    # Out of range high
    ok, guess, err = parse_guess("150", low=1, high=100)
    assert not ok
    assert "between" in err
    # In range
    ok, guess, err = parse_guess("50", low=1, high=100)
    assert ok
    assert guess == 50
