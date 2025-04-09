import pytest
from src.feedback_summary import calculate_top_scores, calculate_grade_counts

def test_calculate_top_scores():
    feedback_data = [
        {'name': 'Alice', 'score': 95},
        {'name': 'Bob', 'score': 88},
        {'name': 'Charlie', 'score': 92},
        {'name': 'David', 'score': 78},
        {'name': 'Eve', 'score': 99}
    ]
    top_scores = calculate_top_scores(feedback_data, top_n=3)
    assert top_scores == [99, 95, 92]

def test_calculate_grade_counts():
    feedback_data = [
        {'name': 'Alice', 'grade': 'A'},
        {'name': 'Bob', 'grade': 'B'},
        {'name': 'Charlie', 'grade': 'A'},
        {'name': 'David', 'grade': 'C'}
    ]
    grade_counts = calculate_grade_counts(feedback_data)
    assert grade_counts == {'A': 2, 'B': 1, 'C': 1}

def test_calculate_top_scores_empty():
    feedback_data = []
    top_scores = calculate_top_scores(feedback_data)
    assert top_scores == []

def test_calculate_grade_counts_empty():
    feedback_data = []
    grade_counts = calculate_grade_counts(feedback_data)
    assert grade_counts == {}

def test_calculate_grade_counts_no_grade():
    feedback_data = [{'name':'John', 'score':100}]
    grade_counts = calculate_grade_counts(feedback_data)
    assert grade_counts == {}

def test_calculate_top_scores_less_than_top_n():
    feedback_data = [
        {'name': 'Alice', 'score': 95},
        {'name': 'Bob', 'score': 88}
    ]
    top_scores = calculate_top_scores(feedback_data, top_n=3)
    assert top_scores == [95, 88]

def test_calculate_grade_counts_mixed_data():
    feedback_data = [
        {'name': 'Alice', 'grade': 'A', 'score': 90},
        {'name': 'Bob', 'grade': 'B'},
        {'name': 'Charlie', 'grade': 'A'},
        {'name': 'David', 'score': 70}
    ]
    grade_counts = calculate_grade_counts(feedback_data)
    assert grade_counts == {'A': 2, 'B': 1}