def count_start_end_words(word_list, letter):
    count = 0
    for word in word_list:
        if word[0] == letter and word[-1] == letter:
            count += 1

    return count

word_list = ["ada", "ida", "alta", "ana", "y"]
print(count_start_end_words(word_list, "a"))

