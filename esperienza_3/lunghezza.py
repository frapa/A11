#import csv
from matplotlib import pyplot as plt
from math import *

#lunghezze = []
#lunghezze_raw = []
#lunghezze_raw_cm = []
#periodi = [[] for i in range(10)]
#periodi_raw = [[] for i in range(10)]
#
#with open("dati/pendolo_masse_num.csv") as f:
#    reader = csv.reader(f)
#    for n, row in enumerate(reader):
#        if n == 0:
#            # cosa totalmente a caso XXX
#            # potrebbe non essere qui, anzi, forse sarebbe pure meglio
#            lunghezze.append(1.057)
#            lunghezze_raw.append("1.057")
#            lunghezze_raw_cm.append("105.7")
#        elif n < 11:
#            periodi[0].append(float(row[2]) / 5) # becco ORO GRANDE
#            periodi_raw[0].append(str(periodi[0][n - 1]))
#
#with open("dati/lunghezza.csv") as f:
#    reader = csv.reader(f)
#    for n, row in enumerate(reader):
#        if n == 0:
#            for i, l in enumerate(row):
#                lunghezze.append(float(l) / 100)
#                lunghezze_raw.append(str(lunghezze[i + 1]))
#                lunghezze_raw_cm.append(l)
#        else:
#            for i, p in enumerate(row):
#                periodi[i + 1].append(float(p) / 5)
#                periodi_raw[i + 1].append(str(periodi[i + 1][n - 1]))
#
## stampa tabella
#for i, l in enumerate(lunghezze_raw):
#    print l + " & " + " & ".join(periodi_raw[i]) + " \\\\"
#
#    print " & ".join(lunghezze_raw_cm)

L = (1.0525, 0.9485, 0.8485, 0.7485, 0.6485, 0.5485, 0.4485, 0.3485, 0.2485, 0.14855)
dL = 5.7740e-04
T = (2.06140, 1.94740, 1.85600, 1.73940, 1.60960, 1.47660, 1.33500, 1.18700, 1.00820, 0.77820)
dT = (0.0057643, 0.0038158, 0.0026625, 0.0033440, 0.0031770, 0.0052222, 0.0038873, 0.0040552, 0.0037618, 0.0039463)
dY = (1.2202e-03, 8.6113e-04, 6.4023e-04, 8.5150e-04, 8.7865e-04, 1.5528e-03, 1.2950e-03, 1.5265e-03, 1.6968e-03, 2.3579e-03)
dY_corr = (0.0023405, 0.0016517, 0.0012280, 0.0016332, 0.0016853, 0.0029784, 0.0024839, 0.0029280, 0.0032547, 0.0045227)
dis = (6.5753e-04, -1.4966e-03, 1.7765e-03, 7.8013e-04, -1.8155e-03, -2.9687e-03, -3.1218e-03, 5.2766e-04, 2.9247e-03, 2.0502e-03)

A = 0.30240
a = 2.0063
b = 0.49915

f1 = plt.figure(figsize=(8, 6))
f1.suptitle("Dipendenza del periodo dalla lunghezza", y=0.93, fontsize=15)

ax = f1.add_subplot(1, 1, 1)
dots = ax.errorbar(x=L, y=T,
    #yerr=dT, xerr=dL, 
    fmt='o', capsize=7)

ax.set_xlabel(u'Lunghezza del filo [m]', labelpad=12, fontsize=14)
ax.set_ylabel(u'Periodo [s]', labelpad=12, fontsize=14)
#ax.set_yscale('log')

fit1 = ax.errorbar(x=[l / 1000.0 for l in range(1201)], y=[a*(l/1000.0)**b for l in range(1201)])
#fit2 = ax.errorbar(x=(0, 0.6), y=(A, A + 0.6*B))

#ax.set_xlim((0, 0.6))
ax.set_xticks((0.2, 0.4, 0.6, 0.8, 1, 1.2))
ax.set_yticks((0.5, 1, 1.5, 2, 2.5))
#ax.set_ylim((2.04, 2.07))
ax.grid(True)

ax.text(-0.03, -0.1, "0")

ax.legend((dots, fit1), ("Dati sperimentali", "Dipendenza non lineare"), 'upper left',
        prop={'size': 12}, numpoints=1)

f1.subplots_adjust(left=0.13, right=0.93, top=0.85, bottom=0.13)


f2 = plt.figure(figsize=(8, 7))
f2.suptitle("Logaritmi di lunghezza e periodo", y=0.97, fontsize=15)

ax2 = f2.add_subplot(1, 1, 1)
dots = ax2.errorbar(x=[log10(l) for l in L], y=[log10(t) for t in T],
    #yerr=dY, #xerr=sigma_res_p, 
    fmt='o', capsize=7)

ax2y = ax2.twinx()
ax2x = ax2.twiny()

