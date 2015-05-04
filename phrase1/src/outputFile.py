#!/usr/bin/python
# -*- coding: utf-8 -*-

line = open("input/p1.test.txt",'r')
answer = open("tmp/test_prob.result",'r')
result = open("output/p1.result.txt",'w')

for i in xrange(200):#5924 2962
    data = line.readline()
    token = data.split()
    ID = token[0]
    ans = answer.readline()
    result.write(str(ID)+'\t'+ans)