def printFirstTenNum():
    for i in range(1,11):
        print(i,end=" ")
        
def printStars(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()

from generate import clean_sentence

def average_word_length(sentence):
    cleaned_sentence = clean_sentence(sentence)
    words = cleaned_sentence.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)