def clean_text(text):
    """
    Cleans user input text by removing extra spaces and empty lines.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    cleaned_lines = [line.strip() for line in text.splitlines() if line.strip()]
    cleaned_text = " ".join(cleaned_lines)

    if not cleaned_text:
        raise ValueError("Input text cannot be empty.")

    return cleaned_text