import csv
from math import *
from matplotlib import pyplot as plt

g = 9.806

pesi = []
allungamenti = []
with open("dati/frapa_statico.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        pesi.append(round(float(row[0]) / 1000.0 * g, 5))
        allungamenti.append(round(abs(float(row[1]) - 50) / 100, 5))

print "Pesi:", pesi
print "Allungamenti:", allungamenti
print

sigma_res_p = 0.0001 / sqrt(12)
sigma_res_l = 0.0015 / sqrt(6)
print sigma_res_p, sigma_res_l

b = sum([p_i*x_i for p_i, x_i in zip(pesi, allungamenti)]) / \
    sum([p_i**2 for p_i in pesi])
sigma_b = sigma_res_l / sqrt(sum([p_i**2 for p_i in pesi]))
print b, sigma_b

chi = sum([(x_i - b*p_i)**2 / sigma_res_l**2
    for p_i, x_i in zip(pesi, allungamenti)])
print chi, len(pesi)

f1 = plt.figure()

ax = f1.add_subplot(1, 1, 1)
ax.errorbar(x=pesi, y=allungamenti,
    #xerr=sigma_res_p, yerr=sigma_res_l,
    fmt='o')

ax.errorbar(x=(0, 1.4), y=(0, b*1.4))
#ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
#ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

ax.set_xlabel(u'Peso [N]', fontsize=14)
ax.set_ylabel(u'Allungamento [m]', fontsize=14)
ax.grid(True)

plt.show()
