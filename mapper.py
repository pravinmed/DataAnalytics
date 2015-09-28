# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:27:57 2015

@author: praveenkumar
"""

import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():

    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the 
    #commas, and emit (i.e. print) a key-value pair containing the 
    #district (not state) and Aadhaar generated, separated by a tab. 
    #Skip rows without the correct number of tokens and also skip 
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    header= 0;
    hLen=0;
    word_count={}
    dist=3
    aadhar =8
    for line in sys.stdin:
        #your code here
        #logging.info(line)
        words = line.strip().split(",")
        if header==0:
            hLen=len(words)
            header=1
        else:
            ln = len(words)
            if ln==hLen:
                count =0;
                district=""
                adharGen=""
                for word in words:
                    count=count+1
                    if count == 4:
                        district = word.strip()
                    if count == 9:
                        adharGen = float(word)
                        break
                if adharGen >=0.0:
                    #print district,'\t',adharGen
                    output = '{0}\t{1}'.format(district,adharGen)
                    logging.info(output)
                    print output
                    #word_count[district] = 1
                #elif adharGen=="1":
                #    word_count[district]=1
    #for key in word_count:
    #    print'{0}\t{1}'.format(key,word_count[key])
                   
            

mapper()
