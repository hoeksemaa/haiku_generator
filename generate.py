import requests
from pysyllables import get_syllable_count

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"


def decode(byte):
    return byte.decode()

def build_dict(words):
    syllable_dict = {}
    for word in words:
        syllables = get_syllable_count(word)
        if syllables:
            if syllables not in syllable_dict.keys():
                syllable_dict[syllables] = []
            syllable_dict[syllables].append(word)
    return syllable_dict

def main():
    response = requests.get(word_site)
    words = response.content.splitlines()
    words = list(map(decode, words))
    
    syllable_dict = build_dict(words)
    
    for key in syllable_dict.keys():
        print("{}: {} words".format(key, len(syllable_dict[key])))

if __name__=='__main__':
    main()
