import unittest 
from unittest.mock import patch 
from main.py import EZ_diff
import numpy as np 


class test_ez_diff_function(unittest.TestCase): 

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
    
    #ChatGPT assistance for learning how to test distributions
    
    @patch('np.random.binomial')
    @patch('np.random.normal')
    @patch('np.random.gamma')
    def test_obs_sum_min_10(self, mock_binomial, mock_normal, mock_gamma): 
        mock_binomial.return_value = 5
        mock_normal.return_value = 0.724353
        mock_gamma.return_value = 0.00004

        N = 10
        t_obs_result, m_obs_result, v_obs_result = self.EZ.obs_sum_stats(10, 0.562176, 0.724353, 0.000040) 

        self.assertEqual(t_obs_result, 5)
        self.assertEqual(m_obs_result, 0.724353)
        self.assertEqual(v_obs_result, 0.00004)
    
    @patch('np.random.binomial')
    @patch('np.random.normal')
    @patch('np.random.gamma')
    def test_obs_sum_min_40(self): 
        mock_binomial.return_value = 22
        mock_normal.return_value = 0.724353
        mock_gamma.return_value = 0.00004

        N = 40
        t_obs_result, m_obs_result, v_obs_result = self.EZ.obs_sum_stats(40, 0.562176, 0.724353, 0.000040) 

        self.assertEqual(t_obs_result, 22)
        self.assertEqual(m_obs_result, 0.724353)
        self.assertEqual(v_obs_result, 0.00004)

    @patch('np.random.binomial')
    @patch('np.random.normal')
    @patch('np.random.gamma')
    def test_obs_sum_min_4000(self): 
        mock_binomial.return_value = 2249
        mock_normal.return_value = 0.724353
        mock_gamma.return_value = 0.00004

        N = 4000
        t_obs_result, m_obs_result, v_obs_result = self.EZ.obs_sum_stats(4000, 0.562176, 0.724353, 0.000040) 

        self.assertEqual(t_obs_result, 2249)
        self.assertEqual(m_obs_result, 0.724353)
        self.assertEqual(v_obs_result, 0.00004)
    
    @patch('np.random.binomial')
    @patch('np.random.normal')
    @patch('np.random.gamma')
    def test_obs_sum_max_10(self): 

        mock_binomial.return_value = 10
        mock_normal.return_value = 0.9820184
        mock_gamma.return_value = 6.5817792

        N = 10
        t_obs_result, m_obs_result, v_obs_result = self.EZ.obs_sum_stats(10, 0.9820184, 0.9820184, 6.5817792) 

        self.assertEqual(t_obs_result, 10)
        self.assertEqual(m_obs_result, 0.9820184)
        self.assertEqual(v_obs_result, 6.5817792)
    
    @patch('np.random.binomial')
    @patch('np.random.normal')
    @patch('np.random.gamma')
    def test_obs_sum_max_40(self): 

        mock_binomial.return_value = 40
        mock_normal.return_value = 0.9820184
        mock_gamma.return_value = 6.5817792

        N = 40
        t_obs_result, m_obs_result, v_obs_result = self.EZ.obs_sum_stats(40, 0.9820184, 0.9820184, 6.5817792) 

        self.assertEqual(t_obs_result, 40)
        self.assertEqual(m_obs_result, 0.9820184)
        self.assertEqual(v_obs_result, 6.5817792) 

    @patch('np.random.binomial')
    @patch('np.random.normal')
    @patch('np.random.gamma')
    def test_obs_sum_max_4000(self): 

        mock_binomial.return_value = 4000
        mock_normal.return_value = 0.9820184
        mock_gamma.return_value = 6.5817792

        N = 4000
        t_obs_result, m_obs_result, v_obs_result = self.EZ.obs_sum_stats(4000, 0.9820184, 0.9820184, 6.5817792) 

        self.assertEqual(t_obs_result, 4000)
        self.assertEqual(m_obs_result, 0.9820184)
        self.assertEqual(v_obs_result, 6.5817792)
        



if __name__ == '__main__': 

    unittest.main() #Help from ChatGPT vor double-checking