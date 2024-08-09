from patterns_print import *
from generate import clean_sentence

print("hello World!")
printFirstTenNum()
print()
printStars(5)

def calculate_average_word_length(sentence: str):
    """Calculates the average word length in a sentence, ignoring punctuation."""
    cleaned_sentence = clean_sentence(sentence)
    words = cleaned_sentence.split(" ")
    if not words:  # Handle empty string or no words after cleaning
        return 0
    
    total_length = sum(len(word) for word in words)
    return total_length / len(words)