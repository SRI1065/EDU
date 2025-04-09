def calculate_top_scores(feedback_data, top_n=5):
    """Calculates the top N scores from the feedback data."""
    scores = [item['score'] for item in feedback_data if 'score' in item]
    scores.sort(reverse=True)
    return scores[:top_n]

def calculate_grade_counts(feedback_data):
    """Calculates the counts of students in each grade category."""
    grade_counts = {}
    for item in feedback_data:
        if 'grade' in item:
            grade = item['grade']
            grade_counts[grade] = grade_counts.get(grade, 0) + 1
    return grade_counts

# Example usage (you'll need to adapt this to how your feedback data is stored):
if __name__ == "__main__":
    feedback_data = [
        {'name': 'Alice', 'score': 95, 'grade': 'A'},
        {'name': 'Bob', 'score': 88, 'grade': 'B'},
        {'name': 'Charlie', 'score': 92, 'grade': 'A'},
        {'name': 'David', 'score': 78, 'grade': 'C'},
        {'name':'Eve', 'score': 99, 'grade': 'A'},
        {'name':'Frank', 'score': 60, 'grade': 'D'}
    ]

    top_scores = calculate_top_scores(feedback_data)
    print("Top Scores:", top_scores)

    grade_counts = calculate_grade_counts(feedback_data)
    print("Grade Counts:", grade_counts)