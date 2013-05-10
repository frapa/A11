from matplotlib import pyplot as plt

masse = (0.088900, 0.162700, 0.496700, 0.202000)
T = (2.0532, 2.0533, 2.0603, 2.0553)
dT = (0.0056621, 0.0039637, 0.0043496, 0.0043487)

A = 2.0510
B =  0.018602

f1 = plt.figure(figsize=(8, 6))
f1.suptitle("Dipendenza del periodo dalla massa", y=0.93, fontsize=15)

ax = f1.add_subplot(1, 1, 1)
dots = ax.errorbar(x=masse, y=T,
    yerr=dT, #xerr=sigma_res_p, 
    fmt='o', capsize=7)

ax.set_xlabel(u'Massa [Kg]', labelpad=12, fontsize=14)
ax.set_ylabel(u'Periodo [s]', labelpad=12, fontsize=14)

fit1 = ax.errorbar(x=(0, 0.6), y=(2.0557, 2.0557))
fit2 = ax.errorbar(x=(0, 0.6), y=(A, A + 0.6*B))

ax.set_xlim((0, 0.6))
ax.set_xticks((0.1, 0.2, 0.3, 0.4, 0.5))
ax.set_ylim((2.04, 2.07))
ax.grid(True)

ax.legend((dots, fit1, fit2), ("Periodi con incertezza", "Media pesata", "Regressione lineare"), 'upper left',
        prop={'size': 12}, numpoints=1)

f1.subplots_adjust(left=0.13, right=0.93, top=0.85, bottom=0.13)

plt.show()
