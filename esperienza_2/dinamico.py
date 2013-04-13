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

medie_periodi = [sum(ps)/len(ps) for ps in periodi]
medie_periodi_2 = [mp**2 for mp in medie_periodi]

sigma_periodi = [ for ps in periodi]

if mpl:
    f1 = plt.figure(figsize=(8, 6))
    f1.suptitle("Pesi e allungamenti", y=0.93, fontsize=15)

    A =  0.033628
    B =  4.0605

    ax = f1.add_subplot(1, 1, 1)
    dots = ax.errorbar(x=masse, y=[p - (A + B*m) for p, m in zip(medie_periodi_2, masse)],
        yerr=sigma_res_l, #xerr=sigma_res_p, 
        fmt='o')

    #fit1 = ax.errorbar(x=(0.02, 0.179999), y=(A + B*0.02, A + B*0.18))
    #fit2 = ax.errorbar(x=(0, 1.4), y=(0, 1.4/k0_s))
    #ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

    ax.set_xlabel(u'Peso [N]', labelpad=12, fontsize=14)
    ax.set_ylabel(u'Allungamento [m]', labelpad=6, fontsize=14)
    ax.grid(True)
    
    plt.show()
