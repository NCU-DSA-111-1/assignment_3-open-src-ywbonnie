import time
start = time.time()
dic = {}

class Node(object):
    def __init__(self,name=None,value=None):
        self._name=name
        self._value=value
        self._left=None
        self._right=None
        
class HuffmanTree(object):
    def __init__(self,char_weights):
        self.Leav=[Node(part[0],part[1]) for part in char_weights]
        while len(self.Leav)!=1:    
            self.Leav.sort(key=lambda node:node._value,reverse=True)
            c=Node(value=(self.Leav[-1]._value+self.Leav[-2]._value))
            c._left=self.Leav.pop(-1)
            c._right=self.Leav.pop(-1)
            self.Leav.append(c)
        self.root=self.Leav[0]
        self.Buffer=list(range(10))
        
    def pre(self,tree,length):
        node=tree
        if (not node):
            return
        elif node._name:
            #print (node._name + '    encoding:',end=''),
            code = ''
            for i in range(length):
                code += str(self.Buffer[i])
                #print (self.Buffer[i],end='')
            #print ('\n')
            #print({node._name:code})
            if node._name not in dic:
                dic.update({node._name:code})
            return 
        self.Buffer[length]=0
        self.pre(node._left,length+1)
        self.Buffer[length]=1
        self.pre(node._right,length+1)
  
    def get_code(self):
        self.pre(self.root,0)
        

def getWeight(string):
    word = []
    weight = []
    for i in range(len(string)):
        if string[i] not in word:
            weight.append((string[i], string.count(string[i])))
            word.append(string[i])
    return weight

def getH(inputstr):
    output = ''
    for i  in range(len(inputstr)):
        output += dic[inputstr[i]]
    return output

#inputstr = input("Enter a Sequence: ")
inputstr = "ABCAABDC"
#char_weights=[('A',3),('B',2),('C',2),('D',1)]
char_weights=getWeight(inputstr)
tree=HuffmanTree(char_weights)
tree.get_code()
#print(char_weights)
#print(dic)

ans = getH(inputstr)
end = time.time()


hlen = 0
for i in range(len(char_weights)):
    idx = char_weights[i][0]
    hlen += char_weights[i][1]*len(dic[idx])

rate = (1 - (hlen/(8*len(inputstr))))

print("Huffman Coding")
print("time:{0}".format(end - start))
print("input:{0}".format(inputstr))
print("output:{0}".format(ans))
print("rate:{0}".format(rate))















