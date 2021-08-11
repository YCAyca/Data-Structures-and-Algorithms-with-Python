# A Huffman Tree Node
class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol 
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

""" A helper function to print the codes of symbols by traveling Huffman Tree"""
codes = dict()

def Calculate_Codes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)

    if(node.left):
        Calculate_Codes(node.left, newVal)
    if(node.right):
        Calculate_Codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal
         
    return codes        

""" A helper function to calculate the probabilities of symbols in given data"""
def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else: 
            symbols[element] += 1     
    return symbols


""" A helper function to print the encoded data"""
def Print_Encoded(data, coding):
    for c in data:
        print(coding[c], end = '')

def Huffman_Encoding(data):
    symbol_with_probs = Calculate_Probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols: ", symbols)
    print("probabilities: ", probabilities)
    
    nodes = []
    
    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)
        #for node in nodes:  
         #    print(node.symbol, node.prob)
    
        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]
    
        left.code = 0
        right.code = 1
    
        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
    
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    
    huffman_encoding = Calculate_Codes(nodes[0])
    print(huffman_encoding)
    Total_Gain(data, huffman_encoding)
    print("Encoded :")
    Print_Encoded(data,huffman_encoding)
    
""" A helper function to calculate the space difference between compressed and non compressed data"""    
def Total_Gain(data, coding):
    before_compression = len(data) * 8 # total bit space to stor the data before compression
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol]) #calculate how many bit is required for that symbol in total
    print("Space usage before compression (in bits):", before_compression)    
    print("Space usage after compression (in bits):",  after_compression)    




""" First Test """
data = "DBAEABCAAADEABCACBAAEABAACDBDAABCDE"
print(data)
Huffman_Encoding(data)

# """ Second Test """

data = """Einstein was born in the German Empire, 
but moved to Switzerland in 1895, forsaking his German citizenship 
(as a subject of the Kingdom of Württemberg)[note 1] the following year. 
In 1897, at the age of 17, he enrolled in the mathematics and physics 
teaching diploma program at the Swiss Federal polytechnic school 
(later renamed as ETH Zurich) in Zürich, graduating in 1900. 
In 1901 he acquired Swiss citizenship, which he kept for the rest of his 
life, and in 1903 he secured a permanent position at the Swiss Patent Office in Bern. 
In 1905, he was awarded a PhD by the University of Zurich. In 1914, 
Einstein moved to Berlin in order to join the Prussian Academy of Sciences and the Humboldt 
University of Berlin. In 1917, Einstein became director of the Kaiser Wilhelm Institute for 
Physics; he also became a German citizen again – Prussian this time. In 1933, while 
Einstein was visiting the United States, Adolf Hitler came to power. Einstein did not return 
to Germany because he objected to the policies of the newly elected Nazi-led government.[16] 
He settled in the United States and became an American citizen in 1940.[17] On the eve of 
World War II, he endorsed a letter to President Franklin D. Roosevelt alerting him to the potential 
German nuclear weapons program and recommending that the US begin similar research. 
Einstein supported the Allies, but generally denounced the idea of nuclear weapons."""
print(data)
Huffman_Encoding(data)

""" Third Test """


f = open("demofile.txt", "r")

data = f.read()
print(data)
Huffman_Encoding(data)


