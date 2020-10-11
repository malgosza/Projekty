word='aaaaaaaaaaaabbbbbbbbbbbbbbaaaaaccccccabccccccccccc1111111'
suma=0
dic={}
i=0
while i<len(word):
    sign=word[i]
    for x in range(0,len(word)):
        if sign==word[x]:
            suma+=1
    if not(sign in dic):
        dic[sign]=suma
    i+=1
    suma=0
print(dic)
  
myDict = {}
for char in word:
    if char in myDict:
        myDict[char] += 1
    else:
        myDict[char] = 1
print(myDict)