# -*- encoding: utf-8 -*-

import csv
import sys
from math import *

mpl = False
try:
    import matplotlib
    from matplotlib import pyplot as plt
    mpl = True
except:
    pass


# LETTURA DATI E CALCOLO PARAMETRI
g = 9.806
k_tab = 9.64

masse = []
masse_raw = []
periodi = []
periodi_raw = []
with open("dati/dyn_masse.csv") as f:
    reader = csv.reader(f)
    for n, row in enumerate(reader):
        if n != 0:
            masse_raw.append(row[0])
            masse.append(float(row[0]) / 1000.0)

            periodi_raw.append(row[1:])
            periodi.append([float(p) / 10 for p in row[1:]])

#periodi_2 = [[p**2 for p in ps] for ps in periodi]

N = len(periodi[0])

medie_periodi = [sum(ps)/len(ps) for ps in periodi]
medie_periodi_2 = [p**2 for p in medie_periodi]#[sum(ps)/len(ps) for ps in periodi_2]

sigma_periodi = [sqrt(1.0/(N - 1)*sum([(p - mp)**2 for p in ps])) for ps, mp in zip(periodi, medie_periodi)]
dT = [sqrt(T**2/N + 0.0003**2) for T in sigma_periodi]
sigma_periodi_2 = [2*mp*sp for mp, sp in zip(medie_periodi, dT)]

A =  0.033628
B =  4.0605

#print "\t", "\n\t".join(map(str, medie_periodi_2))

chi_2 = sum([(mp - A - B * m)**2 / sp**2 for mp, m, sp in zip(medie_periodi_2, masse, sigma_periodi_2)])
sigma_chi_teo = sqrt(2*12)
print "chi^2:", chi_2
print "chi^2 teorico:", 12, "pm", sigma_chi_teo

R = abs(chi_2 - 12)
print R
print 2*sigma_chi_teo

sigma_corr = (1.7195e-03, 1.7990e-03, 2.7121e-03, 1.3979e-03, 1.6901e-03, 1.7020e-03, 9.4043e-04, 1.5829e-03, 1.8003e-03, 1.2421e-03,
   1.2172e-03, 1.1279e-03, 1.7244e-03, 2.1260e-03)

if mpl:
    f1 = plt.figure(figsize=(8, 7))
    f1.suptitle("Discrepanza", y=0.93, fontsize=15)

    ax = f1.add_subplot(1, 1, 1)
    dots = ax.errorbar(x=masse, y=[(p - (A + B*m)) * 1000 for p, m in zip(medie_periodi_2, masse)],
        yerr=[sp2 * 1000 for sp2 in sigma_periodi_2], #xerr=sigma_res_p, 
        fmt='o', capsize=7)

    dots2 = ax.errorbar(x=masse, y=[(p - (A + B*m)) * 1000 for p, m in zip(medie_periodi_2, masse)],
        yerr=[sp2 * 1000 for sp2 in sigma_corr], fmt=None, capsize=7)

    for cap in dots[1]:
        cap.set_markeredgewidth(1)

    for cap in dots2[1]:
        cap.set_markeredgewidth(1)

    fit1 = ax.errorbar(x=(0.02, 0.179999), y=(0, 0))
    #fit2 = ax.errorbar(x=(0, 1.4), y=(0, 1.4/k0_s))
    #ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

    ax.set_xlabel(u'Massa [Kg]', labelpad=12, fontsize=14)
    ax.set_ylabel(u'Discrepanza [$\\times 10^{-3} s^2$]', labelpad=6, fontsize=14)
    ax.grid(True)
    ax.set_xticks((0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18))
    ax.set_ylim(-6, 7)

    ax.legend((dots, dots2), ("Incertezza su $T^2$", "Barre d'errore corrette"), 'upper left',
        prop={'size': 12}, numpoints=1)

    f1.subplots_adjust(left=0.13, right=0.93, top=0.85, bottom=0.13)
    
    f2 = plt.figure(figsize=(8, 6))
    f2.suptitle("Periodo quadro al variare della massa", y=0.93, fontsize=15)

    ax2 = f2.add_subplot(1, 1, 1)
    dots = ax2.errorbar(x=masse, y=medie_periodi_2,
        #yerr=sigma_periodi_2, #xerr=sigma_res_p, 
        fmt='o')

    fit1 = ax2.errorbar(x=(-0.01, 0.179999), y=(A + B*-0.01, A + B*0.18))
    #fit2 = ax.errorbar(x=(0, 1.4), y=(0, 1.4/k0_s))
    #ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

    ax2.set_xlabel(u'Massa [Kg]', labelpad=12, fontsize=14)
    ax2.set_ylabel(u'Periodo al quadrato [$s^2$]', labelpad=6, fontsize=14)
    ax2.grid(True)
    ax2.set_xticks((0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18))
    ax2.set_xlim(-0.01, 0.18)
    ax2.set_ylim(0, 0.8)

    ax2.legend((dots, fit1), ("Dati misurati", "Retta di fit"), 'upper left',
        prop={'size': 12})

    f2.subplots_adjust(left=0.13, right=0.93, top=0.85, bottom=0.13)
    
    f3 = plt.figure(figsize=(8, 6))
    f3.suptitle("Periodo al variare della massa", y=0.93, fontsize=15)

    ax3 = f3.add_subplot(1, 1, 1)
    dots = ax3.errorbar(x=masse, y=medie_periodi,
        #yerr=sigma_periodi_2, #xerr=sigma_res_p, 
        fmt='o')

    fit1 = ax3.errorbar(x=[x*0.001 for x in range(20, 181)], y=[(A + 0.001*B*x)**0.5 for x in range(20, 181)])
    #fit2 = ax.errorbar(x=(0, 1.4), y=(0, 1.4/k0_s))
    #ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

    ax3.set_xlabel(u'Massa [Kg]', labelpad=12, fontsize=14)
    ax3.set_ylabel(u'Periodo [s]', labelpad=6, fontsize=14)
    ax3.grid(True)
    #ax3.set_xticks((0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18))
    ax3.set_xlim(0.02, 0.18)
    #ax3.set_ylim(0, 0.8)

    ax3.legend((dots, fit1), ("Dati misurati", "Andamento non lineare"), 'upper left',
        prop={'size': 12})

    f3.subplots_adjust(left=0.13, right=0.93, top=0.85, bottom=0.13)
    
    plt.show()

print " & ".join(masse_raw), "\\\\"
