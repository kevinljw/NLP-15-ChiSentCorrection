trainData = open("input/p2.val.txt",'r')
noTag = open("tmp/noTagTest.txt",'w')

for line in trainData:
    
    token = line.split('\t')

    testingData = token[1].split('\n')
    
    # # print(wrong)
    # print(testingData[0])

    noTag.write(str(testingData[0])+'\n')

  