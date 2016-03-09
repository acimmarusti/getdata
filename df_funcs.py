"""df_funcs.py

Data frame functions

By Andres Cimmarusti

"""
from __future__ import division
import pandas as pd

def clean(data):

    #Strip whitespaces
    fstrip = lambda x: x if not type(x) is str else x.strip()
    
    data.rename(columns=fstrip, inplace=True)

    datacols = data.columns

    for datcol in datacols:

        if data[datcol].dtypes == 'object':

            data[datcol] = data[datcol].map(fstrip)
