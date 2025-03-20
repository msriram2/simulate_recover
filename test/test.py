# Test File 

import unittest 
from main.py import EZ_diff()

class test_ez_diff_function(unittest.TestCase): 

    #0.778801

    def setUp_EZ_diff(self): 
        self.EZ = EZ_diff() #Help from ChatGPT 

    def test_pred_sum_min(self): 
        r_pred_result, m_pred_result, v_pred_result = self.EZ.pred_sum_stats(0.5, 0.5, 0.1)
        self.assertEqual(r_pred_result, 0.562176)
        self.assertEqual(m_pred_result, 0.724353)
        self.assertEqual(v_pred_result, 0.000040)
    
    def test_pred_sum_max(self): 
        r_pred_result, m_pred_result, v_pred_result = self.EZ.pred_sum_stats(2, 2, 0.5)
        self.assertEqual(r_pred_result, 0.9820184)
        self.assertEqual(m_pred_result, 0.9820184)
        self.assertEqual(v_pred_result, 6.5817792)

