
The tests were able to take in the maximum and minimum value and calculate for all three methods. Since the second method returned a t_obs close to the sample size, the r_obs would've equaled 1, which would invalidate L in the next method. To prevent an undefined answer, I raised an error for L while only testing values up to the .9 value as opposed to the exact sample size value. 

The second class is able to take in the first class and iterate through each of the possible random parameters and varying sample sizes.  

