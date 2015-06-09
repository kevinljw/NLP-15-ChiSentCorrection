#place = open("place.txt",'r')

ans = open("ans.txt",'r')
test = open("p2.test.txt",'r')
result = open("p2.result.txt",'w')
length = 200


for data in test:

    token = data.split()

    ID = token[0]

    data2 = ans.readline()
    token = data2.split()
    start = token[0]
    end = token[1]

    result.write(ID+'\t'+start+'\t'+end+'\n')

