"""
score_calculator.py: Script to compute average score from a list of scores.
"""

def calculate_average(scores):
    """Calculates the average of a list of scores.

    Args:
        scores: A list of numerical scores.

    Returns:
        The average score, or 0 if the list is empty.
    """
    if not scores:
        return 0  # Return 0 for an empty list

    total = sum(scores)
    average = total / len(scores)
    return average

def get_scores_from_input():
    """Gets a list of scores from user input."""

    scores = []
    while True:
        try:
            score = input("Enter a score (or 'done' to finish): ")
            if score.lower() == 'done':
                break
            scores.append(float(score))
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return scores

def main():
    """Main function to run the score calculator."""
    scores = get_scores_from_input()
    average = calculate_average(scores)
    print(f"Scores: {scores}")
    print(f"Average score: {average:.2f}") #format to 2 decimal places.

if __name__ == "__main__":
    main()