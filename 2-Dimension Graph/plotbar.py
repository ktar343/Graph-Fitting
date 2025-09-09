# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 19:29:52 2025

@author: ktar343
"""

import matplotlib.pyplot as plt
import random
import numpy as np

A = np.random.permutation(100)


A = random.sample( range(100), 100 )
x= range(100)  # x value
y= A           # y value      



plt.figure(figsize=(12, 6))
plt.bar(x, y, color='skyblue')
plt.xlabel('Index')
plt.ylabel('Random Value')
plt.title('Random Sample Bar Graph')
plt.grid(True)
plt.show()

