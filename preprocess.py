import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def preprocessInitialize(outputExtracted):
    referenceDict = {}
    experimentalDict = {}
    sentenceKey = 1
    newTitle = []
    newTitle2 = []
    originalTitle = []
    newTitleStr = ''
    fullTitleStr = ''

    extractedTxt = open(outputExtracted, 'r', encoding='utf-8')
    extractedStr = extractedTxt.read()
    extractedList = extractedStr.split('. ')

    with open('output.txt', 'r', encoding='utf-8') as rawOutput:
        title = [next(rawOutput) for x in range(3)]

    for word in title:
        newTitle.append(word.lower().replace('\n', ' '))
        originalTitle.append(word.replace('\n', ' '))

    for word2 in newTitle:
        if(word2 != ' '):
            newTitleStr += word2

    for word3 in originalTitle:
        if(word3 != ' '):
            fullTitleStr += word3

    newTitle2 = newTitleStr.split()
    lastIndex = len(extractedList) - 1

    for sentence in extractedList:
        if(sentence != extractedList[lastIndex]):
            sentenceTokenize = word_tokenize(sentence)
            if(len(sentenceTokenize) >= 10 and len(sentenceTokenize) <= 50):
                sentence = re.sub('\d+,|\[|\d+]|\[d+]|[d+],', '', sentence)
                sentence = sentence.rstrip()
                referenceSentence = sentence.replace('\n', ' ')
                experimentalSentence = sentence.lower().replace('\n', ' ')
                referenceDict[sentenceKey] = referenceSentence
                experimentalDict[sentenceKey] = experimentalSentence
                sentenceKey += 1

    with open('fulltitle.txt', 'w', encoding='utf-8') as text_file:
        print(fullTitleStr, file=text_file)

    with open('referencedictionary.txt', 'w', encoding='utf-8') as text_file:
        print(referenceDict, file=text_file)

    with open('experimentaldictionary.txt', 'w', encoding='utf-8') as text_file:
        print(experimentalDict, file=text_file)

    tokenization(experimentalDict, newTitle2)


def tokenization(exDict, newTitle2):
    for sentenceKey, experimentalSentence in exDict.items():
        exSentTokens = word_tokenize(experimentalSentence)
        exDict[sentenceKey] = exSentTokens

    stopwordsRemoval(exDict, newTitle2)


def stopwordsRemoval(exDict, newTitle2):
    stopWords = set(stopwords.words('english'))
    tempTitle = []

    for word in newTitle2:
        if word not in stopWords:
            tempTitle.append(word)
    newTitle2 = tempTitle

    for sentenceKey, experimentalSentence in exDict.items():
        tempSentence = []
        for word in experimentalSentence:
            if word not in stopWords:
                tempSentence.append(word)

        exDict[sentenceKey] = tempSentence

    specialCharRemoval(exDict, newTitle2)


def specialCharRemoval(exDict, newTitle2):
    tempTitle = []
    for word in newTitle2:
        if word.isalpha():
            tempTitle.append(word)
    newTitle2 = tempTitle

    for sentenceKey, experimentalSentence in exDict.items():
        tempSentence = []
        for word in experimentalSentence:
            if word.isalpha() or word.isnumeric():
                tempSentence.append(word)

        exDict[sentenceKey] = tempSentence

    posTagging(exDict, newTitle2)


def posTagging(exDict, newTitle2):
    tempTitle = nltk.pos_tag(newTitle2)
    newTitle2 = tempTitle

    for sentenceKey, experimentalSentence in exDict.items():
        tempSentence = nltk.pos_tag(experimentalSentence)
        exDict[sentenceKey] = tempSentence

    lemmatization(exDict, newTitle2)


def lemmatization(exDict, newTitle2):
    wordLemmatizer = WordNetLemmatizer()
    tempTitle = []

    for word1 in newTitle2:
        pos1 = ''
        titleWordL = list(word1)
        if titleWordL[1].startswith('N'):
            pos1 = 'n'
        elif titleWordL[1].startswith('J'):
            pos1 = 'a'
        elif titleWordL[1].startswith('V'):
            pos1 = 'v'
        elif titleWordL[1].startswith('R'):
            pos1 = 'r'
        else:
            pos1 = 'n'

        titleWordL[0] = wordLemmatizer.lemmatize(titleWordL[0], pos1)
        titleWordT = tuple(titleWordL)
        tempTitle.append(titleWordT)

    newTitle2 = tempTitle

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

    with open('title.txt', 'w', encoding='utf-8') as text_file:
        print(newTitle2, file=text_file)
