import wordcount as wc


def findContext(sentance):
    wrds = sentance.split(" ")
    probs = []
    for w in wrds:
        prob = wc.getWordProbabilities(w)
        nul = (0,0,0)
        if sum(prob) == float(1):
            probs.append(prob)
        else:
            probs.append(nul)
    return probs


def translateDomainToLabel(text):
    if(text=="PAY"):
        return [1,0,0]
    else:
        return [0,1,0]


def main():
    with open("trainingfile") as file:
        content = file.readlines()
        j=0
        vect = [[0 for i in range(45)] for k in range(10)]

        dom = []
        for lines in content:
            domain = lines[-4:].rstrip()
            textpart = lines[:-5]

            if len(textpart.split(" ")) < 15:
                for i in range(len(textpart.split(" ")), 15):
                    textpart += " abcd"
            cntxt = findContext(textpart)
            for i in range(len(cntxt)):
                vect[j][3*i:3*i+2] = cntxt[i]

            j += 1
            dom.append(translateDomainToLabel(domain))

    return vect, dom
