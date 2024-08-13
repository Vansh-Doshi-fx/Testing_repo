```python
from python_test.patterns_print import *
from phone_validation import is_valid_phone_number

print("hello World!")
printFirstTenNum()
print()
printStars(5)

def calculate_average_word_length(sentence:str):
    words = sentence.split(" ")
    if not words:
        return 0
    
    total_length = sum(len(word) for word in words)
    return total_length / len(words)
```