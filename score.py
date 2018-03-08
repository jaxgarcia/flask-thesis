import math


def scoreInitialize(experimentaldictionary, title, referenceDictionary):
    preprocessedTxt = open(experimentaldictionary, 'r', encoding='utf-8').read()
    exDict = eval(preprocessedTxt)
    scoreDict = {}

    titleTxt = open(title, 'r', encoding='utf-8').read()
    title = eval(titleTxt)

    referenceTxt = open(referenceDictionary, 'r', encoding='utf-8').read()
    reDict = eval(referenceTxt)

    tfinitialize(exDict, scoreDict, title, reDict)


def tfinitialize(exDict, scoreDict, title, reDict):
    for sentenceKey, experimentalSentence in exDict.items():
        sentenceTemp = []
        for word in experimentalSentence:
            wordTL = list(word)
            wordTL.append(0)
            wordTT = tuple(wordTL)
            sentenceTemp.append(wordTT)
        exDict[sentenceKey] = sentenceTemp
        scoreDict[sentenceKey] = []

    tfisf(exDict, scoreDict, title, reDict)


def tfisf(exDict, scoreDict, title, reDict):
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

    sentencePosition(exDict, scoreDict, title, reDict)


def sentencePosition(exDict, scoreDict, title, reDict):
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

    numericToken(exDict, scoreDict, title, reDict)


def numericToken(exDict, scoreDict, title, reDict):
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

    sentenceLength(exDict, scoreDict, title, reDict)


def sentenceLength(exDict, scoreDict, title, reDict):
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

    titleOverlap(exDict, scoreDict, title, reDict)


def titleOverlap(exDict, scoreDict, title, reDict):
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

    properNoun(exDict, scoreDict, title, reDict)


def properNoun(exDict, scoreDict, title, reDict):
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

    scoreEvaluation(exDict, scoreDict, title, reDict)


def scoreEvaluation(exDict, scoreDict, title, reDict):
    weightedScoreDict = {}
    weightedScorePercentage = {}
    finalScore = []
    finalSentenceKeys = []
    finalSentenceDict = {}
    rankKey = 1
    abstract = ''

    for sentenceKey, sentenceScores in scoreDict.items():
        weightedScoreList = []
        currentScore = scoreDict[sentenceKey]
        sentenceScore = 0
        sentenceScoreR = 0
        wtfisfScore = round((currentScore[0] * 0.2), 3)
        wsenPosScore = round((currentScore[1] * 0.2), 3)
        wnumTokenScore = round((currentScore[2] * 0.05), 3)
        wsenLengthScore = round((currentScore[3] * 0.1), 3)
        wtoScore = round((currentScore[4] * 0.4), 3)
        wpnScore = round((currentScore[5] * 0.05), 3)
        sentenceScore = (wtfisfScore + wsenPosScore + wnumTokenScore + wsenLengthScore + wtoScore + wpnScore)
        sentenceScoreR = round(sentenceScore, 3)
        finalScore.append(sentenceScoreR)
        currentScore.append(sentenceScoreR)
        weightedScoreList.extend([wtfisfScore, wsenPosScore, wnumTokenScore, wsenLengthScore, wtoScore, wpnScore, sentenceScoreR])
        scoreDict[sentenceKey] = currentScore
        weightedScoreDict[sentenceKey] = weightedScoreList

    finalScore.sort(reverse=True)
    documentLength = len(reDict)
    if(documentLength <= 30):
        scoreRange = 7
    elif(documentLength <= 60):
        scoreRange = 9
    else:
        scoreRange = 12

    for score in finalScore[:scoreRange]:
        for scoreKey, sentenceScore in scoreDict.items():
            currentScoreKey = scoreKey
            currentScore2 = scoreDict[scoreKey]
            currentSenScore = currentScore2[6]
            if(score == currentSenScore):
                if(currentScoreKey not in finalSentenceKeys):
                    finalSentenceKeys.append(currentScoreKey)

    for finalSentenceKey in finalSentenceKeys:
        finalSentenceList = []
        for sentenceKey, sentenceValue in reDict.items():
            if(finalSentenceKey == sentenceKey):
                finalSentenceList.append(sentenceKey)
                finalSentenceList.append(sentenceValue)
        for scoreKey2, sentenceScore2 in weightedScoreDict.items():
            if(finalSentenceKey == scoreKey2):
                finalSentenceList.append(sentenceScore2)
        finalSentenceDict[rankKey] = finalSentenceList
        rankKey += 1

    for rankKey2, finalValue in finalSentenceDict.items():
        wScoreList = finalValue[2]
        wTotal = wScoreList[6]
        wPercentageList = []
        wPercentageTotal = 0
        for wScore in wScoreList:
            if(wScore < 0):
                wScore = abs(wScore)
                wTotal += wScore
        for wScore2 in wScoreList:
            if(wScore > 0):
                wPercentage = round((wScore2/wTotal) * 100, 1)
                wPercentageTotal += wPercentage
                if(wPercentageTotal <= 100):
                    wPercentageStr = str(wPercentage) + "%"
                else:
                    wPercentageDiff = wPercentageTotal - 100
                    wPercentage = round((wPercentage - wPercentageDiff), 1)
                    wPercentageStr = str(wPercentage) + "%"
            else:
                wPercentageStr = "0%"
            wPercentageList.append(wPercentageStr)
        weightedScorePercentage[rankKey2] = wPercentageList

    finalSentenceKeys.sort()
    for finalKey in finalSentenceKeys:
        abstract += reDict[finalKey] + '. '

    with open('scoredictionary.txt', 'w', encoding='utf-8') as text_file:
        print(scoreDict, file=text_file)

    with open('finalscore.txt', 'w', encoding='utf-8') as text_file:
        print(finalScore, file=text_file)

    with open('weightedscoredictionary.txt', 'w', encoding='utf-8') as text_file:
        print(weightedScoreDict, file=text_file)

    with open('weightedscorepercentage.txt', 'w', encoding='utf-8') as text_file:
        print(weightedScorePercentage, file=text_file)

    with open('abstract.txt', 'w', encoding='utf-8') as text_file:
        print(abstract, file=text_file)

    with open('abstractdictionary.txt', 'w', encoding='utf-8') as text_file:
        print(finalSentenceDict, file=text_file)
