# -*- encoding: utf-8 -*-

from dati import * 
from matplotlib import pyplot as plt

# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
f1 = plt.figure(figsize=(8, 6))

ax1 = f1.add_subplot(1, 1, 1)

# dati primo pomeriggio
serie1 = ax1.errorbar(x=theta1, y=h1,
    yerr=dh1_corr,
    fmt='.')

fit1 = ax1.errorbar(x=(0, 25), y=(A_1, A_1 + B_1*25))
fit1r1 = ax1.errorbar(x=(0, 25), y=(A_1r1, A_1r1 + B_1r1*25))
fit1r2 = ax1.errorbar(x=(0, 25), y=(A_1r2, A_1r2 + B_1r2*25))

# dati secondo lunedì
serie2 = ax1.errorbar(x=theta2, y=h2,
    yerr=dh2_corr,
    fmt='.')

fit2 = ax1.errorbar(x=(0, 25), y=(A_2, A_2 + B_2*25))
fit2r1 = ax1.errorbar(x=(0, 25), y=(A_2r1, A_2r1 + B_2r1*25))
fit2r2 = ax1.errorbar(x=(0, 25), y=(A_2r2, A_2r2 + B_2r2*25))

ax1.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax1.set_ylabel(ur'Dislivello $h$ [m]', fontsize=14)

ax1.grid(True)

f1.subplots_adjust(left=0.13, bottom=0.15, top=0.85, right=0.93)

# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
f2 = plt.figure(figsize=(9, 6))
f12 = plt.figure(figsize=(9, 6))

ax2 = f2.add_subplot(1, 1, 1)
ax3 = f12.add_subplot(1, 1, 1)

# dati primo pomeriggio
serie1g = ax2.errorbar(x=theta1g, y=[a - A_1 - B_1*t for t, a in zip(theta1g, h1g)],
    yerr=dh, fmt='.', capsize=5)

serie1s = ax2.errorbar(x=theta1s, y=[a - A_1 - B_1*t for t, a in zip(theta1s, h1s)],
    yerr=dh, fmt='.', capsize=5)


#serie1_corr = ax2.errorbar(x=theta1, y=[a - A_1 - B_1*t for t, a in zip(theta1, h1)],
#    yerr=dh1_corr, fmt=None, capsize=5, ecolor='m')

#serie1s_corr = ax2.errorbar(x=theta1s, y=[a - A_1 - B_1*t for t, a in zip(theta1s, h1s)],
#    yerr=dh1_corr, fmt=None, capsize=5)

fit01 = ax2.errorbar(x=(-1, 22), y=(0, 0))
fit01r1 = ax2.errorbar(x=(-1, 22), y=(A_1r1 - A_1 + (B_1r1 - B_1)*-1, A_1r1 - A_1 + (B_1r1 - B_1)*22))
fit01r2 = ax2.errorbar(x=(-1, 22), y=(A_1r2 - A_1 + (B_1r1 - B_1)*-1, A_1r2 - A_1 + (B_1r2 - B_1)*22))

smeno = ax2.errorbar(x=(-1, 22), y=(A_1r2_meno - A_1 - B_1r2_meno + B_1, A_1r2_meno - A_1 + (B_1r2_meno - B_1)*22))


serie2g = ax3.errorbar(x=theta2g, y=[a - A_2 - B_2*t for t, a in zip(theta2g, h2g)],
    xerr=dtheta, yerr=dh,
    fmt='.', ecolor='r')


serie2s = ax3.errorbar(x=theta2s, y=[a - A_2 - B_2*t for t, a in zip(theta2s, h2s)],
    xerr=dtheta, yerr=dh,
    fmt='.', ecolor='b')

#serie2_corr = ax3.errorbar(x=theta2, y=[a - A_2 - B_2*t for t, a in zip(theta2, h2)],
#    yerr=dh2_corr, fmt=None, capsize=5, ecolor='m')

fit02 = ax3.errorbar(x=(0, 25), y=(0, 0))
fit02r1 = ax3.errorbar(x=(0, 25), y=(A_2r1 - A_2, A_2r1 - A_2 + (B_2r1 - B_2)*25))
fit02r2 = ax3.errorbar(x=(0, 25), y=(A_2r2 - A_2, A_2r2 - A_2 + (B_2r2 - B_2)*25))

ax2.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax2.set_ylabel(ur'Residuo [m]', fontsize=14)

ax2.set_xlim((-1, 22))
ax2.set_ylim((-0.035, 0.025))

#ax2.legend((serie1g, serie1s, serie1_corr), ("Discesa", "Salita", "Incertezze corrette"),
#    prop={'size': 12}, numpoints=1, loc=8)

ax3.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax3.set_ylabel(ur'Residuo [m]', fontsize=14)

ax2.grid(True)
ax3.grid(True)

f2.subplots_adjust(left=0.10, bottom=0.15, top=0.85, right=0.95, wspace=0.25)
f12.subplots_adjust(left=0.10, bottom=0.15, top=0.85, right=0.95, wspace=0.25)

# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
f4 = plt.figure(figsize=(8, 6))

ax6 = f4.add_subplot(1, 1, 1)

# dati primo pomeriggio
serie41 = ax6.errorbar(x=theta1, y=p1,
    fmt='.')

fit41 = ax6.errorbar(x=(0, 25), y=(88634, 88634 + 372.42*25))

# dati secondo lunedì
serie42 = ax6.errorbar(x=theta2, y=p2,
    fmt='.')
    
fit42 = ax6.errorbar(x=(0, 25), y=(87792, 87792 + 400.76*25))

ax6.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax6.set_ylabel(ur'Pressione $P$ [Pa]', fontsize=14)

ax6.grid(True)

f4.subplots_adjust(left=0.13, bottom=0.15, top=0.85, right=0.93)

# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
f3 = plt.figure(figsize=(12, 6))

ax4 = f3.add_subplot(1, 2, 1)
ax5 = f3.add_subplot(1, 2, 2)

# dati primo pomeriggio
serie31 = ax4.errorbar(x=theta1, y=[a - p_A1 - p_B1*t for t, a in zip(theta1, p1)],
    xerr=dtheta, yerr=dh,
    fmt='.')

fit31 = ax4.errorbar(x=(0, 25), y=(0, 0))

serie32 = ax5.errorbar(x=theta2, y=[a - p_A2 - p_B2*t for t, a in zip(theta2, p2)],
    xerr=dtheta, yerr=dh,
    fmt='.')

fit32 = ax5.errorbar(x=(0, 25), y=(0, 0))

ax4.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax4.set_ylabel(ur'Residuo [Pa]', fontsize=14)

ax5.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax5.set_ylabel(ur'Residuo [Pa]', fontsize=14)

ax4.grid(True)
ax5.grid(True)

f3.subplots_adjust(left=0.13, bottom=0.15, top=0.85, right=0.93, wspace=0.2)

plt.show()
