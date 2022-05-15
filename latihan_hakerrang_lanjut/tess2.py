import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def f(x):
    y = x**2
    return y


def f2(x):
    y = x**3 + x**2 + x
    return y


# membuat animasi grafikasi
for i in range(100):
    plt.scatter(i, f(i))
    plt.grid(True)
    plt.pause(0.1)
plt.show()
