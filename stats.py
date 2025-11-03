def count_words(text):
    # split text by default delimiter " " into words list and return length of that list, which equals to the word count
    return len(text.split())

def count_chars(text):
    # Create empty dictionary
    char_dict = {} 
    # Iterate over each Character in the booktext
    for character in text:
        # Make each character lowercase
        lower_character = character.lower()
        # Check if lower character is already in dictionary as key. 
        # If not, create it and set value to 1
        if lower_character not in char_dict:
            char_dict[lower_character] = 1
        # If key already present in dictionary, add 1 to its value. This way, it counts the chars.
        else: 
            char_dict[lower_character] += 1
    return char_dict

def create_sorted(letter_dict):
    dict_list = []
    # Convert the dictionary to a list of dictionaries: for each key-value pair in the whole dictionary, create a new dictionary and append it to the list
    for key in letter_dict:
        temp_dict = {}
        value = letter_dict[key]
        #temp_dict[key] = value
        temp_dict["char"] = key
        temp_dict["num"] = value
        dict_list.append(temp_dict)
    
    # Sortiere das dictionary mit Hilfe der sort_on helper function
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def sort_on(single_dict):
    return single_dict["num"]

