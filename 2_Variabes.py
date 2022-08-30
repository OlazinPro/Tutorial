from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x **2)

x = np.linspace(-1,5,num=1000)

plt.plot(x,f(x),'green',label="Linea")
plt.xlabel('Eje x')
plt.ylabel('Eje f(x)')
plt.legend()
plt.grid(True)
plt.show()
