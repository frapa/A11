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
sigma_res_l = 0.001 / sqrt(6)
print sigma_res_p, sigma_res_l

f1 = plt.Figure()

plt.show()
