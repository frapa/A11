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

fit1 = ax1.errorbar(x=(0, 25), y=(A_1, A_1 + B_1*25), color="#77CCFF")
#fit1r1 = ax1.errorbar(x=(0, 25), y=(A_1r1, A_1r1 + B_1r1*25))
#fit1r2 = ax1.errorbar(x=(0, 25), y=(A_1r2, A_1r2 + B_1r2*25))

# dati secondo lunedì
serie2 = ax1.errorbar(x=theta2, y=h2,
    yerr=dh2_corr,
    fmt='.')

fit2 = ax1.errorbar(x=(0, 25), y=(A_2, A_2 + B_2*25), color="#B5E332")
#fit2r1 = ax1.errorbar(x=(0, 25), y=(A_2r1, A_2r1 + B_2r1*25))
#fit2r2 = ax1.errorbar(x=(0, 25), y=(A_2r2, A_2r2 + B_2r2*25))

f1.suptitle(u'Dislivello in funzione della temperatura', fontsize=15, y=0.94)
ax1.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14, labelpad=14)
ax1.set_ylabel(ur'Dislivello $h$ [m]', fontsize=14)

ax1.grid(True)

ax1.legend((serie1, serie2, fit1, fit2), ("Prima serie", "Seconda serie", "Retta di fit", "Retta di fit"),
    prop={'size': 12}, numpoints=1, loc='upper left')

f1.subplots_adjust(left=0.12, bottom=0.13, top=0.87, right=0.95)

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
#fit01r1 = ax2.errorbar(x=(-1, 22), y=(A_1r1 - A_1 + (B_1r1 - B_1)*-1, A_1r1 - A_1 + (B_1r1 - B_1)*22))
#fit01r2 = ax2.errorbar(x=(-1, 22), y=(A_1r2 - A_1 + (B_1r1 - B_1)*-1, A_1r2 - A_1 + (B_1r2 - B_1)*22))

#smeno = ax2.errorbar(x=(-1, 22), y=(A_1r2_meno - A_1 - B_1r2_meno + B_1, A_1r2_meno - A_1 + (B_1r2_meno - B_1)*22))


serie2g = ax3.errorbar(x=theta2g, y=[a - A_2 - B_2*t for t, a in zip(theta2g, h2g)],
    xerr=dtheta, yerr=dh,
    fmt='.', ecolor='r')


serie2s = ax3.errorbar(x=theta2s, y=[a - A_2 - B_2*t for t, a in zip(theta2s, h2s)],
    xerr=dtheta, yerr=dh,
    fmt='.', ecolor='b')

#serie2_corr = ax3.errorbar(x=theta2, y=[a - A_2 - B_2*t for t, a in zip(theta2, h2)],
#    yerr=dh2_corr, fmt=None, capsize=5, ecolor='m')

fit02 = ax3.errorbar(x=(0, 25), y=(0, 0))
#fit02r1 = ax3.errorbar(x=(0, 25), y=(A_2r1 - A_2, A_2r1 - A_2 + (B_2r1 - B_2)*25))
#fit02r2 = ax3.errorbar(x=(0, 25), y=(A_2r2 - A_2, A_2r2 - A_2 + (B_2r2 - B_2)*25))

f2.suptitle(u'Residui della prima serie', fontsize=15, y=0.94)
ax2.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14, labelpad=14)
ax2.set_ylabel(ur'Residuo [m]', fontsize=14)

ax2.set_xlim((-1, 22))
ax2.set_ylim((-0.035, 0.025))

#ax2.legend((serie1g, serie1s, serie1_corr), ("Discesa", "Salita", "Incertezze corrette"),
#    prop={'size': 12}, numpoints=1, loc=8)

f12.suptitle(u'Residui della seconda serie', fontsize=15, y=0.94)
ax3.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14, labelpad=14)
ax3.set_ylabel(ur'Residuo [m]', fontsize=14)

ax2.grid(True)
ax3.grid(True)

f2.subplots_adjust(left=0.12, bottom=0.13, top=0.87, right=0.95, wspace=0.25)
f12.subplots_adjust(left=0.12, bottom=0.13, top=0.87, right=0.95, wspace=0.25)

plt.show()
