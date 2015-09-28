# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:25:53 2015

@author: praveenkumar
"""

import datetime
import time

def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    Hint: 
    There are a couple of useful functions in the datetime library that will
    help on this assignment, called strptime and strftime. 
    More info can be seen here and further in the documentation section:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''
    #print date
    words= date.strip().split("-")
    #print words
    month=""
    
    if words[0] == '01':
        month="Jan"
    if words[0]== '02':
        month ="Feb"
    if words[0] == '03':
        month="Mar"
    if words[0] == '04':
        month="Apr"
    if words[0]== '05':
        month ="May"
    if words[0] == '06':
        month="Jun"
    if words[0] == '07':
        month="Jul"
    if words[0]== '08':
        month ="Aug"
    if words[0] == '09':
        month="Sep"
    if words[0] == '10':
        month="Oct"
    if words[0]== '11':
        month ="Nov"
    if words[0] == '12':
        month="Dec"
    
    #print month
    conv_date = '{0} {1} {2}'.format(words[1],month,words[2])
    #print conv_date
    newdate_time = time.strptime(conv_date, "%d %b %y")           
    
    
    date_formatted = '{0}-{1}-{2}'.format(newdate_time.tm_year,words[0],words[1])
    #print date_formatted
    #date_formatted = 
    return date_formatted
