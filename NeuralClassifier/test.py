
import re
print "hello world"

string = "this is a string"
for word in string.split():
    print (word)
count = {}

input = open('testFile').read();
filterInput = re.sub('[^a-zA-Z0-9\n\.]', ' ',input)
for w in filterInput.split():
    	if w in count:
        	count[w] += 1
    	else:
        	count[w] = 1
for word, times in count.items():
    print "%s was found %d times" % (word, times)
