import math
import os
import random
import re
import sys

#write your code here
#solution start
def avg(*num):
  if len(num)==0:
    return None
  sum_num=0
  for i in num:
    sum_num += i
    return(float(sum_num)/len(num))
 #end

 if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = map(int, raw_input().split())
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close() 
