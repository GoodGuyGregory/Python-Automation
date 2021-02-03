import re


def main():
    madlibs = open('madlib.txt', 'r')

    # read the words:
    madlib = madlibs.readline()

    #  split into chunks
    words = madlib.split(' ')

    replacements = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']
    for i in range(len(words)):
        if words[i].isupper() and len(words[i]) >= 4 or words[i] in replacements:
            # creates a clean substring by removing punctuations
            cleanWord = re.sub(r'[^\w\s]', '', words[i])
            print(cleanWord)


main()
