from src.file_reader import read_text_file
from src.text_processor import clean_text
from src.ai_analyzer import analyze_text


def run_agent():
    print("=== AI File Analyzer Agent ===")

    choice = input("Enter '1' to input text or '2' to read from file: ")

    try:
        if choice == "1":
            user_input = input("Enter your text:\n")
            text = clean_text(user_input)

        elif choice == "2":
            file_path = input("Enter file path (e.g., data/sample.txt): ")
            file_content = read_text_file(file_path)
            text = clean_text(file_content)

        else:
            print("Invalid choice.")
            return

        print("\nProcessing...\n")
        result = analyze_text(text)
        print(result)

    except (ValueError, TypeError, FileNotFoundError) as e:
        print(f"\nError: {e}")