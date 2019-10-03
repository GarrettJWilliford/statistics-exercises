import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import viz
import pandas.io.sql as psql
import pickle



def stats_bank():
    bank = stats.poisson(2)
    print(bank.cdf(0))
    print(bank.sf(2))
    print(bank.sf(0))
    

#stats_bank()s


def stats_school():
    school = stats.norm(3, .3)
    print(school.isf(.4))
    print(school.cdf(.15))
    print(school.ppf(.3))
    print('A student with a GPA of 2.8 would qualify for the scholarship')

stats_school()

def stats_market():
    print(stats.poisson(4326, 97))
    market = stats.norm(4326, 86.52)
    print(market.cdf(97))

#stats_market()


a = 6
print(a)
if a is 6:
    print(a)




def stats_codeup():
    students = stats.poisson(66)
    breakroom = students.isf(.8)
    print(breakroom)
    students = stats.poisson(breakroom)
    a = stats.binom(breakroom, .03)
    print(a.sf(0))
    print(a.pmf(2))
    print(a.pmf(5))
    
#stats_codeup()



def stats_panaderia():
    m = stats.norm(15, 3)
    print(m.cdf(17))
    
#stats_panaderia()













