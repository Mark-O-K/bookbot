import sys
from stats import get_num_words, get_num_characters, get_characters_list

def main():
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    characters = get_num_characters(text)
    character_list = get_characters_list(characters)
    print_report(book_path, words, character_list)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, words, character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for pair in character_list:
        if not pair["char"]:
            continue
        print(f"{pair['char']}: {pair['num']}")
    
    print("============= END ===============")
main()