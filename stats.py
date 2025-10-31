
def get_book_text(filepath: str) -> str:
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            # .read() pulls all content from the file into one string variable
            text = file.read()
            return text
    except FileNotFoundError:
        print(f"Error: The file at '{filepath}' was not found.")
        return ""  # Return an empty string or you could raise the error
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def countWords(filepath):
    text = get_book_text(filepath)
    splitted = text.split()
    counted = len(splitted)

    return counted;

def wordsList(filepath):
    text = get_book_text(filepath)
    splitted = text.split()

    return splitted;
