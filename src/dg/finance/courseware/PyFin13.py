# -*- coding: utf-8 -*-

# ## Portfolios

# ### Position

from dxa import *

me_gbm = market_environment('me_gbm', dt.datetime(2015, 1, 1))

me_gbm.add_constant('initial_value', 36.)
me_gbm.add_constant('volatility', 0.2)
me_gbm.add_constant('currency', 'EUR')

me_gbm.add_constant('model', 'gbm')


me_am_put = market_environment('me_am_put', dt.datetime(2015, 1, 1))

me_am_put.add_constant('maturity', dt.datetime(2015, 12, 31))
me_am_put.add_constant('strike', 40.)
me_am_put.add_constant('currency', 'EUR')


payoff_func = 'np.maximum(strike - instrument_values, 0)'

am_put_pos = derivatives_position(
             name='am_put_pos',
             quantity=3,
             underlying='gbm',
             mar_env=me_am_put,
             otype='American',
             payoff_func=payoff_func)


am_put_pos.get_info()


# #### Portfolio

me_jd = market_environment('me_jd', me_gbm.pricing_date)

# add jump diffusion specific parameters
me_jd.add_constant('lambda', 0.3)
me_jd.add_constant('mu', -0.75)
me_jd.add_constant('delta', 0.1)
# add other parameters from gbm
me_jd.add_environment(me_gbm)

# needed for portfolio valuation
me_jd.add_constant('model', 'jd')

me_eur_call = market_environment('me_eur_call', me_jd.pricing_date)

me_eur_call.add_constant('maturity', dt.datetime(2015, 6, 30))
me_eur_call.add_constant('strike', 38.)
me_eur_call.add_constant('currency', 'EUR')

payoff_func = 'np.maximum(maturity_value - strike, 0)'

eur_call_pos = derivatives_position(
             name='eur_call_pos',
             quantity=5,
             underlying='jd',
             mar_env=me_eur_call,
             otype='European',
             payoff_func=payoff_func)


underlyings = {'gbm': me_gbm, 'jd' : me_jd}
positions = {'am_put_pos' : am_put_pos, 'eur_call_pos' : eur_call_pos}

# discounting object for the valuation
csr = constant_short_rate('csr', 0.06)


val_env = market_environment('general', me_gbm.pricing_date)
val_env.add_constant('frequency', 'W')
  # monthly frequency
val_env.add_constant('paths', 25000)
val_env.add_constant('starting_date', val_env.pricing_date)
val_env.add_constant('final_date', val_env.pricing_date)
  # not yet known; take pricing_date temporarily
val_env.add_curve('discount_curve', csr)
  # select single discount_curve for whole portfolio

portfolio = derivatives_portfolio(
                name='portfolio',
                positions=positions,
                val_env=val_env,
                assets=underlyings,
                fixed_seed=False)

portfolio.get_statistics(fixed_seed=False)

portfolio.get_statistics(fixed_seed=False)[['pos_value', 'pos_delta', 'pos_vega']].sum()
  # aggregate over all positions

portfolio.get_positions()

portfolio.valuation_objects['am_put_pos'].present_value()

portfolio.valuation_objects['eur_call_pos'].delta()

path_no = 777
path_gbm = portfolio.underlying_objects['gbm'].get_instrument_values()[
                                                            :, path_no]
path_jd = portfolio.underlying_objects['jd'].get_instrument_values()[
                                                            :, path_no]


import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

plt.figure(figsize=(7, 4))
plt.plot(portfolio.time_grid, path_gbm, 'r', label='gbm')
plt.plot(portfolio.time_grid, path_jd, 'b', label='jd')
plt.xticks(rotation=30)
plt.legend(loc=0); plt.grid(True)
# tag: dx_portfolio_1
# title: Non-correlated risk factors

correlations = [['gbm', 'jd', 0.9]]

port_corr = derivatives_portfolio(
                name='portfolio',
                positions=positions,
                val_env=val_env,
                assets=underlyings,
                correlations=correlations,
                fixed_seed=True)

port_corr.get_statistics()

path_gbm = port_corr.underlying_objects['gbm'].            get_instrument_values()[:, path_no]
path_jd = port_corr.underlying_objects['jd'].            get_instrument_values()[:, path_no]


