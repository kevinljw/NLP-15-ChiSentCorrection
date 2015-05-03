import os
import sys

os.chdir('libsvm-3.20/python')
from svmutil import *

y, x = svm_read_problem('../../../ngram_probLog.txt')
m = svm_train(y, x)

y,x = svm_read_problem('../../../ngram_test_probLog.txt')

p_label, p_acc, p_val = svm_predict(y, x, m)

int_p_label = map(int, p_label)
# p_label, p_acc, p_val = svm_predict([0]*len(x), x, m)
fo = open("../../../svmResult.txt", "w")
str1 = '\n'.join(map(str, int_p_label))
fo.write(str1)
fo.close()

print p_label
print p_acc
print p_val