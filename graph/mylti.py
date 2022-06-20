import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 1000, 20)
y1 = x ** 2 + 500 * x
y2 = x ** 2
plt.plot(x, y1, 'r o')
plt.plot(x, y2, 'g ^')


plt.xlabel('Подпись по оси Х')
plt.ylabel('Подпись по оси Y')
plt.title('Название графика ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$ Использование специальных символов ')
plt.grid(True)
plt.show()


# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html