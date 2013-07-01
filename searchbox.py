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


    def getWords(self, word = "", node=None, prt_nd=None):
	
	if node.getSize() == 0:
	    print word
	    return ""

	if node.end:
	    print word
	for l in node.ltrs:
		self.getWords(word = word + l, node=node.ltrs[l], prt_nd=node)
	    	    

class Node(object):
    def __init__(self):
	self.ltrs={}
	self.end = False #a letter that points to self is the end of a full word
	
    def getSize(self):
	return len(self.ltrs)


p = Root()
p.populate("with an ability to compress myself")
p.populate("i am a search box tree")
p.populate("hello world")
p.compress(p.root)
p.getWords(node=p.root)

