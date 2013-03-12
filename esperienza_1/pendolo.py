# -*- encoding: utf-8 -*-

from math import *
import csv
import itertools
import matplotlib.pyplot as plt
from matplotlib import rc

def mean(data):
    return sum(data) / len(data)

# leggi i dati
header = []
meas = {}
with open('pendolo/pendolo.csv') as csvfile:
    data = csv.reader(csvfile)

    for n, row in enumerate(data):
        if n == 0:
            for i, name in enumerate(row):
                header.append(name)
                meas[name] = []
        else:
            for i, value in enumerate(row):
                meas[header[i]].append(float(value) / 10.0)

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

t = plt.title('Periodo del pendolo', fontsize=16)
t.set_y(1.15)
plt.suptitle('60 misure effettuate da 3 diversi sperimentatori', x=0.52, y=0.91)
xlab = plt.xlabel('Periodo [s]', fontsize=14)
plt.ylabel(u'Probabilità', fontsize=14)
plt.grid(True)
plt.xticks(rotation=30)
plt.gca().set_yticklabels(("0", "0.2", "0.4", "0.6", "0.8", "0.1"))

plt.axis((1.480, 1.515, 0, 100))

plt.vlines(m, 0, 100, linestyles='dashed', linewidth=2, color=(0, 0, 1))
plt.vlines(m - sigma - 0.00003, 0, 100, linestyles='dashed', linewidth=1, color=(0.55, 0.55, 0.55), zorder=-4)
plt.vlines(m + sigma - 0.00003, 0, 100, linestyles='dashed', linewidth=1, color=(0.55, 0.55, 0.55), zorder=-4)
plt.axvspan(m - sigma, m + sigma, color=(0.7, 0.7, 0.7), alpha=0.5, zorder=-5)

plt.text(m - 0.0003, 102, "m")
plt.text(m - sigma - 0.0013, 102, u"m - σ")
plt.text(m + sigma - 0.0013, 102, u"m + σ")

# make sure nothing goes outside the screen
plt.tight_layout()

plt.show()
