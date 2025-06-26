def shuffle(sentence):
    words = sentence.split()

    wordlist = ["word"] *len(words)
    for word in words:
        place = int(word[-1]) - 1
        correct_word = word[:-1]
        wordlist[place] = correct_word
    return " ".join(wordlist)

print(shuffle("sadik2 ali3 salahudin1"))