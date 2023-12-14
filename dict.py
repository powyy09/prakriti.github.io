from nltk.corpus import wordnet

def get_word_meanings(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return "Meaning not found for this word."
user_word = input("Enter a word to get its meaning: ").lower()
meaning = get_word_meanings(user_word)
print(f"The meaning of '{user_word}' is: {meaning}")
