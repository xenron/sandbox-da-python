# -*- coding: utf-8 -*-

# ## Valuation Classes

# ### European Options

from dx_simulation import *

me_gbm = market_environment('me_gbm', dt.datetime(2015, 1, 1))

me_gbm.add_constant('initial_value', 36.)
me_gbm.add_constant('volatility', 0.2)
me_gbm.add_constant('final_date', dt.datetime(2015, 12, 31))
me_gbm.add_constant('currency', 'EUR')
me_gbm.add_constant('frequency', 'M')
me_gbm.add_constant('paths', 10000)

csr = constant_short_rate('csr', 0.06)

me_gbm.add_curve('discount_curve', csr)

gbm = geometric_brownian_motion('gbm', me_gbm)

me_call = market_environment('me_call', me_gbm.pricing_date)

me_call.add_constant('strike', 40.)
me_call.add_constant('maturity', dt.datetime(2015, 12, 31))
me_call.add_constant('currency', 'EUR')

payoff_func = 'np.maximum(maturity_value - strike, 0)'

from valuation_mcs_european import valuation_mcs_european

eur_call = valuation_mcs_european('eur_call', underlying=gbm,
                        mar_env=me_call, payoff_func=payoff_func)


get_ipython().magic(u'time eur_call.present_value()')

get_ipython().magic(u'time eur_call.delta()')

get_ipython().magic(u'time eur_call.vega()')

get_ipython().run_cell_magic(u'time', u'', u's_list = np.arange(34., 46.1, 2.)\np_list = []; d_list = []; v_list = []\nfor s in s_list:\n    eur_call.update(initial_value=s)\n    p_list.append(eur_call.present_value(fixed_seed=True))\n    d_list.append(eur_call.delta())\n    v_list.append(eur_call.vega())')

from plot_option_stats import plot_option_stats
get_ipython().magic(u'matplotlib inline')

plot_option_stats(s_list, p_list, d_list, v_list)
# tag: option_stats_1
# title: Present value, Delta and Vega estimates for European call option
# size: 75

payoff_func = 'np.maximum(0.33 * (maturity_value + max_value) - 40, 0)'
  # payoff dependent on both the simulated maturity value
  # and the maximum value

eur_as_call = valuation_mcs_european('eur_as_call', underlying=gbm,
                            mar_env=me_call, payoff_func=payoff_func)

get_ipython().run_cell_magic(u'time', u'', u's_list = np.arange(34., 46.1, 2.)\np_list = []; d_list = []; v_list = []\nfor s in s_list:\n    eur_as_call.update(s)\n    p_list.append(eur_as_call.present_value(fixed_seed=True))\n    d_list.append(eur_as_call.delta())\n    v_list.append(eur_as_call.vega())')

plot_option_stats(s_list, p_list, d_list, v_list)
# tag: option_stats_2
# title: Present value, Delta and Vega estimates for European Asian call option
# size: 75


# ### American Options

from dx_simulation import *

me_gbm = market_environment('me_gbm', dt.datetime(2015, 1, 1))

me_gbm.add_constant('initial_value', 36.)
me_gbm.add_constant('volatility', 0.2)
me_gbm.add_constant('final_date', dt.datetime(2016, 12, 31))
me_gbm.add_constant('currency', 'EUR')
me_gbm.add_constant('frequency', 'W')
  # weekly frequency
me_gbm.add_constant('paths', 50000)

csr = constant_short_rate('csr', 0.06)

me_gbm.add_curve('discount_curve', csr)

gbm = geometric_brownian_motion('gbm', me_gbm)

payoff_func = 'np.maximum(strike - instrument_values, 0)'

me_am_put = market_environment('me_am_put', dt.datetime(2015, 1, 1))

me_am_put.add_constant('maturity', dt.datetime(2015, 12, 31))
me_am_put.add_constant('strike', 40.)
me_am_put.add_constant('currency', 'EUR')

from valuation_mcs_american import valuation_mcs_american

am_put = valuation_mcs_american('am_put', underlying=gbm,
                    mar_env=me_am_put, payoff_func=payoff_func)

get_ipython().magic(u'time am_put.present_value(fixed_seed=True, bf=5)')

get_ipython().run_cell_magic(u'time', u'', u'ls_table = []\nfor initial_value in (36., 38., 40., 42., 44.): \n    for volatility in (0.2, 0.4):\n        for maturity in (dt.datetime(2015, 12, 31),\n                         dt.datetime(2016, 12, 31)):\n            am_put.update(initial_value=initial_value,\n                          volatility=volatility,\n                          maturity=maturity)\n            ls_table.append([initial_value,\n                             volatility,\n                             maturity,\n                             am_put.present_value(bf=5)])')

print "S0  | Vola | T | Value"
print 22 * "-"
for r in ls_table:
    print "%d  | %3.1f  | %d | %5.3f" %           (r[0], r[1], r[2].year - 2014, r[3])

am_put.update(initial_value=36.)
am_put.delta()

am_put.vega()




