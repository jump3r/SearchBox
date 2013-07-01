import os
#import thread

class Root(object):
    def __init__(self):
	self.root=None
	
    def compress(self, node, prt_nd=None, prt_ltr=None):

	if node.getSize()==0:
	    return node
	else:
	    if (prt_nd==None and prt_ltr==None):# or node.getSize()>1:		
		for k in node.ltrs.keys():		   
		   self.compress(node.ltrs[k], node, k)

	    elif node.getSize()==1:
		key = node.ltrs.keys()[0]
		old_parent_key_val = prt_nd.ltrs.pop(prt_ltr)
		old_key_val = node.ltrs.pop(key) #bool is kept
		new_key = prt_ltr+key
		prt_nd.ltrs[new_key] = old_key_val #contains right .end bool 
		self.compress(old_key_val, prt_nd, new_key)
	return 
	    
    def addDepth(self, node):

	if node.getSize()==0:
	    return 0
	else:
	    node.depth = node.getSize()	    
	    for b in node.ltrs:		
		node.depth += self.addDepth(node.ltrs[b])
	
	return node.depth

    def populate(self, textfile): #str textfile
	'''Non-recursive'''
	curr=self.root	
	text = [i for i in textfile]

	if self.root==None and len(textfile)>0:
	    self.root=Node()
	    curr = self.root.ltrs[text[0]] = Node()
	    
	    text = text[1:]

	for l,p in zip(text,range(len(text))):	    
	    if l in curr.ltrs:
		curr=curr.ltrs[l]
	    else:
		next = curr.ltrs[l] = Node()		
		curr = next
	curr.end=True

	
    def getAllWords(self, word = "", node=None, prt_nd=None):
	
	if node.getSize() == 0:
	    print word
	    return

	if node.end:
	    print word
	for l in node.ltrs:
	    self.getAllWords(word = word + l, node=node.ltrs[l], prt_nd=node)


#NOT TESTED===========
    def printAllWordsAfterWord(word):
	
	n = self.getEndNodeForWord(self.root, word)
	self.getAllWordsAfterNode(n, word)

    def getEndNodeForWord(self, node, word):
	'''Trace from given node until the last letter of word
		 is reached or return None '''
	curr=node
	text = [l for l in textfile]
	if self.root==None:
	    return None
	else:
	    for l in text:
		if l in curr.ltrs:
		    curr = curr.ltrs[l]
		else:
		    return None
	return curr

    def printAllWordsAfterNode(self, node, projection = ""):
	
	if node.getSize() == 0:
	    print projection
	    return

	if node.end:
	    print projection

	for l in node.ltrs:
	    self.getAllWordsAfter(node.ltrs[l], projection = projection+l)
#=========================
class Node(object):
    def __init__(self):
	self.ltrs={}
	self.end = False #a letter that points to self is the end of a full word
	self.depth = 0
	
    def getSize(self):
	return len(self.ltrs)

    def isEmpty(self):
	if self.getSize():
	    return False
	return True


p = Root()

s = "hello world, im an optimized search tree with lesser levels and better performance, although there is a room for improvement"
for w in s.split():
    p.populate(w)

p.addDepth(p.root)
p.compress(p.root)
p.addDepth(p.root)
p.getAllWords(node=p.root)

