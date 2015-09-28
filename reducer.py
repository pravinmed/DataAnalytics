# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:28:14 2015

@author: praveenkumar
"""

import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
        
    dist_count={}
    #print "hello"
    #print sys.stdin
    for line in sys.stdin:
        # your code here
        #print line
        words=line.strip().split('\t')
        
        if len(words)>=2:
            count = float(words[1])
            if words[0] in dist_count:
                dist_count[words[0]]+=count
            else:
                dist_count[words[0]]=count
                
     
    for key in dist_count:
        #print key,'\t',str(dist_count[key])
        output ='{0}\t{1}'.format(key,(dist_count[key]))
        print output
        logging.info(output)
                
    
        
        

reducer()
