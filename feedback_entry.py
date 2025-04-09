"""
feedback_entry.py: Script to collect student feedback (e.g., names, scores).
"""

def collect_feedback():
    """Collects student feedback and returns a list of dictionaries."""

    feedback_list = []

    while True:
        student_name = input("Enter student name (or 'done' to finish): ")
        if student_name.lower() == 'done':
            break

        try:
            score = float(input("Enter student score: "))
        except ValueError:
            print("Invalid score. Please enter a number.")
            continue  # Skip to the next iteration of the loop

        feedback_list.append({"name": student_name, "score": score})

    return feedback_list

def display_feedback(feedback_data):
    """Displays the collected student feedback."""

    if not feedback_data:
        print("No feedback collected.")
        return

    print("\nStudent Feedback:")
    print("-" * 20)
    for entry in feedback_data:
        print(f"Name: {entry['name']}, Score: {entry['score']}")

def save_feedback_to_file(feedback_data, filename="student_feedback.txt"):
    """Saves the feedback data to a text file."""

    try:
        with open(filename, "w") as file:
            for entry in feedback_data:
                file.write(f"{entry['name']},{entry['score']}\n")
        print(f"Feedback saved to {filename}")
    except Exception as e:
        print(f"Error saving feedback to file: {e}")

def load_feedback_from_file(filename="student_feedback.txt"):
    """Loads feedback data from a text file."""
    feedback_list = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                feedback_list.append({"name": name, "score": float(score)})
        print(f"Feedback loaded from {filename}")
        return feedback_list
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as e:
        print(f"Error loading feedback from file: {e}")
        return []

def main():
    """Main function to run the feedback collection and display."""
    load_previous = input("Load previous data? (yes/no): ").lower()
    if load_previous == 'yes':
        feedback = load_feedback_from_file()
    else:
        feedback = collect_feedback()

    display_feedback(feedback)

    save_to_file = input("Save feedback to file? (yes/no): ").lower()
    if save_to_file == 'yes':
        save_feedback_to_file(feedback)

if __name__ == "__main__":
    main()