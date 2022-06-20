import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

mpl.use('Qt5Agg')

plt.plot(range(10))

plt.show()