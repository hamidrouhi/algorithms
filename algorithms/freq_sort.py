'''
	this module genarate tree of chars with it frequency,
	this appear for some alghorithm like Huffman alghorithm
	
	you can use this like other modules,

	WARNING: this module is't work if you give bad data,
	for more info see this http://github.com/revolt313/pyheap

'''
__version__= '1.0.0'

def heap_gen(Data):
	global tree,parent
	tree=list(Data)
	while len(tree)>1:
		LeftChild=min(tree)
		index=tree.index(LeftChild)
		LeftChildIndex=list(tree[index])
		del tree[index]
		RightChild=min(tree)
		index=tree.index(RightChild)
		RightChildIndex=list(RightChild)
		del tree[index]
		parent=(LeftChildIndex[0]+RightChildIndex[0],LeftChild,RightChild)
		tree.append(parent)
	return tree[0]

