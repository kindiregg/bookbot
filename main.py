book_path = "books/frankenstein.txt"
def main():
    text = book_text(book_path)
    word_count = get_word_count(text)
    book_low = lowered_string(text)
    # prints word count of book to check everything was printed
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print(f"Contains {word_count} words.")
    for char in get_character_dict(book_low):

        print(f"")

# takes file contents returns count
def get_word_count(booktext):
    return len(booktext.split())


# takes path of file returns entire file contents
def book_text(path):
    with open(path) as f:
        return f.read()
    
def get_character_dict(book_low):
    char_count = {}
    for c in book_low:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count            
            
def lowered_string(book):
    return book.lower()  
main()