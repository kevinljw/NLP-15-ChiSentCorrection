__author__ = 'mac'

redundant = open("input/p2.train.txt",'r')
#newredundant = open("newredundant.txt",'r')
red = open("tmp/redundant.txt",'w')
#place = open("place.txt",'w')

reWords = set()
for i in xrange(2962):#5924 2962
    data = redundant.readline()
    #print(data)
    token = data.split()
    #print(token)
    wrong = token[1]
    sentence = token[2]
    #print(wrong)
    #print(sentence)
    #print(len(sentence))
    #rightset = set()


    word = sentence.decode('utf8')
    wordW = wrong.decode('utf8')
    nGramHashKey = word
    for k in xrange(len(wordW)):
        if k == len(word):
            break
        if word[k]!=wordW[k]:
            break

    #print(wordW[k:k+len(wordW)-len(word)])
    ans = wordW[k:k+len(wordW)-len(word)]
    reWords.add(ans.encode('utf8'))
    #place.write(str(k+1)+' '+str(k+len(wordW)-len(word))+'\n')
    #red.write(str(ans.encode('utf8'))+'\n')
    """
    for i in range(len(wrong)/3):
        if i*3+4 == len(right):
            #print(wrong[i:])
            break
        if wrong[i*3:i*3+3] != right[i*3:i*3+3]:

            break
    """
"""
stop = open("stopword_1.txt",'r')
for line in stop:
    reWords.add(line[:len(line)-1])
"""
#    re = len(wrong)-len(right)
#    print(wrong[i*3:i*3+re])
"""
for data in newredundant:
    token = data.split()
    ans = token[0].decode('utf8')

    reWords.add(ans.encode('utf8'))
"""
"""
redundantWord = open("testDefined_ans_w.txt",'r')
count = 0
for data in newredundant:
    token = data.split()
    if token[0].decode('utf8') in reWords:
        count+=1

print(count/200)
"""
for item in reWords:
    red.write(str(item)+'\n')

