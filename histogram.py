# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 05:30:32 2017

@author: BALASUBRAMANIAM
"""

import matplotlib.pyplot as plt
import numpy as np

plt.hist([1, 2, 1], bins=[0, 1, 2, 3])
plt.show()


#x = np.random.normal(size = 1000)

#plt.hist(x, normed=True, bins=30)
#plt.ylabel('Probability')
#plt.show()


'''
#cumulative histogram 
plt.hist(x, 
         bins=100, 
         normed=True,
         stacked=True,
         cumulative=True)
plt.show()


plt.hist(x, 
         bins=100, 
         normed=True, 
         stacked=True, 
         )
plt.show()
'''
