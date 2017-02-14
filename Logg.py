import sys
import os
import datetime
def makelog(name='log.txt'):
    log = open(str(name), 'w')
    log.close()
def log(msg, lvl='info', logfile='log.txt'):
    if not os.path.isfile(logfile):
        makelog()
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f = open(logfile, 'a')
    if lvl == 'info':
        string = '[' + str(t) + '] [INFO]: ' + str(msg) + '\n'
    elif lvl == 'warn':
        string = '[' + str(t) + '] [WARN]: ' + str(msg) + '\n'
    elif lvl == 'error':
        string = '[' + str(t) + '] [ERROR]: ' + str(msg) + '\n'
    elif lvl == 'exception':
        string = '[' + str(t) + '] [EXCEPTION]: ' + str(msg) + '\n' 
    else:
        raise Exception('Invalid String!')
    f.write(string)
    f.close()
def remlog(log='log.txt'):
    os.remove(log)
    
        
    