ax2.set_xlabel(u'$X \;=\; \log_{10}(\ell)$', labelpad=12, fontsize=14)
ax2.set_ylabel(u'$Y \;=\; \log_{10}(\,\mathcal{T}\,)$', labelpad=12, fontsize=14)
ax2x.set_xlabel(u'Lunghezza del filo [m]', labelpad=12, fontsize=14)
ax2y.set_ylabel(u'Periodo [s]', labelpad=12, fontsize=14)
#ax2.set_xlabel(ur'$X \;=\; log(\ell)$', labelpad=12, fontsize=14)
#ax2.set_ylabel(u'$Y \;=\; log(\mathcal{T})$', labelpad=12, fontsize=14)
#ax.set_yscale('log')

#fit1 = ax.errorbar(x=[l / 1000.0 for l in range(1201)], y=[a*(l/1000.0)**b for l in range(1201)])
fit2 = ax2.errorbar(x=(-0.9, 0.1), y=(A - 0.9 * b, A + 0.1 * b))

ax2.set_xlim((-0.9, 0.1))
ax2x.set_xlim((-0.9, 0.1))
ax2.set_ylim((-0.2, 0.4))
ax2y.set_ylim((-0.2, 0.4))

ax2x.set_xticks([log10(l/100.0) for l in range(15, 125, 10)])
ax2x.set_xticklabels(['0.15', '0.25', '0.35', '0.45', '0.55', '0.65', '0.75', '0.85', '0.95', '1.05', '1.15'], rotation=45)

ax2y.set_yticks([log10(l/100.0) for l in range(75, 250, 25)])
ax2y.set_yticklabels([str(l/100.0) for l in range(75, 250, 25)])

ax2.grid(True)

#ax2.text(-0.03, -0.1, "0")

ax2.legend((dots, fit2), ("Dati sperimentali", "Dipendenza lineare $Y = A + bX$"), 'upper left',
        prop={'size': 12}, numpoints=1)

f2.subplots_adjust(left=0.13, right=0.87, top=0.80, bottom=0.13)


f3 = plt.figure(figsize=(8, 7))
f3.suptitle("Discrepanza tra dati e regressione", y=0.97, fontsize=15)

ax3 = f3.add_subplot(1, 1, 1)
dots = ax3.errorbar(x=[log10(l) for l in L], y=[d * 1000 for d in dis],
    yerr=[dy * 1000 for dy in dY], #xerr=sigma_res_p, 
    fmt=None, capsize=7)
#dots = ax3.errorbar(x=[l for l in L], y=[t - a*l**b  for t, l in zip(T, L)],
#    yerr=dT, #xerr=sigma_res_p, 
#    fmt='o', capsize=7)

dots2 = ax3.errorbar(x=[log10(l) for l in L], y=[d * 1000 for d in dis],
    yerr=[dy * 1000 for dy in dY_corr], #xerr=sigma_res_p, 
    fmt='o', capsize=7)

ax3.set_xlabel(u'$X \;=\; \log_{10}(\ell)$', labelpad=12, fontsize=14)
ax3.set_ylabel(ur'Discrepanza ( $\times \, 10^{-3}$)', labelpad=12, fontsize=14)
#ax.set_yscale('log')

fit3 = ax3.errorbar(x=[-0.9, 0.1], y=(0, 0))
#fit2 = ax.errorbar(x=(0, 0.6), y=(A, A + 0.6*B))

ax3.set_xlim((-0.9, 0.1))
#ax3.set_xticks((0.2, 0.4, 0.6, 0.8, 1, 1.2))
#ax3.set_yticks((0.5, 1, 1.5, 2, 2.5))
ax3.set_ylim((-8, 8))
ax3.grid(True)

ax3y = ax3.twinx()
ax3x = ax3.twiny()
#ax3x.grid(True)

ax3x.set_xlabel(u'Lunghezza del filo [m]', labelpad=12, fontsize=14)
ax3y.set_ylabel(u'Discrepanza [s]', labelpad=12, fontsize=14)

ax3x.set_xlim((-0.9, 0.1))
ax3y.set_ylim((-0.02, 0.02))

ax3x.set_xticks([log10(l/100.0) for l in range(15, 125, 10)])
ax3x.set_xticklabels(['0.15', '0.25', '0.35', '0.45', '0.55', '0.65', '0.75', '0.85', '0.95', '1.05', '1.15'], rotation=45)

#ax3y.set_yticks([log10(t/100.0) * 1000.0 for t in range(98, 102, 1)])

#ax3.text(-0.03, -0.1, "0")

ax3.legend((dots, dots2, fit3), ("Dati con incertezze", "Incertezze corrette", "Retta di fit"), 'lower left',
        prop={'size': 12}, numpoints=1)

f3.subplots_adjust(left=0.13, right=0.87, top=0.80, bottom=0.13)

plt.show()
