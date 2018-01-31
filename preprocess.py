from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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

    with open('experimentaldictionary.txt', 'w', encoding='utf-8') as text_file:
        print(experimentalDict, file=text_file)


tokenization(experimentalDict)
