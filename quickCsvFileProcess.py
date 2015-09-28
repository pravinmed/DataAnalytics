# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 07:00:35 2015

@author: praveenkumar
"""

def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        r = csv.reader(f)
        name = r.next()[1]
        header = r.next()
        data = [row for row in r]

    return (name, data)