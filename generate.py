import requests
from pysyllables import get_syllable_count
from random import randrange, choice

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
haiku_syllables = [5, 7, 5]

def decode(byte):
    return byte.decode()

def get_words():
    response = requests.get(word_site)
    words = response.content.splitlines()
    words = list(map(decode, words))
    return words

def build_dict(words):
    syllable_dict = {}
    for word in words:
        syllables = get_syllable_count(word)
        if syllables:
            if syllables not in syllable_dict.keys():
                syllable_dict[syllables] = []
            syllable_dict[syllables].append(word)
    return syllable_dict

def build_line(syllable_dict, syllables):
    line = ""
    total_syllables = 0
    diff = syllables - total_syllables
    while diff > 0:
        #print(total_syllables, syllables)
        i = randrange(1, diff+1)
        random_word = choice(syllable_dict[i])
        #print("{} syllables: {}".format(i, random_word))
        line += random_word
        line += " "
        total_syllables += i
        diff = syllables - total_syllables
    return line 

def main():
    words = get_words()
    syllable_dict = build_dict(words)
    #print(syllable_dict)
    #print("here's your custom haiku!:")
    for i in haiku_syllables:
        print(build_line(syllable_dict, i))

if __name__=='__main__':
    main()
