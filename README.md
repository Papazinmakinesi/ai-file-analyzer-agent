# AI File Analyzer Agent

## Project Description

AI File Analyzer Agent is a small Python project that analyzes text input and `.txt` files. The main purpose of the project is to help users understand a text document faster by returning a short summary, important keywords, and a basic content category.

The project is built as a command-line application. It follows a simple single-agent workflow: the agent receives the input, calls the required tools, and returns the result to the user.

## Features

- Accepts direct text input
- Reads text from `.txt` files
- Cleans the input before analysis
- Generates a short summary
- Extracts important keywords
- Classifies the text as educational, technical, or general
- Uses a local fallback analyzer if the external API is not available

## Project Structure


ai-file-analyzer-agent/
├── data/
│   └── sample.txt
├── docs/
│   └── journal.md
├── src/
│   ├── __init__.py
│   ├── agent.py
│   ├── ai_analyzer.py
│   ├── file_reader.py
│   └── text_processor.py
├── tests/
│   ├── test_file_reader.py
│   └── test_text_processor.py
├── .env
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt

## How It Works

The application starts from main.py. The user chooses whether to enter text manually or read text from a file.

If file input is selected, the file reader loads the content from a .txt file. The text processor removes unnecessary spaces and empty lines. Then the analyzer module processes the cleaned text and returns the final output.

The final output contains:

summary
keywords
classification

## Installation

Clone the repository: git clone https://github.com/Papazinmakinesi/ai-file-analyzer-agent.git

Go to the project folder: cd ai-file-analyzer-agent

Install the required dependencies: pip install -r requirements.txt

## Configuration

The project includes an .env file for configuration.
If a valid OpenAI API key is available, the system can use the external AI model for text analysis.

If the API key is missing, invalid, or has no available quota, the project still runs with the local fallback analyzer. This was added so the application can still be tested and demonstrated.

## Running the Application

Start the program with: python main.py
Then choose one of the options shown in the terminal:
1 - enter text manually
2 - read text from file
For file input, an example file is available:
data/sample.txt

## Running Tests

The project uses pytest for testing.

Run the tests with: python -m pytest
The tests check file reading, text cleaning, invalid file extensions, missing files, empty input, and invalid input types.

## Project Journal
The project journal is stored in: docs/journal.md
It includes the work completed for Step 1, Step 2, Step 3, and the final submission explanation.

## Deployment

The project is prepared as a local command-line Python application. It does not need a web server or external hosting to run.

A user only needs to install the dependencies, check the configuration file, and run:

python main.py
Author

Ekin Taner
231ADB277