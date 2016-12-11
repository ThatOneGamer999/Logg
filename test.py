import Logg
import os
makelog()
if not os.path.isfile('log.txt'):
 raise Exception('error!')
else:
 print "Logging Creation \t\t\t\t\t[OK]
log('Info')
print "Logging          \t\t\t\t\t[OK]"
remlog()
if os.path.isfile('log.txt'): raise Exception('error!')
else: print "Logging Deletion \t\t\t\t\t[OK]
