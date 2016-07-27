# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:46:48 2015

@author: Tanmay
"""

import numpy as np


def price_european(strike=100, S0=100, time=1.0,
                   rate=0.5, mu=0.2, steps=50,
                   N=10000, option="call"):
    """
    Calculates the price for European option via Monte-Carlo method
    strike: double
        The strike value for the instrument
    S0: double
        The current price of the instrument
    time: double
        The duration of the option
    rate: double
        The interest rate
    mu: double
        The drift rate
    steps: int
        The number of steps to be evalued in the tenure
    N: long
        The number of simulations to be done for MC simulation
    option: string
        The type of the instrument either put of call
    Returns
    -------
    double
        price of call/put depending upon "type"
    
    """

    dt = time / steps
    print dt
    rand = np.random.standard_normal((steps + 1, N))
    S = np.zeros((steps+1, N))
    S[0] = S0

    for t in range(1, steps+1):
        S[t] = S[t-1] * np.exp((rate-0.5 * mu ** 2) * dt
                               + mu * np.sqrt(dt) * rand[t])
        price_call = (np.exp(-rate * time)
                      * np.sum(np.maximum(S[-1] - strike, 0))/N)
        price_put = (np.exp(-rate * time)
                     * np.sum(np.maximum(strike - S[-1], 0))/N)

    return price_call if option.upper() == "CALL" else price_put

