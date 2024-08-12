from python_test.patterns_print import *

print("hello World!")
printFirstTenNum()
print()
printStars(5)

def calculate_average_word_length(sentence:str):
    """Calculates the average word length in a sentence, ignoring punctuation."""
    words = sentence.split(" ")
    if not words:  # Handle empty string or no words after cleaning
        return 0
    
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def get_fibonacci_list(n):
    a, b = 0, 1
    fibonacci_list = []
    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list