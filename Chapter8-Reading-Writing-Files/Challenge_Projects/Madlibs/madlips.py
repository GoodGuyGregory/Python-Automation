import re


def main():
    madlibs = open('madlib.txt', 'r')
    # write to new
    finishedMadlib = open('finishedMadlib.txt', 'w')

    # read the words:
    madlib = madlibs.readline()

    #  split into chunks
    words = madlib.split(' ')

    replacements = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']
    for i in range(len(words)):
        if words[i].isupper() and len(words[i]) >= 4 or words[i] in replacements:
            # creates a clean substring by removing punctuations
            cleanWord = re.sub(r'[^\w\s]', '', words[i])
            if cleanWord[0].lower() == 'a':
                userWord = input("Enter an {}: " .format(cleanWord.lower()))
                # swap the word
                words[i] = userWord

                finishedMadlib.write(str(words[i]) + " ")

            else:
                userWord = input("Enter a {}: " .format(cleanWord.lower()))
                words[i] = userWord

                finishedMadlib.write(str(words[i]) + " ")
        else:
            finishedMadlib.write(str(words[i]) + " ")
    finishedMadlib.close()
    madlibs.close()


main()
