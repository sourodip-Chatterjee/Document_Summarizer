# Document Summarizer with OpenAI GPT-4

This Python script uses OpenAI's GPT-4 model to generate concise summaries of text documents. It reads a document from a file, sends its content to the GPT-4 API, and prints the summary.

## Features---
- Summarizes any text document using OpenAI's ChatGPT model.
- Reads input from a specified file.
- Includes robust error handling for missing API keys, file issues, and API errors.
- Modular design for easy customization.

---

## Requirements---
- Python 3.7 or higher
- OpenAI Python SDK (`openai`)
- An active OpenAI API key

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/document-summarizer.git
   cd document-summarizer
   ```

2. **Install Dependencies**:
   Create a virtual environment and install the required libraries:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**:
   Add your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your_api_key'  # On Windows: set OPENAI_API_KEY=your_api_key
   ```

---

## Usage

1. Place your document in the same directory as the script (e.g., `example_document.txt`).

2. Run the script:
   ```bash
   python summarize.py
   ```

3. The script will output the original document and its summary.

---

## Dependencies

Install the following Python libraries (also listed in `requirements.txt`):
- `openai` >= 0.27.0

---
