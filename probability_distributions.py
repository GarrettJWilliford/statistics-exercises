import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import viz
import pandas.io.sql as psql
import pickle




def stats_bank():
    b = range(8)
    bank = stats.poisson(2)
    bb = stats.poisson(2).pmf(b)
    trial = bank.rvs(10_000)
    print(trial)
    print('<<<<<>>>>>')
    plt.bar(b, bb)
    #plt.show()
    print(bank.cdf(0))
    print(bank.sf(2))
    print(bank.sf(0))
    

#stats_bank()


def stats_school():
    school = stats.norm(3, .3)
    print(school.isf(.4))
    print(school.cdf(.15))
    print(school.ppf(.3))
    print('A student with a GPA of 2.8 would qualify for the scholarship')

#stats_school()

def stats_market():
    market = stats.binom(4326, .02)
    print(market.sf(96))
    simulated_market = ((np.random.random((10_000, 4326)) <= .02).sum(axis = 1) >= 97).mean()
    print(simulated_market)

#stats_market()

def stats_homework():
    homework = stats.binom(60, 1 / 101)
    print(homework.pmf(1))

#stats_homework()

def stats_codeup():
    students = stats.poisson(66)
    breakroom = students.isf(.8)
    students = stats.poisson(breakroom)
    a = stats.binom(breakroom, .03)
    print(a.sf(0))
    print(a.pmf(2))
    print(a.pmf(5))
    
stats_codeup()



def stats_panaderia():
    m = stats.norm(15, 3)
    print(m.cdf(17))
    
#stats_panaderia()














