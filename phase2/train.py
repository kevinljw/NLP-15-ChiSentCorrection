trainData = open("input/p2.train.txt",'r')
cw = open("tmp/cw.txt",'w')
cww = open("tmp/cww.txt",'w')

for line in trainData:
    
    token = line.split('\t')

    right = token[2].split('\n')
    
    # print(wrong)
    print(right[0])

  