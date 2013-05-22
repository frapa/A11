# -*- encoding: utf-8 -*-

from dati import * 
from matplotlib import pyplot as plt

f1 = plt.figure(figsize=(8, 6))

ax1 = plt.subplot(1, 1, 1)

# dati primo pomeriggio
serie1 = ax1.errorbar(x=theta1, y=h1,
    fmt='o')

# dati secondo lunedì
serie2 = ax1.errorbar(x=theta2, y=h2,
    fmt='o')

ax1.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax1.set_ylabel(ur'Dislivello $h$ [m]', fontsize=14)

ax1.grid(True)

f1.subplots_adjust(left=0.13, bottom=0.15, top=0.85, right=0.93)

plt.show()
