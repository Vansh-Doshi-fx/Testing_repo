import string

def clean_sentence(sentence):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.translate(translator)
    cleaned_sentence = ' '.join(cleaned_sentence.split())
    return cleaned_sentence