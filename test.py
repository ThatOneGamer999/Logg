import Logg
from Logg import *
import os
makelog()
if not os.path.isfile('log.txt'):
 raise Exception('error!')
else:
 print "Logging Creation \t\t\t\t\t[OK]"
log('Info')
print "Logging          \t\t\t\t\t[OK]"
f = open('log.txt', 'r');
l = f.readlines()
for i in l:
 print i
f.close()
remlog()
if os.path.isfile('log.txt'): raise Exception('error!')
else: print "Logging Deletion \t\t\t\t\t[OK]"
