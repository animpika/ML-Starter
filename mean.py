import numpy as np
speed = [1,2,2,2,3,3,4,4,5,6]
mn = np.mean(speed)
print(mn)
md = np.median(speed)
print(md)
from scipy import stats
modu = stats.mode(speed)
print(f"Mode is {modu[0]}, count is {modu[1]}")
varian = np.var(speed)
print(varian)
std_dev = np.std(speed)
print(std_dev)