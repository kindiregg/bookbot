from stats import get_num_words
import sys

print(f"SYSTEST: {sys.argv}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = book_text(book_path)
    num_words = get_num_words(text)
    book_low = lowered_string(text)
    # printed console report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document.")
    report(book_low)
    print("--- End report ---")

# takes path of file returns entire file contents
def book_text(path):
    with open(path) as f:
        return f.read()

# gets a count of each character in the book, places in dictionary    
def get_character_dict(book_low):
    char_count = {}
    for c in book_low:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count            

# reports count of each character in report
def report(book_low):
    char_dict = get_character_dict(book_low)
    char_items = list(char_dict.items())
    char_items.sort(key=lambda item: item[1], reverse=True)
    for char, count in char_items:
        if char.isalpha():
            print(f"{char}: {count}")

# sets the book string to lower case            
def lowered_string(book):
    return book.lower()  

main()