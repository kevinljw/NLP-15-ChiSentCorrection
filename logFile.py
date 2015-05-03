import numpy as np


line = open("ngram_prob.txt",'r')

line2 = open("ngram_test_prob.txt",'r')

line3 = open("ngram_probLog.txt",'w')

line4 = open("ngram_test_probLog.txt",'w')

x = []
y = []
for i in xrange(5294):#1904
    data = line.readline()
    token = data.split()
    y.append(int(token[0]))
    f1 = token[1].split(':')
    f2 = token[2].split(':')
    #print(f1)
    f1 = np.log10(float(f1[1]))
    f2 = np.log10(float(f2[1]))
    line3.write(str(token[0])+' 1:'+str(f1)+' 2:'+str(f2)+'\n')


xnew = []
for i in xrange(200):#1904
    data = line2.readline()
    token = data.split()
    f1 = token[0].split(':')
    f2 = token[1].split(':')
    f1 = np.log10(float(f1[1]))
    f2 = np.log10(float(f2[1]))
    line4.write('0 1:'+str(f1)+' 2:'+str(f2)+'\n')

