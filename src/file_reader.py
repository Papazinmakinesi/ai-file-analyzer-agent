def read_text_file(file_path):
    """
    Reads a .txt file and returns its content as a string.
    """

    if not file_path.endswith(".txt"):
        raise ValueError("Only .txt files are supported.")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        if not content.strip():
            raise ValueError("The file is empty.")

        return content

    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")