from python_test.patterns_print import *

print("hello World!")
printFirstTenNum()
print()
printStars(5)


"""calculate_average_word_length -> uncleaned sentence, might calculate wrong average world length"""
def calculate_average_word_length(sentence:str):
    """Calculates the average word length in a sentence, ignoring punctuation."""
    words = sentence.split(" ")
    if not words:  # Handle empty string or no words after cleaning
        return 0
    
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def validate_phone_number(phone_number: str) -> bool:
    """Validates a phone number format."""
    import re
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    return bool(pattern.match(phone_number))