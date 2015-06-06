redundant = open("input/p2.train.txt",'r')
red = open("tmp/redundant.txt",'w')
for line in redundant:
    #print(line)
    token = line.split('\t')
    wrong = token[1]
    #print(wrong)
    rightN = token[2].split('\n')
    find = 0
    print(wrong)
    print(rightN[0])
    right = rightN[0]
    #wrongset = set()
    #rightset = set()
    """
    for i in xrange(len(wrong)):
        wrongset.add(wrong[i])
    for i in xrange(len(right)):
        rightset.add(right[i])

    print(wrongset-rightset)
    """
    for i in xrange(len(wrong)):
        if i == len(right):
            print(wrong[i:])
            break
        if wrong[i] != right[i]:
            re = len(wrong)-len(right)
            print(wrong[i:i+re])
            red.write(wrong[i:i+re])
            find = 1
            break
        #if find == 1:
            #break

