# -*- encoding: utf-8 -*-

from dati import * 
from matplotlib import pyplot as plt

# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
f1 = plt.figure(figsize=(8, 6))

ax1 = f1.add_subplot(1, 1, 1)

# dati primo pomeriggio
serie1 = ax1.errorbar(x=theta1, y=h1,
    fmt='.')

fit1 = ax1.errorbar(x=(0, 25), y=(A_1, A_1 + B_1*25))

# dati secondo lunedì
serie2 = ax1.errorbar(x=theta2, y=h2,
    fmt='.')
    
fit2 = ax1.errorbar(x=(0, 25), y=(A_2, A_2 + B_2*25))

ax1.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax1.set_ylabel(ur'Dislivello $h$ [m]', fontsize=14)

ax1.grid(True)

f1.subplots_adjust(left=0.13, bottom=0.15, top=0.85, right=0.93)

# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
f2 = plt.figure(figsize=(12, 6))

ax2 = f2.add_subplot(1, 2, 1)
ax3 = f2.add_subplot(1, 2, 2)

# dati primo pomeriggio
serie1g = ax2.errorbar(x=theta1g, y=[a - A_1 - B_1*t for t, a in zip(theta1g, h1g)],
    xerr=dtheta, yerr=dh,
    fmt='.')

serie1s = ax2.errorbar(x=theta1s, y=[a - A_1 - B_1*t for t, a in zip(theta1s, h1s)],
    xerr=dtheta, yerr=dh,
    fmt='.')

fit01 = ax2.errorbar(x=(0, 25), y=(0, 0))

serie2g = ax3.errorbar(x=theta2g, y=[a - A_2 - B_2*t for t, a in zip(theta2g, h2g)],
    xerr=dtheta, yerr=dh,
    fmt='.')


serie2s = ax3.errorbar(x=theta2s, y=[a - A_2 - B_2*t for t, a in zip(theta2s, h2s)],
    xerr=dtheta, yerr=dh,
    fmt='.')

fit02 = ax3.errorbar(x=(0, 25), y=(0, 0))

ax2.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax2.set_ylabel(ur'Dislivello $h$ [m]', fontsize=14)

ax3.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax3.set_ylabel(ur'Dislivello $h$ [m]', fontsize=14)

ax2.grid(True)
ax3.grid(True)

f2.subplots_adjust(left=0.10, bottom=0.15, top=0.85, right=0.95, wspace=0.25)

# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
f3 = plt.figure(figsize=(12, 6))

ax4 = f3.add_subplot(1, 2, 1)
ax5 = f3.add_subplot(1, 2, 2)

# dati primo pomeriggio
serie1 = ax4.errorbar(x=theta1, y=[a - A_1 - B_1*t for t, a in zip(theta1, h1)],
    xerr=dtheta, yerr=dh,
    fmt='.')

fit01 = ax4.errorbar(x=(0, 25), y=(0, 0))

serie2 = ax5.errorbar(x=theta2, y=[a - A_2 - B_2*t for t, a in zip(theta2, h2)],
    xerr=dtheta, yerr=dh,
    fmt='.')

fit02 = ax5.errorbar(x=(0, 25), y=(0, 0))

ax4.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax4.set_ylabel(ur'Dislivello $h$ [m]', fontsize=14)

ax5.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax5.set_ylabel(ur'Dislivello $h$ [m]', fontsize=14)

ax4.grid(True)
ax5.grid(True)

f3.subplots_adjust(left=0.13, bottom=0.15, top=0.85, right=0.93, wspace=0.2)

plt.show()