plt.figure(figsize=(7, 4))
plt.plot(portfolio.time_grid, path_gbm, 'r', label='gbm')
plt.plot(portfolio.time_grid, path_jd, 'b', label='jd')
plt.xticks(rotation=30)
plt.legend(loc=0); plt.grid(True)
# tag: dx_portfolio_2
# title: Highly correlated risk factors


pv1 = 5 * port_corr.valuation_objects['eur_call_pos']. present_value(full=True)[1]
pv1


pv2 = 3 * port_corr.valuation_objects['am_put_pos'].present_value(full=True)[1]
pv2

plt.hist([pv1, pv2], bins=25,
         label=['European call', 'American put']);
plt.axvline(pv1.mean(), color='r', ls='dashed',
            lw=1.5, label='call mean = %4.2f' % pv1.mean())
plt.axvline(pv2.mean(), color='r', ls='dotted',
            lw=1.5, label='put mean = %4.2f' % pv2.mean())
plt.xlim(0, 80); plt.ylim(0, 10000)
plt.grid(); plt.legend()
# tag: dx_portfolio_3
# title: Frequency distributions of option position present values

pvs = pv1 + pv2
plt.hist(pvs, bins=50, label='portfolio');
plt.axvline(pvs.mean(), color='r', ls='dashed',
            lw=1.5, label='mean = %4.2f' % pvs.mean())
plt.xlim(0, 80); plt.ylim(0, 7000)
plt.grid(); plt.legend()
# tag: dx_portfolio_4
# title: Portfolio frequency distribution of present values

# portfolio with correlation
pvs.std()

# portfolio without correlation
pv1 = 5 * portfolio.valuation_objects['eur_call_pos'].            present_value(full=True)[1]
pv2 = 3 * portfolio.valuation_objects['am_put_pos'].            present_value(full=True)[1]
(pv1 + pv2).std()


###VSTOXX数据###
#VSTOXX指数数据
import numpy as np
import pandas as pd

url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'
vstoxx_index = pd.read_csv(url, index_col=0, header=2,
                           parse_dates=True, dayfirst=True,
                           sep=',')

vstoxx_index.info()

vstoxx_index = vstoxx_index[('2013/12/31' < vstoxx_index.index)
                            & (vstoxx_index.index < '2014/4/1')]

np.round(vstoxx_index.tail(), 2)


#VSTOXX期货数据
vstoxx_futures = pd.read_excel('d:/data/vstoxx_march_2014.xlsx',
                               'vstoxx_futures')
vstoxx_futures.info()

del vstoxx_futures['A_SETTLEMENT_PRICE_SCALED']
del vstoxx_futures['A_CALL_PUT_FLAG']
del vstoxx_futures['A_EXERCISE_PRICE']
del vstoxx_futures['A_PRODUCT_ID']

columns = ['DATE', 'EXP_YEAR', 'EXP_MONTH', 'PRICE']
vstoxx_futures.columns = columns

import datetime as dt
import calendar

def third_friday(date):
    day = 21 - (calendar.weekday(date.year, date.month, 1) + 2) % 7
    return dt.datetime(date.year, date.month, day)
    
set(vstoxx_futures['EXP_MONTH'])

third_fridays = {}
for month in set(vstoxx_futures['EXP_MONTH']):
    third_fridays[month] = third_friday(dt.datetime(2014, month, 1))
    
third_fridays    

tf = lambda x: third_fridays[x]
vstoxx_futures['MATURITY'] = vstoxx_futures['EXP_MONTH'].apply(tf)

vstoxx_futures.tail()

#VSTOXX期权数据
vstoxx_options = pd.read_excel('d:/data/vstoxx_march_2014.xlsx',
                               'vstoxx_options')
vstoxx_options.info()

del vstoxx_options['A_SETTLEMENT_PRICE_SCALED']
del vstoxx_options['A_PRODUCT_ID']

columns = ['DATE', 'EXP_YEAR', 'EXP_MONTH', 'TYPE', 'STRIKE', 'PRICE']
vstoxx_options.columns = columns

vstoxx_options['MATURITY'] = vstoxx_options['EXP_MONTH'].apply(tf)

