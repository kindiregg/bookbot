book_path = "books/frankenstein.txt"
def main():
    text = book_text(book_path)
    word_count = get_word_count(text)
    # prints word count of book to check everything was printed
    print(f"Contains {word_count} words.")

# takes file contents returns count
def get_word_count(booktext):
    return len(booktext.split())


# takes path of file returns entire file contents
def book_text(path):
    with open(path) as f:
        return f.read()
        
main()