import numpy as np 
import scipy.stats as stats 
import matplotlib.pyplot as plt 
import random


class EZ_diff(): 
    
    def __init__(self, N, v, a, t): 
        #AI Help: Received help for determining how to generate random values for each initialized variable in this class.
        self.N = N 
        self.v = v 
        self.a = a
        self.t = t
    
        """self.v = random.uniform(0.5, 2) 
        self.a = random.uniform(0.5, 2)
        self.t = random.uniform(0.1, 0.5)"""

    def pred_sum_stats(self, a, v, t):
        """Calculates predicted summary stats for R, M, and V"""

        Y = np.exp(-a * v)

        r_pred = (1 /Y + 1)
        m_pred = (t + (a /(2 * v)) * ((1 - Y)/(1 + Y)))
        v_pred = ((a / 2 * (v**3)) * ((1 - (2 * a * v * Y) - (Y ** 2)) / ((Y + 1) ** 2))
        
        return r_pred, m_pred, v_pred 
        
    
    def obs_sum_stats(self, N, r_pred, m_pred, v_pred): 

        t_obs = np.random.binomial(N, r_pred)

        sd = (v_pred / N)
        m_obs = np.random.normal(m_pred, sd)

        sp = (N - 1) / 2
        theta = (2* v_pred) / (N - 1)
        v_obs = np.random.gamma(sp, theta)

        return t_obs, m_obs, v_obs

    
    def est_params(self, r_obs, m_obs): 

        L = np.log10(r_obs / (1 - r_obs))

        ie = (((r_obs)**2 * L) - (r_obs * L) + (r_obs - 0.5))
        v_est = np.sign(r_obs - 0.5) * (((L * ie) / v_obs) ** 0.25)

        a_est = L / v_est 

        exp_minus = 1 - np.exp(-v_est * a_est)
        exp_plus = 1 + np.exp(-v_est * a_est)
        t_est = m_obs - (a_est / (2 * v_est)) * (exp_minus / exp_plus)

        return v_est, a_est, t_est


class calculate_bias: 

    def __init__(self, N, v_est, a_est, t_est): 
        self.v_est = v_est 
        self.a_est = a_est 
        self.t_est = t_est 
        
    def est_bias(self): 
        b_v = 
        b_a = 
        b_t = 
        B_square = 
        #Method to check that b == 0 and b 



    

