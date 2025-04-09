# tests/test_feedback_entry.py
import pytest
from feedback_entry import collect_feedback, display_feedback, save_feedback_to_file, load_feedback_from_file

def test_collect_feedback_empty():
    """Tests collect_feedback with no input."""
    # Simulate user input
    inputs = ["done"]
    # Mock the input function
    def mock_input(prompt):
        return inputs.pop(0)

    # Replace the input function with our mock
    original_input = __builtins__.input
    __builtins__.input = mock_input

    feedback = collect_feedback()
    __builtins__.input = original_input #restore input

    assert feedback == []

def test_collect_feedback_with_data():
    """Tests collect_feedback with valid input."""
    inputs = ["Alice", "90", "Bob", "85", "done"]

    def mock_input(prompt):
        return inputs.pop(0)

    original_input = __builtins__.input
    __builtins__.input = mock_input

    feedback = collect_feedback()
    __builtins__.input = original_input

    expected_feedback = [{"name": "Alice", "score": 90.0}, {"name": "Bob", "score": 85.0}]
    assert feedback == expected_feedback

def test_save_and_load_feedback(tmp_path):
    """Tests saving and loading feedback to/from a file."""
    feedback_data = [{"name": "Charlie", "score": 95.0}, {"name": "David", "score": 80.0}]
    test_file = tmp_path / "test_feedback.txt"
    save_feedback_to_file(feedback_data, test_file)
    loaded_feedback = load_feedback_from_file(test_file)
    assert loaded_feedback == feedback_data

def test_load_nonexistent_file():
    """Tests the load_feedback_from_file function with a non-existent file."""
    loaded_feedback = load_feedback_from_file("nonexistent_file.txt")
    assert loaded_feedback == []

# tests/test_score_calculator.py
import pytest
from score_calculator import calculate_average, get_scores_from_input

def test_calculate_average_empty():
    """Tests calculate_average with an empty list."""
    assert calculate_average([]) == 0

def test_calculate_average_valid():
    """Tests calculate_average with a valid list of scores."""
    scores = [80, 90, 85, 95]
    assert calculate_average(scores) == 87.5

def test_get_scores_from_input_empty():
    """Tests get_scores_from_input with no input."""
    inputs = ["done"]

    def mock_input(prompt):
        return inputs.pop(0)

    original_input = __builtins__.input
    __builtins__.input = mock_input

    scores = get_scores_from_input()
    __builtins__.input = original_input

    assert scores == []

def test_get_scores_from_input_valid():
    """Tests get_scores_from_input with valid input."""
    inputs = ["80", "90", "85", "95", "done"]

    def mock_input(prompt):
        return inputs.pop(0)

    original_input = __builtins__.input
    __builtins__.input = mock_input

    scores = get_scores_from_input()
    __builtins__.input = original_input

    assert scores == [80.0, 90.0, 85.0, 95.0]

def test_get_scores_from_input_invalid():
    """Tests get_scores_from_input with invalid input."""
    inputs = ["80", "abc", "90", "done"]

    def mock_input(prompt):
        return inputs.pop(0)

    original_input = __builtins__.input
    __builtins__.input = mock_input

    scores = get_scores_from_input()
    __builtins__.input = original_input

    assert scores == [80.0, 90.0]