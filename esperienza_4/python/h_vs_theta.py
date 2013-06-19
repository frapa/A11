# -*- encoding: utf-8 -*-

from dati import * 
from matplotlib import pyplot as plt

# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
f1 = plt.figure(figsize=(8, 8))

ax1 = f1.add_subplot(1, 1, 1)

# dati primo pomeriggio
serie1r1 = ax1.errorbar(x=T1r1, y=H1r1,
    yerr=dh1r1_tot_corr,
    fmt='.')

serie1r2 = ax1.errorbar(x=T1r2, y=H1r2,
    yerr=dh1r2_tot_corr_meno,
    fmt='.')

#fit1 = ax1.errorbar(x=(0, 25), y=(A_1, A_1 + B_1*25))
fit1r1 = ax1.errorbar(x=(-1, 25), y=(A_1r1 - B_1r1, A_1r1 + B_1r1*25), color="#77CCFF")
fit1r2 = ax1.errorbar(x=(-1, 25), y=(A_1r2 - B_1r2, A_1r2 + B_1r2*25), color="#B5E332")

# dati secondo lunedì
serie2r1 = ax1.errorbar(x=T2r1, y=H2r1,
    yerr=dh2r1_tot_corr,
    fmt='.')

serie2r2 = ax1.errorbar(x=T2r2, y=H2r2,
    yerr=dh2r2_tot_corr,
    fmt='.', color="#800080")

#fit2 = ax1.errorbar(x=(0, 25), y=(A_2, A_2 + B_2*25))
fit2r1 = ax1.errorbar(x=(-1, 25), y=(A_2r1 - B_2r1, A_2r1 + B_2r1*25), color='#FFA500')
fit2r2 = ax1.errorbar(x=(-1, 25), y=(A_2r2 - B_2r2, A_2r2 + B_2r2*25), color="#D370FF")

ax1.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax1.set_ylabel(ur'Dislivello $d$ [m]', fontsize=14)

ax1.set_xlim((-1, 25))
ax1.set_ylim((-0.9, 0.1))

ax1.legend((serie1r1, fit1r1, serie1r2, fit1r2, serie2r1, fit2r1, serie2r2, fit2r2),
    ("Gruppo 1", "Fit gruppo 1", "Gruppo 2", "Fit gruppo 2", "Gruppo 3", "Fit gruppo 3", "Gruppo 4", "Fit gruppo 4"),
    prop={'size': 12}, numpoints=1, loc='upper left')

f1.suptitle("Rette di fit dei residui", fontsize=15, y=0.96)

ax1.grid(True)

f1.subplots_adjust(left=0.13, bottom=0.1, top=0.90, right=0.93)

# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
f2 = plt.figure(figsize=(9, 6))
f12 = plt.figure(figsize=(9, 6))

ax2 = f2.add_subplot(1, 1, 1)
ax3 = f12.add_subplot(1, 1, 1)

# dati primo pomeriggio
serie1r1 = ax2.errorbar(x=T1r1, y=[a - A_1 - B_1*t for t, a in zip(T1r1, H1r1)],
    yerr=dh1r1_tot_corr, fmt='.', capsize=5)

serie1r2 = ax2.errorbar(x=T1r2, y=[a - A_1 - B_1*t for t, a in zip(T1r2, H1r2)],
    yerr=dh1r2_tot_corr_meno, fmt='.', capsize=5)


#serie1_corr = ax2.errorbar(x=theta1, y=[a - A_1 - B_1*t for t, a in zip(theta1, h1)],
#    yerr=dh1_corr, fmt=None, capsize=5, ecolor='m')

#serie1s_corr = ax2.errorbar(x=theta1s, y=[a - A_1 - B_1*t for t, a in zip(theta1s, h1s)],
#    yerr=dh1_corr, fmt=None, capsize=5)

fit01 = ax2.errorbar(x=(-1, 22), y=(0, 0))
fit01r1 = ax2.errorbar(x=(-1, 22), y=(A_1r1 - A_1 + (B_1r1 - B_1)*-1, A_1r1 - A_1 + (B_1r1 - B_1)*22), color="#77CCFF")
#fit01r2 = ax2.errorbar(x=(-1, 22), y=(A_1r2 - A_1 + (B_1r1 - B_1)*-1, A_1r2 - A_1 + (B_1r2 - B_1)*22))

smeno = ax2.errorbar(x=(-1, 22), y=(A_1r2_meno - A_1 - B_1r2_meno + B_1, A_1r2_meno - A_1 + (B_1r2_meno - B_1)*22), color="#B5E332")

ax2.legend((fit01, serie1r1, fit01r1, serie1r2, smeno),
    ("Retta di fit serie 1", "Gruppo 1", "Fit gruppo 1", "Gruppo 2", "Fit gruppo 2"),
    prop={'size': 12}, numpoints=1, loc='lower center')

