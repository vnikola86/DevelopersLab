import re

# Function to get words ending with a specified letter in a sentence
def get_words_ends_with_letter(text, letter):
    # Split the text into sentences using regular expressions
    sentences = re.split(r'[.!?]', text)
    result = []

    for sentence in sentences:
        # Split the sentence into words
        words = sentence.split()
        count = 0
        sentence_result = []

        for word in words:
            # Check if the word ends with the specified letter
            if word.endswith(letter):
                sentence_result.append(word)
                count += 1

        # Add the tuple to the result list only if there are words ending with the specified letter in the sentence
        if sentence_result:
            result.append((sentence_result, count))

    return result

# Test the function
text = "Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences."
letter = "s"
result = get_words_ends_with_letter(text, letter)
print(result)
