from functools import reduce

strings = ["Hello, World!", "Python is cool", "Functional programming rocks"]


def count_words(strings):

    word_counts = map(lambda x: len(x.split()), strings)

    total_words = reduce(lambda x, y: x + y, word_counts, 0)
    return total_words


result = count_words(strings)
print("Total number of words:", result)
