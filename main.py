#Main Script 

import numpy as np 
import scipy.optimize as opt 


class EZ_diff(): 
    
    def __init__(self, N, v, a, t): 
        #How can I randomize values for v, a, t given the range of values?
        self.N = N 
        self.v = v 
        self.a = a 
        self.t = t 
    
    def pred_sum_stats(self, a, v, t):
        Y = np.exp(-a * v)

        if Y != -1: 
            r_pred = (1 /Y + 1)
        else: 
            raise ValueError()
        
        if v != 0 and Y != -1: 
            m_pred = (t + (a /(2 * v)) * ((1 - Y)/(1 + Y)))
            v_pred = ((a / 2 * (v**3)) * ((1 - (2 * a * v * Y) - (Y ** 2)) / ((Y + 1) ** 2))
        else: 
            raise ValueError() 
        
    
    def obs_sum_stats(self, N, r_pred): 
        #Find correct math equations to set up this definition 

        t_obs = scipy.binomial()

    def est_params(self): 
        #Find correct equations to set up 



    def est_bias(self): 
        b_v = 
        b_a = 
        b_t = 
        B_square = 
        #Method to check that b == 0 and b 






