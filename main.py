from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book = "./books/frankenstein.txt"
    num_words = count_words(get_book_text(book))
    print(f"Found {num_words} total words")

if __name__== "__main__":
    main()