sample = {1: [('help', 'NN'), ('someone', 'NN'), ('evaluate', 'VBG'), ('large', 'JJ'), ('amount', 'NN'), ('bangla', 'NN'), ('document', 'NNS'), ('writing', 'NNS'), ('give', 'VBG'), ('necessary', 'JJ'), ('information', 'NN'), ('content', 'NN'), ('document', 'NNS')], 2: [('hi', 2), ('hello', 5), ('hello', 2), ('hello', 5)], 3: [('yow', 1), ('hello', 5), ('jacks', 1), ('jacks', 7)]}
import math

isf = 0
isf = 20

def hays():
    for k, v in sample.items():
        temp = []
        for w in v:
            wtl = list(w)
            wtl.append(0)
            wtl.append(0)
            wtt = tuple(wtl)
            temp.append(wtt)
        sample[k] = temp


    for k, v in sample.items():
        cs = k
        for k2, v2 in sample.items():
            temp2 = []
            os = k2
            csw = sample[cs]
            osw = sample[os]
            if(cs != os):
                for word in csw:
                    counter = 0
                    ctl = list(word)
                    cw = ctl[0]
                    for word2 in osw:
                        otl = list(word2)
                        ow = otl[0]
                        if(cw == ow):
                            counter += 1
                    ctl[2] += counter
                    ctt = tuple(ctl)
                    temp2.append(ctt)
                sample[k] = temp2


    for k, v in sample.items():
        cs = v
        t = []
        print(len(v))
        for w in cs:
            c = 0
            csl = list(w)
            cw = csl[0]
            for w2 in cs:
                osl = list(w2)
                ow = osl[0]
                if(cw == ow):
                    c += 1
            csl[3] += c - 1
            cst = tuple(csl)
            t.append(cst)
        sample[k] = t

    print(sample)

def hello():
    print("wtf")

print("something")
'''for sentenceKey3, experimentalSentence3 in exDict.items():
    currentSentence2 = experimentalSentence3
    sentenceTemp2 = []
    for word3 in currentSentence2:
        tf = 0
        currentWordL = list(word3)
        currentWord2 = currentWordL[0]
        for word4 in currentSentence2:
            otherWordL = list(word4)
            otherWord2 = otherWordL[0]
            if(currentWord2 == otherWord2):
                tf += 1
        currentWordL[3] += tf - 1
        currentWordT = tuple(currentWordL)
        sentenceTemp2.append(currentWordT)
    exDict[sentenceKey3] = sentenceTemp2'''
