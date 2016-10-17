
# coding: utf-8


import numpy as np
import pandas as pd
import datetime as dt


##日期建模与处理
dates = [dt.datetime(2015, 1, 1), dt.datetime(2015, 7, 1), dt.datetime(2016, 1, 1)]

(dates[1]-dates[0]).days/365.

(dates[2]-dates[1]).days/365.

fractions=[0.0,0.5,1.0]

#从datetime对象列表或者数组中得出年份数
def get_year_deltas(date_list, day_count=365.):
    ''' Return vector of floats with day deltas in years.
    Initial value normalized to zero.
    
    Parameters
    ==========
    date_list : list or array
        collection of datetime objects
    day_count : float
        number of days for a year
        (to account for different conventions)
    
    Results
    =======
    delta_list : array
        year fractions
    '''

    start = date_list[0]
    delta_list = [(date - start).days / day_count
                  for date in date_list]
    return np.array(delta_list)

deltas = get_year_deltas(dates)
deltas



##固定短期利率
class constant_short_rate(object):
    ''' Class for constant short rate discounting.
    
    Attributes
    ==========
    name : string
        name of the object
    short_rate : float (positive)
        constant rate for discounting
    
    Methods
    =======
    get_discount_factors :
        get discount factors given a list/array of datetime objects
        or year fractions
    '''

    def __init__(self, name, short_rate):
        self.name = name
        self.short_rate = short_rate
        if short_rate < 0:
            raise ValueError('Short rate negative.')

    def get_discount_factors(self, date_list, dtobjects=True):
        if dtobjects is True:
            dlist = get_year_deltas(date_list)
        else:
            dlist = np.array(date_list)
        dflist = np.exp(self.short_rate * np.sort(-dlist))
        return np.array((date_list, dflist)).T

csr=constant_short_rate('csr',0.05)
csr.get_discount_factors(dates)

csr.get_discount_factors(deltas, dtobjects=False)

##市场环境
class market_environment(object):
    ''' Class to model a market environment relevant for valuation.
    
    Attributes
    ==========
    name: string
        name of the market environment
    pricing_date : datetime object
        date of the market environment
    
    Methods
    =======
    add_constant :
        adds a constant (e.g. model parameter)
    get_constant :
        gets a constant
    add_list :
        adds a list (e.g. underlyings)
    get_list :
        gets a list
    add_curve :
        adds a market curve (e.g. yield curve)
    get_curve :
        gets a market curve
    add_environment :
        adds and overwrites whole market environments
        with constants, lists, and curves
    '''

    def __init__(self, name, pricing_date):
        self.name = name
        self.pricing_date = pricing_date
        self.constants = {}
        self.lists = {}
        self.curves = {}

    def add_constant(self, key, constant):
        self.constants[key] = constant

    def get_constant(self, key):
        return self.constants[key]

    def add_list(self, key, list_object):
        self.lists[key] = list_object

    def get_list(self, key):
        return self.lists[key]

    def add_curve(self, key, curve):
        self.curves[key] = curve

    def get_curve(self, key):
        return self.curves[key]

    def add_environment(self, env):
        # overwrites existing values, if they exist
        for key in env.constants:
            self.constants[key] = env.constants[key]
        for key in env.lists:
            self.lists[key] = env.lists[key]
        for key in env.curves:
            self.curves[key] = env.curves[key]

me_gbm = market_environment('me_gbm', dt.datetime(2015, 1, 1))


me_gbm.add_constant('initial_value', 36.)
me_gbm.add_constant('volatility', 0.2)
me_gbm.add_constant('final_date', dt.datetime(2015, 12, 31))
me_gbm.add_constant('currency', 'EUR')
me_gbm.add_constant('frequency', 'M')
me_gbm.add_constant('paths', 10000)


me_gbm.add_curve('discount_curve', csr)

me_gbm.get_constant('final_date')
