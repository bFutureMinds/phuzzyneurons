import HTMLParser
import enchant
import os
from rest_fuzzy.settings import BASE_DIR

APPOSTOPHES = {"'s" : " is", "'re" : "are","'ll" : "will", "'aint" : "are not","isn't" : "is not","'d" : "had","'ve" :"have" ,"can't" : "cannot"}
html_parser = HTMLParser.HTMLParser();
d = enchant.Dict("en_US")


with open(os.path.join(BASE_DIR, 'vocabulary')) as file:
    content = file.readlines()

def getcorrectspell(word):
    spellcorrectedword =''
    for lines in content:
        line = lines.split();
        if word in line:
            spellcorrectedword = line[0]
    return spellcorrectedword

def spellCorrection(word):
    reformedstatement = []
    for w in word.split():
        if not d.check(w):
            spellcorrectedword = getcorrectspell(w)
            if spellcorrectedword:
                new = spellcorrectedword
                reformedstatement.append(new)
            else:
                reformedstatement.append(w)
        else:
            reformedstatement.append(w)
    s = " ".join(reformedstatement)
    return s

def filterString(inputString):
    #htmltagsfilteredstring = html_parser.unescape(inputString).decode("utf8").encode('ascii','ignore')
    words = inputString.split()
    reformed = [APPOSTOPHES[word] if word in APPOSTOPHES else word for word in words]
    reformed = " ".join(reformed)
    return spellCorrection(reformed)
