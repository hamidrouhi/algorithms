'''
Huffman coding is based on the frequency of occurance of
a data item (pixel in images).The principle is to use a
lower number of bits to encode the data that occurs more
frequently. Codes are stored in a Code Book which may be
constructed for each image or a set of images.
In all cases the code book plus encoded data must be
transmitted to enable decoding.

for more information http://en.wikipedia.org/wiki/Huffman_coding
'''


def heap_gen(Data):  # generate heap
	tree = list(Data)
	while len(tree) > 1:
		LeftChild = min(tree)
		index = tree.index(LeftChild)
		LeftChildList = list(tree[index])
		del tree[index]
		RightChild = min(tree)
		index = tree.index(RightChild)
		RightChildList = list(RightChild)
		del tree[index]
		parent = (LeftChildList[0] + RightChildList[0], LeftChild, RightChild)
		tree.append(parent)
	return tree[0]


def encode(huffhep):  # generate huffman Code
	def enc(huffheap, prefix=''):
		global keys
		if len(huffheap) == 2:
			key = (huffheap[1], str(prefix))
			keys.append(key)

		else:
			enc(huffheap[1], prefix + '0')
			enc(huffheap[2], prefix + '1')
	enc(huffheap)
	codes()


def get_CharCount(string):
	charCount = {}
	huffheap = []
	for char in string:
		charCount[char] = charCount.get(char, 0) + 1
	for items in charCount.items():
		items = list(items)
		huffheap.append((items[1], items[0]))
	huffheap.sort()
	huffheap = heap_gen(huffheap)
	encode(huffheap)


def codes():
	huffcode = ''
	code = {}
	for items in keys:
		items = list(items)
		code[items[0]] = items[1]
	for i in string:
		huffcode = huffcode + str(code[i])
	print huffcode


def huffman(DATA):  # main func
	string = DATA
	keys = []
	get_CharCount(string)
