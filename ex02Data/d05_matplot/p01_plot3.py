import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def g(t):
    return np.sin(np.pi*t)

t1 = np.arange(0.0, 5.0, 0.01)
t2 = np.arange(0.0, 5.0, 0.01)

# 2개의 차트를 동시에 띄우기
plt.figure(1)
plt.plot(t1, f(t1))

plt.figure(2)
plt.plot(t2, g(t2))

plt.show()