testingData = open("testDefined.txt",'r')
outputResult = open("testDefined_ans.txt",'w')

for line in testingData:
    
    if line and not line.isspace():
    
      token = line.decode('utf-8').split()

      if "[" and "]" in token[1]:
         # print token[1]
         # print token[1].find('[')+1
         # print token[1].find(']')-1
         outputResult.write(str(token[1].find('[')+1)+"\t"+str(token[1].find(']')-1)+"\n")
      # testingData = token[0].split('\n')
    
      
    # print (testingData[0]+"-")
    # # # print(wrong)
    # # print(testingData[0])
    # words = jieba.cut(testingData[0], cut_all=False)
    # for word in words:
    #   # print word.encode('UTF-8')
    #   noTag.write(str(word.encode('UTF-8'))+" ")
    # noTag.write("\n")

  