# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:47:23 2015

@author: praveenkumar
"""

from pandas import *
from ggplot import *

import pandas

def lineplot(hr_year_csv):
    # A csv file will be passed in as an argument which
    # contains two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Fill out the body of this function, lineplot, to use the
    # passed-in csv file, hr_year.csv, and create a
    # chart with points connected by lines, both colored 'red',
    # showing the number of HR by year.
    #
    # You will want to first load the csv file into a pandas dataframe
    # and use the pandas dataframe along with ggplot to create your visualization
    #
    # You can check out the data in the csv file at the link below:
    # https://www.dropbox.com/s/awgdal71hc1u06d/hr_year.csv
    #
    # You can read more about ggplot at the following link:
    # https://github.com/yhat/ggplot/
    
    data = pandas.read_csv(hr_year_csv)
    # first method to plot
    gg = ggplot(data,aes('yearID','HR'))+geom_point(color='RED')+geom_line(color='red')
    print gg
   
    # second method 
    gg = ggplot(aes(x='yearID', y='HR'), data) +\
    geom_line() +\
    stat_smooth(colour='blue', span=0.2)
    return gg
