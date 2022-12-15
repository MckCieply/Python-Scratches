#i have constant data and gotta make plot of those
#think box is the best
import numpy as np
import matplotlib as plt
#2 periods of vibration each
#Rod 1
#w/o weights, wide weights, central weights
rod_1 = np.array([[1.65, 1.57, 1.55, 1.65, 1.62],       #w/o weights
                  [3.60, 3.68, 3.60, 3.69, 3.54],       #wide weights
                  [1.84, 1.81, 1.85, 1.81, 1.78]])      #central weights
rod_1 /= 2
#Rod 2
rod_2 = np.array([[1.20, 1.22, 1.22, 1.23, 1.32],       #w/o weights
                  [2.68, 2.64, 2.50, 2.73, 2.79],       #wide weights
                  [2.68, 2.64, 2.50, 2.73, 2.79]])      #central weights
rod_2 /= 2

