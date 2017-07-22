from random import randint
import string


def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"


def random_noun():
    random_num = randint(0, 1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

#it is a NOUN or VERB
def word_transformer(word):
    if word == '':
        return ''
    wordNew = word.replace('VERB', random_verb())
    wordNew = wordNew.replace('NOUN', random_noun())
    if wordNew == word:
        return word[0]
    else:
        return wordNew

def word_transformer(word):
    if word == '':
        return ''
    wordNew = word.replace('VERB', random_verb())
    wordNew = wordNew.replace('NOUN', random_noun())
    if wordNew == word:
        return word[0]
    else:
        return wordNew

s = 'it is a NOUN or VERB'
print word_transformer(s)
