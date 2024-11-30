def letter_value(letter_list, letter):
    for letter in letter_list:
        if letter[0] == letter:
            return letter[1:]
    return []
