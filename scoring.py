import math

preprocessedTxt = open('experimentaldictionary.txt', 'r', encoding='utf-8').read()
exDict = eval(preprocessedTxt)
scoreDict = {}

titleTxt = open('title.txt', 'r', encoding='utf-8').read()
title = eval(titleTxt)


def tfinitialize(exDict):
    for sentenceKey, experimentalSentence in exDict.items():
        sentenceTemp = []
        for word in experimentalSentence:
            wordTL = list(word)
            wordTL.append(0)
            wordTT = tuple(wordTL)
            sentenceTemp.append(wordTT)
        exDict[sentenceKey] = sentenceTemp
        scoreDict[sentenceKey] = []

    tfisf(exDict)


def tfisf(exDict):
    for sentenceKey, experimentalSentence in exDict.items():
        currentKey = sentenceKey
        for sentenceKey2, experimentalSentence2 in exDict.items():
            sentenceTemp = []
            otherKey = sentenceKey2
            currentSentence = exDict[currentKey]
            otherSentence = exDict[otherKey]
            if(currentKey != otherKey):
                for word in currentSentence:
                    frequency = 0
                    currentWordL = list(word)
                    currentWord = currentWordL[0]
                    for word2 in otherSentence:
                        otherWordL = list(word2)
                        otherWord = otherWordL[0]
                        if(currentWord == otherWord):
                            frequency += 1
                        else:
                            frequency += 0
                    currentWordL[2] += frequency
                    currentWordT = tuple(currentWordL)
                    sentenceTemp.append(currentWordT)
                exDict[sentenceKey] = sentenceTemp

        for sentenceKey3, experimentalSentence3 in exDict.items():
            currentSentence2 = exDict[sentenceKey3]
            isf = 0
            tf = 0
            tfisf = 0
            aveTfisf = 0
            listTemp = []
            length = len(currentSentence2)
            for word3 in currentSentence2:
                currentWordL2 = list(word3)
                frequency2 = currentWordL2[2]
                isf += frequency2

            for word4 in currentSentence2:
                currentWordL3 = list(word4)
                tf = currentWordL3[2]
                if(isf > 0):
                    tfisf += (math.log10(isf) * tf)/length
                else:
                    tfisf += 0

            if(length > 0):
                aveTfisf = round(tfisf/length, 3)
            else:
                aveTfisf = 0

            listTemp.append(aveTfisf)
            scoreDict[sentenceKey3] = listTemp

    with open('experimentaldictionary2.txt', 'w', encoding='utf-8') as text_file:
        print(exDict, file=text_file)

    sentencePosition(scoreDict, exDict)


def sentencePosition(scoreDict, exDict):
    n = len(exDict)
    th = 0.2 * n
    minv = th * 2
    maxv = th * 2 * n

    for sentenceKey, sentenceScore in scoreDict.items():
        senPos = 0
        currentScore = scoreDict[sentenceKey]
        if(sentenceKey == 1 or sentenceKey == n):
            senPos = 1
        else:
            senPos = round(math.cos((sentenceKey - minv) * ((1/maxv) - minv)), 3)

        currentScore.append(senPos)
        scoreDict[sentenceKey] = currentScore

    numericToken(scoreDict, exDict)


def numericToken(scoreDict, exDict):
    for sentenceKey, experimentalSentence in exDict.items():
        currentSentence = exDict[sentenceKey]
        currentScore = scoreDict[sentenceKey]
        numToken = 0
        for word in currentSentence:
            currentWordL = list(word)
            currentWord = currentWordL[0]
            if(currentWord.isnumeric()):
                numToken += 1
            else:
                numToken += 0

        length = len(currentSentence)
        if(length > 0):
            numTokenScore = round(numToken/length, 3)
        else:
            numTokenScore = 0
        currentScore.append(numTokenScore)
        scoreDict[sentenceKey] = currentScore

    sentenceLength(scoreDict, exDict)


def sentenceLength(scoreDict, exDict):
    maxLength = 0
    for sentenceKey, experimentalSentence in exDict.items():
        currentSentence = exDict[sentenceKey]
        currentLength = len(currentSentence)
        if(currentLength >= maxLength):
            maxLength = currentLength

    for sentenceKey2, experimentalSentence2 in exDict.items():
        currentSentence2 = exDict[sentenceKey2]
        currentScore = scoreDict[sentenceKey2]
        senLength = len(currentSentence2)
        senLengthScore = round((senLength/maxLength), 3)
        currentScore.append(senLengthScore)
        scoreDict[sentenceKey2] = currentScore

    titleOverlap(scoreDict, exDict)


def titleOverlap(scoreDict, exDict):
    for sentenceKey, experimentalSentence in exDict.items():
        currentSentence = exDict[sentenceKey]
        currentScore = scoreDict[sentenceKey]
        length = len(currentSentence)
        commonTerms = 0
        for word in currentSentence:
            currentWordL = list(word)
            currentWord = currentWordL[0]
            for word2 in title:
                titleWordL = list(word2)
                titleWord = titleWordL[0]
                if(currentWord == titleWord):
                    commonTerms += 1
        if(length > 0):
            toScore = round(commonTerms/length, 3)
        else:
            toScore = 0
        currentScore.append(toScore)
        scoreDict[sentenceKey] = currentScore

    properNoun(scoreDict, exDict)


def properNoun(scoreDict, exDict):
    for sentenceKey, experimentalSentence in exDict.items():
        currentSentence = exDict[sentenceKey]
        currentScore = scoreDict[sentenceKey]
        length = len(currentSentence)
        pnCount = 0
        for word in currentSentence:
            currentWordL = list(word)
            currentPos = currentWordL[1]
            if(currentPos == 'NNP'):
                pnCount += 1
        if(length > 0):
            pnScore = round(pnCount/length, 3)
        else:
            pnScore = 0
        currentScore.append(pnScore)
        scoreDict[sentenceKey] = currentScore

    scoreEvaluation(scoreDict, exDict)

    with open('scoredictionary.txt', 'w', encoding='utf-8') as text_file:
        print(scoreDict, file=text_file)


def scoreEvaluation(scoreDict, exDict):
    finalScore = []

    for sentenceKey, sentenceScores in scoreDict.items():
        currentScore = scoreDict[sentenceKey]
        sentenceScore = 0
        sentenceScoreR = 0
        tfisfScore = currentScore[0]
        senPosScore = currentScore[1]
        numTokenScore = currentScore[2]
        senLengthScore = currentScore[3]
        toScore = currentScore[4]
        pnScore = currentScore[5]
        sentenceScore = ((0.1 * tfisfScore) + (0.2 * toScore) + (0.2 * (senPosScore + pnScore)) + (0.2 * (numTokenScore + senLengthScore)))
        sentenceScoreR = round(sentenceScore, 3)
        finalScore.append(sentenceScoreR)
        currentScore.append(sentenceScoreR)
        scoreDict[sentenceKey] = currentScore

    finalScore.sort(reverse=True)

    with open('scoredictionary.txt', 'w', encoding='utf-8') as text_file:
        print(scoreDict, file=text_file)

    with open('finalscore.txt', 'w', encoding='utf-8') as text_file:
        print(finalScore, file=text_file)


tfinitialize(exDict)
