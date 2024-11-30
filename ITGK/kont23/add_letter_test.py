def add_letter_test(letter_list, letter, score):
    letter = letter_value(letter_list)
    if letter == []:
        letter_list.append([letter,score])
    else:
        for letter in letter_list:
            if letter[0] == letter:
                letter.append(score)
    return letter_list
