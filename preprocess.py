import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

referenceDict = {}
experimentalDict = {}
sentenceKey = 1

extractedTxt = open('outputextracted.txt', 'r', encoding='utf-8')
extractedStr = extractedTxt.read()
extractedList = extractedStr.split('.')

for sentence in extractedList:
    referenceSentence = sentence.replace('\n', ' ')
    experimentalSentence = sentence.lower().replace('\n', ' ')
    referenceDict[sentenceKey] = referenceSentence
    experimentalDict[sentenceKey] = experimentalSentence
    sentenceKey += 1

with open('referencedictionary.txt', 'w', encoding='utf-8') as text_file:
    print(referenceDict, file=text_file)

with open('experimentaldictionary.txt', 'w', encoding='utf-8') as text_file:
    print(experimentalDict, file=text_file)


def tokenization(exDict):
    for sentenceKey, experimentalSentence in exDict.items():
        exSentTokens = word_tokenize(experimentalSentence)
        exDict[sentenceKey] = exSentTokens

    stopwordsRemoval(exDict)


def stopwordsRemoval(exDict):
    stopWords = set(stopwords.words('english'))

    for sentenceKey, experimentalSentence in exDict.items():
        tempSentence = []
        for word in experimentalSentence:
            if word not in stopWords:
                tempSentence.append(word)

        exDict[sentenceKey] = tempSentence

    specialCharRemoval(exDict)


def specialCharRemoval(exDict):
    for sentenceKey, experimentalSentence in exDict.items():
        tempSentence = []
        for word in experimentalSentence:
            if word.isalpha() or word.isnumeric():
                tempSentence.append(word)

        exDict[sentenceKey] = tempSentence

    posTagging(exDict)


def posTagging(exDict):
    for sentenceKey, experimentalSentence in exDict.items():
        tempSentence = nltk.pos_tag(experimentalSentence)
        exDict[sentenceKey] = tempSentence

    lemmatization(exDict)


def lemmatization(exDict):
    wordLemmatizer = WordNetLemmatizer()

    for sentenceKey, experimentalSentence in exDict.items():
        tempSentence = []
        for word in experimentalSentence:
            pos = ''
            wordTuple = [wt for wt in word]
            wtToList = list(wordTuple)
            if wtToList[1].startswith('N'):
                pos = 'n'
            elif wtToList[1].startswith('J'):
                pos = 'a'
            elif wtToList[1].startswith('V'):
                pos = 'v'
            elif wtToList[1].startswith('R'):
                pos = 'r'
            else:
                pos = 'n'
            wtToList[0] = wordLemmatizer.lemmatize(wtToList[0], pos)
            wlToTuple = tuple(wtToList)
            tempSentence.append(wlToTuple)

        exDict[sentenceKey] = tempSentence

    with open('experimentaldictionary.txt', 'w', encoding='utf-8') as text_file:
        print(exDict, file=text_file)


tokenization(experimentalDict)
