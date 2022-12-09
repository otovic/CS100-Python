def get_longest_word(words):
    longest_word = ""
    longest_word_len = 0
    for word in words:
        if len(word) > longest_word_len:
            longest_word = word
            longest_word_len = len(word)
    return longest_word, longest_word_len

words = ["Hello", "world", "this", "is", "a", "list", "of", "words"]
longest_word, length = get_longest_word(words)
print(f"The longest word is {longest_word} with length {length}") # "The longest word is 'world' with length 5"