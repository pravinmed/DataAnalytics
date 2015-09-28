# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:37:43 2015

@author: praveenkumar
"""

import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this assignment, the reducer should
    print one row per weather type, along with the average value of
    ENTRIESn_hourly for that weather type, separated by a tab. You can assume
    that the input to the reducer will be sorted by weather type, such that all
    entries corresponding to a given weather type will be grouped together.

    In order to compute the average value of ENTRIESn_hourly, you'll need to
    keep track of both the total riders per weather type and the number of
    hours with that weather type. That's why we've initialized the variable 
    riders and num_hours below. Feel free to use a different data structure in 
    your solution, though.

    An example output row might look like this:
    'fog-norain\t1105.32467557'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    riders = 0      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None
    rider_map={}
    rider_count={}
    for line in sys.stdin:
        # your code here
        words = line.strip().split("\t")
        if len(words) >=2:
            riderCount = (float(words[1].strip()))
            weather = words[0].strip()
            if old_key == None:
                old_key = weather
            if old_key != weather:
                rider_map[old_key]=rider_map[old_key]/num_hours
                old_key = weather
                num_hours = 0
            if weather in rider_map:
                num_hours+=1
                rider_map[weather]+=riderCount
            else:
                num_hours=1
                rider_map[weather]=riderCount
    rider_map[old_key]=rider_map[old_key]/num_hours         
    for key in rider_map:
        output ='{0}\t{1}'.format(key,(rider_map[key]))
        print output
        logging.info(output)

reducer()
