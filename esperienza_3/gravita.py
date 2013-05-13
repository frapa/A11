from matplotlib import pyplot as plt

L = (1.0525, 0.9485, 0.8485, 0.7485, 0.6485, 0.5485, 0.4485, 0.3485, 0.2485, 0.14855)
g = (9.7786, 9.8744, 9.7248, 9.7675, 9.8825, 9.9323, 9.9359, 9.7661, 9.6534, 9.6839)
dg = (0.054950, 0.039160, 0.028675, 0.038304, 0.039992, 0.071028, 0.059261, 0.068663, 0.075449, 0.105184)

g1 = 9.8
g3 = 9.81

f1 = plt.figure(figsize=(8, 6))
f1.suptitle("Dipendenza del periodo dalla lunghezza", y=0.93, fontsize=15)

ax = f1.add_subplot(1, 1, 1)
dots = ax.errorbar(x=L, y=g,
    yerr=dg, #xerr=sigma_res_p, 
    fmt='o', capsize=7)

ax.set_xlabel(u'Lunghezza del filo [m]', labelpad=12, fontsize=14)
ax.set_ylabel(u'Periodo [s]', labelpad=12, fontsize=14)

fit1 = ax.errorbar(x=(0, 1.2), y=(g1, g1))
fit2 = ax.errorbar(x=(0, 1.2), y=(g3, g3))

#ax.set_xlim((0, 0.6))
#ax.set_xticks((0.1, 0.2, 0.3, 0.4, 0.5))
#ax.set_ylim((2.04, 2.07))
ax.grid(True)

#ax.legend((dots, fit1), ("Periodi con incertezza", "Dipendenza non lineare"), 'upper left',
#        prop={'size': 12}, numpoints=1)

f1.subplots_adjust(left=0.13, right=0.93, top=0.85, bottom=0.13)

plt.show()
