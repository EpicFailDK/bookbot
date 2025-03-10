from stats import get_num_words, get_num_symbols, get_sorted_list
import sys
import os # Import the os module for path checking


def main():
    # Step 1: Check if the user provided exactly one extra argument
    if len(sys.argv) != 2:  # Two entries: the script name and the book path.
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Step 2: Get the book path from sys.argv
    book_path = sys.argv[1]

    # Step 3: Check if the file exists
    if not os.path.exists(book_path):
        print(f"Error: The file '{book_path}' does not exist.")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    

    print(f"Book path provided: {book_path}")

    # Continue your existing logic with the dynamically set book_path
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_symbols = get_num_symbols(text)
    sorted_list = get_sorted_list(num_symbols)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()