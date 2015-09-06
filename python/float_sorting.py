#!/usr/bin/python

import timeit

setup = '''
import random 
s = [random.random() for i in range(1000000)]
'''

index_sequence = [index for index in xrange(100000, 1000000, 100000)]
time_sequence = [(timeit.Timer('a=s[:%d];sorted(a)' %index, setup=setup).repeat(1,3))[0] for index in index_sequence]

### find the loose bound on the list size
print 'Find soft bound'
flag1 = True
flag2 = True
flag3 = True
soft_bd = []
time_bd = [10.0, 100.0, 1000.0]
for index in xrange(len(time_sequence)):
  if flag1: 
    if time_sequence[index] > time_bd[0]/1000.0:
      soft_bd.append(index_sequence[index])
      print "sorted in %d ms - array size: %d" %(time_bd[0], index_sequence[index])
      flag1 = False
  if flag2:
    if time_sequence[index] > time_bd[1]/1000.0:
      soft_bd.append(index_sequence[index])
      print "sorted in %d ms - array size: %d" %(time_bd[1], index_sequence[index])
      flag2 = False
  if flag3:
    if time_sequence[index] > time_bd[2]/1000.0:
      soft_bd.append(index_sequence[index])
      print "sorted in %d ms - array size: %d" %(time_bd[2], index_sequence[index])
      flag3 = False
  else:
    break

###seek the accurate list size 
print 'Find accurate bound'
for ii in xrange(len(time_bd)):
  sbd = soft_bd[ii]
  unit = 100000
  while unit > 10:
    unit = unit / 10
    index_sequence = [index for index in xrange(sbd-unit*10, sbd+unit, unit)]
    time_sequence = [(timeit.Timer('a=s[:%d];sorted(a)' %index, setup=setup).repeat(1,3))[0] for index in index_sequence]
    for index in xrange(len(time_sequence)):
      if time_sequence[index] > time_bd[ii]/1000.0:
        print "sorted in %d ms - array size: %d" %(time_bd[ii], index_sequence[index-1])
        sbd = index_sequence[index]
        break

