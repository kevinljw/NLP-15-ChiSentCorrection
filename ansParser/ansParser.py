# ansData = open("predict.txt",'r')
ansData = open("result.txt",'r')
outputResult = open("ansParser.txt",'w')

i = 0

for line in ansData:
    

    if line and not line.isspace():
    
      token = line.decode('utf-8').split()
      # print 
      outputResult.write("p2test-"+str(i)+"\t"+str(token[0][:int(token[1])-1].encode('UTF-8'))+"["+str(token[0][int(token[1])-1:int(token[2])].encode('UTF-8'))+"]"+str(token[0][int(token[2]):].encode('UTF-8'))+"\n")   
  
      i+=1