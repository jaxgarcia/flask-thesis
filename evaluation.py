from rouge import Rouge

hypothesisTxt = open('hypothesis.txt', 'r', encoding='utf-8')
hypothesis = hypothesisTxt.read()

referenceTxt = open('reference.txt', 'r', encoding='utf-8')
reference = referenceTxt.read()

rouge = Rouge()
scores = rouge.get_scores(hypothesis, reference)
print(scores)
