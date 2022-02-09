import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(2,8,25)
y = np.random.normal(5,2,100000)
plt.hist(y,500)
plt.show()