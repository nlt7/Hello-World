s1=input("Enter first sentence ")
s2=input("Enter second sentence ")
print (s1,s2)
fs=(s1+s2)
print(fs)
finallist=fs.split(" ")

#for i in range (0,len(fs)):
#    finallist.append(fs[i])

print(finallist)
finallist.sort()
print(finallist)
print(len(finallist))

sentences= {}

for word in finallist:
    sentences[word]=finallist.count(word)

print(sentences)