vstoxx_options.head()

vstoxx_options['STRIKE'] = vstoxx_options['STRIKE'] / 100.
vstoxx_options.head()

save = True
if save is True:
    import warnings
    warnings.simplefilter('ignore')
    h5 = pd.HDFStore('d:/data/vstoxx_march_2014.h5',
                     complevel=9, complib='blosc')
    h5['vstoxx_index'] = vstoxx_index
    h5['vstoxx_futures'] = vstoxx_futures
    h5['vstoxx_options'] = vstoxx_options
    h5.close()
    
    
###模型检验###
#相关市场数据
pricing_date = dt.datetime(2014, 3, 31)
  # last trading day in March 2014
maturity = third_fridays[10]
  # October maturity
initial_value = vstoxx_index['V2TX'][pricing_date]
  # VSTOXX on pricing_date
forward = vstoxx_futures[(vstoxx_futures.DATE == pricing_date)
            & (vstoxx_futures.MATURITY == maturity)]['PRICE'].values[0]

tol = 0.20
option_selection =     vstoxx_options[(vstoxx_options.DATE == pricing_date)
                 & (vstoxx_options.MATURITY == maturity)
                 & (vstoxx_options.TYPE == 'C')
                 & (vstoxx_options.STRIKE > (1 - tol) * forward)
                 & (vstoxx_options.STRIKE < (1 + tol) * forward)] 

option_selection

#期权建模
from dxa import *

me_vstoxx = market_environment('me_vstoxx', pricing_date)

me_vstoxx.add_constant('initial_value', initial_value)
me_vstoxx.add_constant('final_date', maturity)
me_vstoxx.add_constant('currency', 'EUR')

me_vstoxx.add_constant('frequency', 'B')
me_vstoxx.add_constant('paths', 10000)

csr = constant_short_rate('csr', 0.01)

me_vstoxx.add_curve('discount_curve', csr)

me_vstoxx.add_constant('kappa', 1.0)
me_vstoxx.add_constant('theta', 1.2 * initial_value)
vol_est =  vstoxx_index['V2TX'].std()             * np.sqrt(len(vstoxx_index['V2TX']) / 252.)
me_vstoxx.add_constant('volatility', vol_est)

vol_est

vstoxx_model = square_root_diffusion('vstoxx_model', me_vstoxx)

me_vstoxx.add_constant('strike', forward)
me_vstoxx.add_constant('maturity', maturity)

payoff_func = 'np.maximum(maturity_value - strike, 0)'

vstoxx_eur_call = valuation_mcs_european('vstoxx_eur_call',
                        vstoxx_model, me_vstoxx, payoff_func)

vstoxx_eur_call.present_value()


option_models = {}
for option in option_selection.index:
    strike = option_selection['STRIKE'].ix[option]
    me_vstoxx.add_constant('strike', strike)
    option_models[option] =                         valuation_mcs_european(
                                'eur_call_%d' % strike,
                                vstoxx_model,
                                me_vstoxx,
                                payoff_func)
    
def calculate_model_values(p0):
    ''' Returns all relevant option values.
    
    Parameters
    ===========
    p0 : tuple/list
        tuple of kappa, theta, volatility
    
    Returns
    =======
    model_values : dict
        dictionary with model values
    '''
    kappa, theta, volatility = p0
    vstoxx_model.update(kappa=kappa,
                        theta=theta,
                        volatility=volatility)
    model_values = {}
    for option in option_models:
       model_values[option] = option_models[option].present_value(fixed_seed=True)
    return model_values
    
calculate_model_values((0.5, 27.5, vol_est))
    

#检验过程
i = 0
def mean_squared_error(p0):
    ''' Returns the mean-squared error given
    the model and market values.
    
    Parameters
    ===========
    p0 : tuple/list
        tuple of kappa, theta, volatility
    
    Returns
    =======
    MSE : float
        mean-squared error
    '''
    global i
    model_values = np.array(calculate_model_values(p0).values())
    market_values = option_selection['PRICE'].values
    option_diffs = model_values - market_values
    MSE = np.sum(option_diffs ** 2) / len(option_diffs)
      # vectorized MSE calculation
    if i % 20 == 0:
        if i == 0:
            print '%4s  %6s  %6s  %6s --> %6s' %                  ('i', 'kappa', 'theta', 'vola', 'MSE')
        print '%4d  %6.3f  %6.3f  %6.3f --> %6.3f' %                 (i, p0[0], p0[1], p0[2], MSE)
    i += 1
    return MSE        

