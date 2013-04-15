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
periodi = []
with open("dati/dyn_masse.csv") as f:
    reader = csv.reader(f)
    for n, row in enumerate(reader):
        if n != 0:
            masse.append(float(row[0]) / 1000.0)

            periodi.append([float(p) / 10 for p in row[1:]])

#periodi_2 = [[p**2 for p in ps] for ps in periodi]

medie_periodi = [sum(ps)/len(ps) for ps in periodi]
medie_periodi_2 = [p**2 for p in medie_periodi]#[sum(ps)/len(ps) for ps in periodi_2]

sigma_periodi = [sqrt(1.0/(len(periodi[0]) - 1)*sum([(p - mp)**2 for p in ps])) for ps, mp in zip(periodi, medie_periodi)]
sigma_periodi_2 = [2*mp*sp for mp, sp in zip(medie_periodi, sigma_periodi)]

A =  0.033628
B =  4.0605

#print "\t", "\n\t".join(map(str, medie_periodi_2))

chi_2 = sum([(mp - A - B * m)**2 / sp**2 for mp, m, sp in zip(medie_periodi_2, masse, sigma_periodi_2)])
print chi_2

if mpl:
    f1 = plt.figure(figsize=(8, 6))
    f1.suptitle("Pesi e allungamenti", y=0.93, fontsize=15)

    ax = f1.add_subplot(1, 1, 1)
    dots = ax.errorbar(x=masse, y=medie_periodi_2, #[p - (A + B*m) for p, m in zip(medie_periodi_2, masse)],
        yerr=sigma_periodi_2, #xerr=sigma_res_p, 
        )#fmt='o')

    fit1 = ax.errorbar(x=(0.02, 0.179999), y=(A + B*0.02, A + B*0.18))
    #fit2 = ax.errorbar(x=(0, 1.4), y=(0, 1.4/k0_s))
    #ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

    ax.set_xlabel(u'Peso [N]', labelpad=12, fontsize=14)
    ax.set_ylabel(u'Allungamento [m]', labelpad=6, fontsize=14)
    ax.grid(True)
    
    plt.show()
