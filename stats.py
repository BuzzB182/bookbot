def count_words(text):
    return len(text.split())

def count_chars(text):
    char_dict = {} 
    for character in text:
        lower_character = character.lower()
        if lower_character not in char_dict:
            char_dict[lower_character] = 1
        else: 
            char_dict[lower_character] += 1
    return char_dict
