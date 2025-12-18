import matplotlib.pyplot as plt
import numpy as np


step = 2000
total_time = 5
dt = total_time / step
position = np.loadtxt('results.csv') # loadtxt converts all this file 
# directly in numbers

time = np.linspace(0, total_time, step)

# print('\n'.join(position.readlines()))
print(position[:5])

plt.plot(time, position)
plt.show()