mean_squared_error((0.5, 27.5, vol_est))

import scipy.optimize as spo
get_ipython().run_cell_magic(u'time', u'', u'i = 0\nopt_global = spo.brute(mean_squared_error,\n                ((0.5, 3.01, 0.5),  # range for kappa\n                 (15., 30.1, 5.),  # range for theta\n                 (0.5, 5.51, 1)),  # range for volatility\n                 finish=None)')

i = 0
mean_squared_error(opt_global)

get_ipython().run_cell_magic(u'time', u'', u'i = 0\nopt_local = spo.fmin(mean_squared_error, opt_global,\n                     xtol=0.00001, ftol=0.00001,\n                     maxiter=100, maxfun=350)')

i = 0
mean_squared_error(opt_local)

calculate_model_values(opt_local)

pd.options.mode.chained_assignment = None
option_selection['MODEL'] =  np.array(calculate_model_values(opt_local).values())
option_selection['ERRORS'] = option_selection['MODEL'] - option_selection['PRICE']

option_selection[['MODEL', 'PRICE', 'ERRORS']]

round(option_selection['ERRORS'].mean(), 3)


import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
fix, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(8, 8))
strikes = option_selection['STRIKE'].values
ax1.plot(strikes, option_selection['PRICE'], label='market quotes')
ax1.plot(strikes, option_selection['MODEL'], 'ro', label='model values')
ax1.set_ylabel('option values')
ax1.grid(True)
ax1.legend(loc=0)
wi = 0.25
ax2.bar(strikes - wi / 2., option_selection['ERRORS'],
        label='market quotes', width=wi)
ax2.grid(True)
ax2.set_ylabel('differences')
ax2.set_xlabel('strikes')


###基于VSTOXX的美式期权###
#期权头寸建模
me_vstoxx = market_environment('me_vstoxx', pricing_date)
me_vstoxx.add_constant('initial_value', initial_value)
me_vstoxx.add_constant('final_date', pricing_date)
me_vstoxx.add_constant('currency', 'NONE')

me_vstoxx.add_constant('kappa', opt_local[0])
me_vstoxx.add_constant('theta', opt_local[1])
me_vstoxx.add_constant('volatility', opt_local[2])

me_vstoxx.add_constant('model', 'srd')

payoff_func = 'np.maximum(strike - instrument_values, 0)'


shared = market_environment('share', pricing_date)
shared.add_constant('maturity', maturity)
shared.add_constant('currency', 'EUR')

option_positions = {}
  # dictionary for option positions
option_environments = {}
  # dictionary for option environments
for option in option_selection.index:
    option_environments[option] =         market_environment('am_put_%d' % option, pricing_date)
        # define new option environment, one for each option
    strike = option_selection['STRIKE'].ix[option]
      # pick the relevant strike
    option_environments[option].add_constant('strike', strike)
      # add it to the environment
    option_environments[option].add_environment(shared)
      # add the shared data
    option_positions['am_put_%d' % strike] =                     derivatives_position(
                        'am_put_%d' % strike,
                        quantity=100.,
                        underlying='vstoxx_model',
                        mar_env=option_environments[option],
                        otype='American',
                        payoff_func=payoff_func)

#期权投资组合    
val_env = market_environment('val_env', pricing_date)
val_env.add_constant('starting_date', pricing_date)
val_env.add_constant('final_date', pricing_date)
  # temporary value, is updated during valuation
val_env.add_curve('discount_curve', csr)
val_env.add_constant('frequency', 'B')
val_env.add_constant('paths', 25000)    

underlyings = {'vstoxx_model' : me_vstoxx}

portfolio = derivatives_portfolio('portfolio', option_positions,
                                  val_env, underlyings)

get_ipython().magic(u'time results = portfolio.get_statistics(fixed_seed=True)')


results.sort(columns='name')


results[['pos_value','pos_delta','pos_vega']].sum()
