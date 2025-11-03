from stats import count_words, count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book = "./books/frankenstein.txt"
    text = get_book_text(book)
    num_words = count_words(text)
    print(f"Found {num_words} total words\n")
    character_dict = count_chars(text)
    print(character_dict)

if __name__== "__main__":
    main()