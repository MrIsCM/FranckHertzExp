#=======================
#
#         Lord X
#
#       24/11/2021
#
#=======================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from peakdetect import peakdetect


#print("Current working dir: ", os.getcwd())

#==========================================================
#   Read the data and save it as a pandas data frame 
#==========================================================

AllData = pd.read_csv("Datos\AllData.csv", sep=";", skiprows=[0,1, 2])
#print(AllData.head())

#==========================================================
#   Save it as a numpy array. I know better how to work 
#   with numpy arrays
#==========================================================

Data = AllData.to_numpy()
#print(Data)
#print(Data[:,0], Data[:,1])

#==========================================================
#   Get the actual peaks using peakdetect function.
#   Warning: the parameters MUST be optimize for each
#            set of data. Just try.
# 
#   Then format it correctly dividing maxes and mins
#   (print to check, optional) 
#==========================================================

peaks = peakdetect(Data[:,23], Data[:,22], lookahead=1, delta=0.15)
maxes = np.array(peaks[0])
mins = np.array(peaks[1])
print("\nMaximos\n\n", maxes, "\n")
print("\nMinimos\n\n", mins, "\n")


#==========================================================
#   The actual plot:
#       - Create figure (with size)
#       - PLot the data 
#       - Plot the peaks
#       - Labels
#       - Show
#==========================================================


fig = plt.figure(figsize=(13,6))
plt.scatter(Data[:,22], Data[:,23], c='red', marker='x', s=3)
plt.scatter(maxes[:,0], maxes[:,1], c='blue', marker='o', s=10)
plt.scatter(mins[:,0], mins[:,1], c='blue', marker='o', s=10)
plt.ylabel='Voltaje (v)'
plt.xlabel='Intensidad (nA)'
plt.show()