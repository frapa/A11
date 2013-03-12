# -*- encoding: utf-8 -*-

from math import *
import csv
import itertools
import matplotlib.pyplot as plt
from matplotlib import rc

def mean(data):
    return sum(data) / len(data)

tex = r""

# leggi i dati
header = []
meas = {}
with open('pendolo/pendolo.csv') as csvfile:
    data = csv.reader(csvfile)
    tab = [[], [], []]

    l = 0
    for n, row in enumerate(data):
        l += 1

        if n == 0:
            for i, name in enumerate(row):
                header.append(name)
                meas[name] = []
        else:
            for i, value in enumerate(row):
                meas[header[i]].append(float(value) / 10.0)
                tab[i].append(value.strip() + " s")

    tex += "\\begin{{tabular}} {{l || {}}}\n\t\\hline \\hline\n".format(" | ".join(["c" for i in range(l)]))

    for i in range(3):
        tex += "\t" + header[i] + " & " + " & ".join(tab[i][:10]) + " \\\\ \cline{2-11} \n"
        tex += "\t & " + " & ".join(tab[i][10:20]) + " \\\\ \hline \n"

tex += '\t\\hline\n\\end{tabular}'
print tex

xs = tuple(itertools.chain(*meas.values()))
N = len(xs)
m = mean(xs)
D = sum([(x - m)**2 for x in xs]) / (N - 1)
sigma = sqrt(D)

print "N = {}\nm = {}\nD = {}\nσ = {}".format(N, m, D, sigma)

# bins 
delta = 0.003
x_min = 1.4835
x_max = 1.5135
bins = [x_min + i * delta for i in range(int((x_max - x_min) / delta) + 1)]

# istogramma
n, r_bins, patches = plt.hist(xs, bins, (x_min, x_max),
    normed=True, color=(0, 0.65, 1), alpha=0.7)

plt.gca().set_ylim((0, 100))
t = plt.title('Periodo del pendolo', fontsize=16)
t.set_y(1.15)
plt.suptitle('60 misure effettuate da 3 diversi sperimentatori', x=0.50, y=0.89)
xlab = plt.xlabel('Periodo [s]', fontsize=14)
plt.ylabel(u'Densità campionaria $[\\frac{1}{s}]$', fontsize=14)
plt.grid(True)
plt.xticks(rotation=30)

plt.vlines(m, 0, 100, linestyles='dashed', linewidth=2, color=(0, 0, 1))
plt.vlines(m - sigma - 0.00003, 0, 100, linestyles='dashed', linewidth=1, color=(0.55, 0.55, 0.55), zorder=-4)
plt.vlines(m + sigma - 0.00003, 0, 100, linestyles='dashed', linewidth=1, color=(0.55, 0.55, 0.55), zorder=-4)
plt.axvspan(m - sigma, m + sigma, color=(0.7, 0.7, 0.7), alpha=0.5, zorder=-5)

prob = plt.twinx()
prob.set_ylim((0, 100))
prob.set_ylabel(u"Frequenza campionaria", fontsize=14)
prob.set_yticklabels(["0", "0.06", "0.12", "0.18", "0.24", "0.30"])

plt.text(m - 0.0003, 102, "m")
plt.text(m - sigma - 0.0013, 102, u"m - σ")
plt.text(m + sigma - 0.0013, 102, u"m + σ")

# make sure nothing goes outside the screen
plt.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.15)

plt.show()
