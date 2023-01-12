from collections import Counter
import struct
import numpy as np
import time
start = time.time()

def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

#inputstr = input("Enter a Sequence: ")
inputstr = "ABCAABDC"

res= Counter(inputstr)
#print(str(res))
M=len(res)

N = 5
A= np.zeros((M,5),dtype=object) 

reskeys= list(res.keys())
resvalue = list(res.values())
totalsum = sum(resvalue) 

#Creating Table

A[M-1][3] =0
for i in range(M):
    A[i][0]= reskeys[i]
    A[i][1] = resvalue[i] 
    A[i][2] = ((resvalue[i]*1.0)/totalsum)

i=0
A[M-1][4] = A[M-1][2]
while i < M-1:
    A[M-i-2][4] = A[M-i-1][4] + A[M-i-2][2]    
    A[M-i-2][3] = A[M-i-1][4]    
    i+=1

#print(A)

#print("\n------- ENCODING -------\n")

strlist=list(inputstr)
LEnco=[]
UEnco=[]
LEnco.append(0)
UEnco.append(1)

for i in range(len(strlist)):
    result= np.where(A == reskeys[reskeys.index(strlist[i])])
    addtollist = (LEnco[i] + (UEnco[i] - LEnco[i])*float(A[result[0],3]))    
    addtoulist= (LEnco[i] + (UEnco[i] - LEnco[i])*float(A[result[0],4]))
    LEnco.append(addtollist)
    UEnco.append(addtoulist)
    
tag= (LEnco[-1] + UEnco[-1])/2.0
LEnco.insert(0,"Lower Range")
UEnco.insert(0,"Upper Range")
end = time.time()

    
#print(np.transpose(np.array(([LEnco],[UEnco]),dtype=object)))
#print("\nThe Tag is \n")

rate = (1 - (len(binary(tag))/(8*len(inputstr))))

print("Arithmetic Coding")
print("time:{0}".format(end - start))
print("input: {0}".format(inputstr))
print("output: {0}".format(tag))
print("output in bin: {0}".format(binary(tag)))
print("rate:{0}".format(rate))




'''
print("\n------- DECODING -------\n")

ltag=0
utag= 1
decodedSeq=[]

for i in range(len(inputstr)):
    numDeco= ((tag - ltag)*1.0)/(utag - ltag)
    for i in range(M):
        if (numDeco > float(A[i,3]) and numDeco < float(A[i,4])):
            decodedSeq.append(str(A[i,0]))
            ltag= float(A[i,3])
            utag= float(A[i,4])
    tag=numDeco
        
print("The decoded Sequence is \n")
print("".join(decodedSeq))
'''
