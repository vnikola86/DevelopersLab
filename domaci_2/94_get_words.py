def get_words_with_even_length_and_without_char(sentence, char):
    words = sentence.split()
    result_words = [word for word in words if len(word) % 2 == 0 and char not in word]
    return result_words

sentence_input = input("Enter a sentence: ")
char_input = input("Enter a character: ")

result = get_words_with_even_length_and_without_char(sentence_input, char_input)
print(result)
