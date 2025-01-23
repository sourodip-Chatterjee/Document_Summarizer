import openai
import os

# Set up OpenAI API key
def setup_openai_api():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OpenAI API key is missing! Please set it in the environment variables.")

# Function to summarize a document
def summarize_document(content, max_tokens=150):
    """
    Summarizes the given document using OpenAI's ChatGPT model.

    Parameters:
        content (str): The text content to summarize.
        max_tokens (int): The maximum token length of the summary.

    Returns:
        str: The summary of the document.
    """
    try:
        # Ensure max_tokens is within GPT model's constraints
        if max_tokens <= 0 or max_tokens > 4000:
            raise ValueError("max_tokens must be between 1 and 4000 for GPT-4.")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes documents."},
                {"role": "user", "content": f"Summarize the following document:\n\n{content}"}
            ],
            max_tokens=max_tokens,
            temperature=0.5
        )
        summary = response['choices'][0]['message']['content']
        return summary.strip()
    except openai.error.OpenAIError as e:
        print(f"Error while communicating with OpenAI: {e}")
        return None
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Main script
def main():
    setup_openai_api()

    # Example document
    document_path = "example_document.txt"  # Replace with your document's path

    if not os.path.exists(document_path):
        print(f"Error: The file '{document_path}' does not exist.")
        return

    try:
        with open(document_path, 'r', encoding='utf-8') as file:
            document_content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    print("Original Document:\n", document_content)
    print("\nGenerating summary...\n")
    
    summary = summarize_document(document_content, max_tokens=150)
    if summary:
        print("Document Summary:\n", summary)
    else:
        print("Failed to generate a summary.")

# Entry point
if __name__ == "__main__":
    main()
