'''
	this module genarate tree of chars with it frequency,
	this appear for some alghorithm like Huffman alghorithm
	WARNING: this module is't work if you give bad data,

	for more info see http://en.wikipedia.org/wiki/Huffman_coding
'''
__version__ = '1.0.0'


def sort(Data):
	global tree, parent
	tree = list(Data)
	while len(tree) > 1:
		LeftChild = min(tree)
		index = tree.index(LeftChild)
		LeftChildIndex = list(tree[index])
		del tree[index]
		RightChild = min(tree)
		index = tree.index(RightChild)
		RightChildIndex = list(RightChild)
		del tree[index]
		parent = (LeftChildIndex[0] + RightChildIndex[0], LeftChild, RightChild)
		tree.append(parent)
	return tree[0]

