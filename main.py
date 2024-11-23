book_path = "books/frankenstein.txt"
def main():
    text = book_text(book_path)
    word_count = get_word_count(text)
    book_low = lowered_string(text)
    # printed console report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the doument.")
    print(get_character_dict(book_low))
    report(book_low)
    print("--- End report ---")

# takes file contents returns count
def get_word_count(booktext):
    return len(booktext.split())


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
            print(f"The '{char}' characer was found {count} times")

# sets the book string to lower case            
def lowered_string(book):
    return book.lower()  

main()