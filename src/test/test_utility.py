import numpy as np
import unittest
from src.utils.data import fold_data, normalization, one_hot

class TestUtilities(unittest.TestCase):
    def test_fold_data(self):

        # Validating number of obtained folds and the size of them
        k = 1
        test_data = np.arange(0, 6, 1).reshape(3,2)
        test = fold_data(test_data, k)
        self.assertEqual(len(test),k)
        self.assertEqual([len(x) for x in test],[len(test_data) // k] * k)
        
        # If there is no room for another fold all the remaining elements should be in the last
        k = 2
        test_data = np.arange(0, 10, 1).reshape(5,2)
        test = fold_data(test_data, k)
        self.assertEqual(len(test),k)
        self.assertEqual(len(test[0]),len(test_data) // k)
        self.assertEqual(len(test[1]),3)

        # General case with perfect fit
        k = 3
        test_data = np.arange(0, 24, 1).reshape(12,2)
        test = fold_data(test_data, k)
        self.assertEqual(len(test),k)

    def test_one_hot(self):
        n_cls = 10
        y_data = np.random.randint(0, n_cls, 10)
        encoded = one_hot(y_data, n_cls)

        # Validating unique vector for each class
        self.assertEqual(list(np.sum(encoded,axis=1)),[1]*10)

        # Validating the argmax of the one-hot should match the original value
        self.assertEqual(list(np.argmax(encoded,axis=1)),list(y_data))
    
    def test_normalization(self):
        x_data = np.random.randint(0, 10000, 2000)
        normalized = normalization(x_data)
        
        # Validating default values for lower_bound and higher_bound
        self.assertEqual(np.min(normalized),0)
        self.assertEqual(np.max(normalized),1)

        lower = 2
        higher = 4
        normalized = normalization(x_data,lower_bound=lower,higher_bound=higher)

        # Validating values for lower_bound and higher_bound in specific range
        self.assertEqual(np.min(normalized),lower)
        self.assertEqual(np.max(normalized),higher)
         

       