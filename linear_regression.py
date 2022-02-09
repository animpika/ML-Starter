import matplotlib.pyplot as plt
from scipy import stats
x = [64, 68, 58, 97, 52, 51]
y = [86, 87, 90, 59, 91, 93]
plt.scatter(x,y)
plt.show()

slope, intercept, r, p, std_err = stats.linregress(x,y)

def mymethod(x):
    return slope*x+intercept


y = mymethod(11)
print(y)