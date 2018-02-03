import sys
import os
import time
from open_bci_ganglion import OpenBCIBoard
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt

eeg = []
output = open('data.txt','w')

def handle_sample(sample):
    eeg.append(sample.channel_data)
    output.write(','.join([str(s) for s in sample.channel_data])+'\n')

#Establish connection with the board
board = OpenBCIBoard()

#Stream data for 10 seconds
board.start_streaming(handle_sample, 10)
output.close()

eeg = np.array(eeg)
time = np.linspace(0, 10, eeg[:,1].size)

fig,ax = plt.subplots()
ax.plot(time,eeg[:,1])


ax.set(xlabel='time (s)', ylabel='voltage (mV)',title='Ganglion')
ax.grid()

plt.show()
