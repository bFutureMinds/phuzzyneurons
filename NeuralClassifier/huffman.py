from heapq import heappush, heappop, heapify
import re

def codecreate(symbol2weights, tutor= False):
	heap = [ [float(wt), [sym, []]] for sym, wt in symbol2weights.iteritems() ] 
	heapify(heap) 
	if tutor: print "ENCODING:", sorted(symbol2weights.iteritems()) 
	while len(heap) >1: 
		lo = heappop(heap) 
		hi = heappop(heap) 
		if tutor: print " COMBINING:", lo, '\n AND:', hi
		for i in lo[1:]: i[1].insert(0, '0')
		for i in hi[1:]: i[1].insert(0, '1')
		lohi = [ lo[0] + hi[0] ] + lo[1:] + hi[1:]
		if tutor: print " PRODUCING:", lohi, '\n' 
		heappush(heap, lohi)
	codes = heappop(heap)[1:]
	for i in codes: i[1] = ''.join(i[1]) 
	return sorted(codes, key=lambda x: (len(x[-1]), x)) 
      
     # Input types 
input = open('testFile').read();
filterInput = re.sub('[^a-zA-Z0-9\n\.]', ' ',input)
symbol2weights = dict((ch, filterInput.count(ch)) for ch in set(filterInput.split())) # for astring 
     	  
huff = codecreate(symbol2weights, True) 
print "\nSYMBOL\t\tWEIGHT\t\tHUFFMAN CODE" 
for h in huff:
	print "%s\t\t%s\t\t%s" % (h[0], symbol2weights[h[0]], h[1].zfill(10))
