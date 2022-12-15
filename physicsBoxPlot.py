#i have constant data and gotta make plot of those
#think box is the best
import numpy as np
import matplotlib as plt
#2 periods of vibration each
#Rod 1
#w/o weights
measur_11 = np.array([1.65, 1.57, 1.55, 1.65, 1.62])
measur_11 /= 2
#w wide weights
measur_12 = np.array([3.60, 3.68, 3.60, 3.69, 3.54])
measur_12 /= 2
#w central weights
measur_13 = np.array([1.84, 1.81, 1.85, 1.81, 1.78])
measur_13 /= 2
#Rod 2
#w/o weights
measur_21 = np.array([1.20, 1.22, 1.22, 1.23, 1.32])
measur_21 /= 2
#w wide weights
measur_22 = np.array([2.68, 2.64, 2.50, 2.73, 2.79])
measur_22 /= 2
#w central weights
measur_23 = np.array([1.38, 1.34, 1.38, 1.34, 1.29])
measur_22 /= 2