serie2g = ax3.errorbar(x=T2r1, y=[a - A_2 - B_2*t for t, a in zip(T2r1, H2r1)],
    yerr=dh2r1_tot_corr,
    fmt='.', capsize=5, color='r')


serie2s = ax3.errorbar(x=T2r2, y=[a - A_2 - B_2*t for t, a in zip(T2r2, H2r2)],
    yerr=dh2r2_tot_corr,
    fmt='.', capsize=5, color="#800080")

#serie2_corr = ax3.errorbar(x=theta2, y=[a - A_2 - B_2*t for t, a in zip(theta2, h2)],
#    yerr=dh2_corr, fmt=None, capsize=5, ecolor='m')

fit02 = ax3.errorbar(x=(0, 25), y=(0, 0), color="#44AA00")
fit02r1 = ax3.errorbar(x=(0, 25), y=(A_2r1 - A_2, A_2r1 - A_2 + (B_2r1 - B_2)*25), color='#FFA500')
fit02r2 = ax3.errorbar(x=(0, 25), y=(A_2r2 - A_2, A_2r2 - A_2 + (B_2r2 - B_2)*25), color="#D370FF")

ax2.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax2.set_ylabel(ur'Residuo [m]', fontsize=14)

ax2.set_xlim((-1, 22))
ax2.set_ylim((-0.025, 0.020))

#ax2.legend((serie1g, serie1s, serie1_corr), ("Discesa", "Salita", "Incertezze corrette"),
#    prop={'size': 12}, numpoints=1, loc=8)

ax3.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
ax3.set_ylabel(ur'Residuo [m]', fontsize=14)

ax3.set_ylim((-0.035, 0.04))
ax3.set_xlim((1, 25))

ax3.legend((fit02, serie2r1, fit02r1, serie2r2, fit02r2),
    ("Retta di fit serie 2", "Gruppo 3", "Fit gruppo 3", "Gruppo 4", "Fit gruppo 4"),
    prop={'size': 12}, numpoints=1, loc='upper center')

f2.suptitle("Sottoserie della serie 1", fontsize=15, y=0.94)
f12.suptitle("Sottoserie della serie 2", fontsize=15, y=0.94)

ax2.grid(True)
ax3.grid(True)

f2.subplots_adjust(left=0.10, bottom=0.15, top=0.85, right=0.95, wspace=0.25)
f12.subplots_adjust(left=0.10, bottom=0.15, top=0.85, right=0.95, wspace=0.25)

## XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
#f4 = plt.figure(figsize=(8, 6))
#
#ax6 = f4.add_subplot(1, 1, 1)
#
## dati primo pomeriggio
#serie41 = ax6.errorbar(x=theta1, y=p1,
#    fmt='.')
#
#fit41 = ax6.errorbar(x=(0, 25), y=(88634, 88634 + 372.42*25))
#
## dati secondo lunedì
#serie42 = ax6.errorbar(x=theta2, y=p2,
#    fmt='.')
#    
#fit42 = ax6.errorbar(x=(0, 25), y=(87792, 87792 + 400.76*25))
#
#ax6.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
#ax6.set_ylabel(ur'Pressione $P$ [Pa]', fontsize=14)
#
#ax6.grid(True)
#
#f4.subplots_adjust(left=0.13, bottom=0.15, top=0.85, right=0.93)
#
## XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
#f3 = plt.figure(figsize=(12, 6))
#
#ax4 = f3.add_subplot(1, 2, 1)
#ax5 = f3.add_subplot(1, 2, 2)
#
## dati primo pomeriggio
#serie31 = ax4.errorbar(x=theta1, y=[a - p_A1 - p_B1*t for t, a in zip(theta1, p1)],
#    xerr=dtheta, yerr=dh,
#    fmt='.')
#
#fit31 = ax4.errorbar(x=(0, 25), y=(0, 0))
#
#serie32 = ax5.errorbar(x=theta2, y=[a - p_A2 - p_B2*t for t, a in zip(theta2, p2)],
#    xerr=dtheta, yerr=dh,
#    fmt='.')
#
#fit32 = ax5.errorbar(x=(0, 25), y=(0, 0))
#
#ax4.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
#ax4.set_ylabel(ur'Residuo [Pa]', fontsize=14)
#
#ax5.set_xlabel(ur'Temperatura $\theta$ [°C]', fontsize=14)
#ax5.set_ylabel(ur'Residuo [Pa]', fontsize=14)
#
#ax4.grid(True)
#ax5.grid(True)
#
#f3.subplots_adjust(left=0.13, bottom=0.15, top=0.85, right=0.93, wspace=0.2)
#
plt.show()
