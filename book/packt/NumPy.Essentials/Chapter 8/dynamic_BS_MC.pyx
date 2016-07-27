
import numpy as np

def price_european_cython(double strike = 100,double S0 = 100,
                          double time = 1.0, double rate = 0.5,
                          double mu = 0.2, int steps = 50, 
                          long N = 10000, char* option = "call"):
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

    cdef double dt = time / steps
    rand = np.random.standard_normal((steps + 1, N))
    S = np.zeros((steps+1, N));
    S[0] = S0

    for t in range(1,steps+1):
        S[t] = S[t-1] * np.exp((rate-0.5 * mu ** 2) * dt
                               + mu * np.sqrt(dt) * rand[t])

        price_call = (np.exp(-rate * time)
                      * np.sum(np.maximum(S[-1] - strike, 0))/N)
        price_put = (np.exp(-rate * time)
                     * np.sum(np.maximum(strike - S[-1], 0))/N)

        return price_call if option.upper() == "CALL" else price_put
