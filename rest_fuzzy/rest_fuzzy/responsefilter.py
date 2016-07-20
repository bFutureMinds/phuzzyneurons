import os
from rest_fuzzy.settings import BASE_DIR
def getDictionaryForUser():
    d = {}
    with open(os.path.join(BASE_DIR, 'user-info')) as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    return d

def filterresponse(response):
    print response
    dic =getDictionaryForUser()
    test = response.format(**dic)
    print test
    return test

#filterresponse("your balance is 10")
def testresponse():
    print 'hello'