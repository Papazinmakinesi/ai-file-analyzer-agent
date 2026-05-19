\# AI File Analyzer Agent



\## Project Description

This project is an AI-based Python application that analyzes text input and generates structured outputs. The system can process both direct user input and `.txt` files. It provides a summary, extracts keywords, and classifies the content.



The system is designed as a single intelligent agent that coordinates multiple tools during execution.



\---



\## Features

\- Text input and file input support

\- Automatic text summarization

\- Keyword extraction

\- Content classification (educational, technical, general)

\- Fallback analysis when AI API is unavailable

\- Modular and structured design



\---



\## System Architecture

The system follows an agent-based architecture:



\- Agent (main controller)

\- File Reader Module

\- Text Processing Module

\- AI Analyzer Module (with fallback support)



\---



\## Installation



1\. Clone the repository:

git clone https://github.com/Papazinmakinesi/ai-file-analyzer-agent.git



2\. Navigate to the project folder:

cd ai-file-analyzer-agent



3\. Install dependencies:

pip install -r requirements.txt



\---



\## Configuration



Create a `.env` file in the root directory and add your OpenAI API key:

OPENAI\_API\_KEY=your\_api\_key\_here



\---



\## Usage



Run the application:

python main.py



Follow the instructions in the terminal:

\- Enter `1` for manual text input

\- Enter `2` for file input



\---



\## Example Output

Summary:

...



Keywords:

...



Classification:

...



\---



\## Testing



Run tests using:

pytest



\---



\## Deployment



The system can be deployed as a local command-line application. It is designed to be easily extendable into a web service or API-based system.



\---



\## Technologies Used

\- Python

\- OpenAI API

\- dotenv

\- pytest



\---



\## Notes

If the OpenAI API is unavailable or quota is exceeded, the system automatically switches to a fallback analyzer to ensure continuous functionality.



\---



\## Author
Ekin Taner


