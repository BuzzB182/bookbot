from stats import count_words, count_chars, create_sorted

def get_book_text(filepath):
    # open the file and read it -> get content of file as string
    with open(filepath) as f:
        return f.read()

def main():
    book = "./books/frankenstein.txt"
    text = get_book_text(book)
    num_words = count_words(text)
    character_dict = count_chars(text)
    sorted_dict_list = create_sorted(character_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for sorted_dict in sorted_dict_list:
        if sorted_dict['char'].isalpha():
            print(f"{sorted_dict['char']}: {sorted_dict['num']}")
    
    print("============= END ===============")


if __name__== "__main__":
    main()