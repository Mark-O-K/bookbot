def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    characters = {}
    for character in text:
        lower_character = character.lower()
        if lower_character in characters:
            characters[lower_character] += 1
        else:
            characters[lower_character] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def get_characters_list(dictionary):
    character_list = []
    for character in dictionary:
        temp_dictionary = {}
        if character.isalpha():
            temp_dictionary = {"char": character, "num": dictionary[character]}
            character_list.append(temp_dictionary)
    character_list.sort(reverse=True, key=sort_on)
    return character_list
        