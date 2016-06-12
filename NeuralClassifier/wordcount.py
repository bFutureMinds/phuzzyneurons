#!/usr/bin/python

wordcountForPayment={}
wordCountForLogin={}
wordCountForOthers= {}

with open("trainingfile") as file:
    content = file.readlines()
    for lines in content:
        domain=lines[-4:].rstrip()
        textpart = lines[:-5]
        #print domain
        if domain=="PAY":
            for word in textpart.split(" "):
               # print word
                if word not in wordcountForPayment:
                    wordcountForPayment[word] =1
                else:
                    wordcountForPayment[word] += 1
        elif domain=="LGN":
            for word in textpart.split(" "):
               # print word
                if word not in wordCountForLogin:
                    wordCountForLogin[word] =1
                else:
                    wordCountForLogin[word] += 1
        else:
            for word in textpart.split(" "):
               # print word
                if word not in wordCountForLogin:
                    wordCountForLogin[word] = 1
                else:
                    wordCountForLogin[word] += 1


#print wordcountForPayment
#print wordCountForLogin
#print wordCountForOthers



def getWordProbabilities(word):

    paymentCount = 0
    loginCount = 0
    otherCount = 0
    if word in wordcountForPayment:
        paymentCount = wordcountForPayment[word]
    if word in wordCountForLogin:
        loginCount += wordCountForLogin[word]
    if word in wordCountForOthers:
        otherCount += wordCountForOthers[word]
    totalCount = paymentCount + loginCount + otherCount;
    if(totalCount == 0):
        return float(0), float(0), float(0)
    else:
        return float(paymentCount)/float(totalCount), float(loginCount)/float(totalCount),float(otherCount)/float(totalCount)

# for w in wordcountForPayment:
#    prob = wordcountForPayment[w]/float(getWordCount(w))
#    print "probability for %s /t %s" % (w,prob)
file.close()