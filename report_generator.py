# src/report_generator.py

def export_feedback_to_txt(feedback_data, filename="feedback_report.txt"):
    """
    Exports feedback data to a text file.

    :param feedback_data: List of dictionaries containing feedback (e.g., [{"name": "John", "score": 8}, ...])
    :param filename: Output .txt file name
    """
    try:
        with open(filename, 'w') as file:
            file.write("Student Feedback Report\n")
            file.write("=" * 30 + "\n\n")
            for entry in feedback_data:
                name = entry.get("name", "Unknown")
                score = entry.get("score", "N/A")
                file.write(f"Name: {name}\n")
                file.write(f"Score: {score}\n")
                file.write("-" * 20 + "\n")
        print(f"Feedback successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting feedback: {e}")
