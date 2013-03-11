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
meas = []
with open('pendolo/n100.csv') as csvfile:
    data = csv.reader(csvfile)

    for row in data:
        meas.append(float(row[0]))

# compute some stuff
xs = meas
N = len(xs)
m = mean(xs)
D = sum([(x - m)**2 for x in xs]) / (N - 1)
sigma = sqrt(D)

print "N = {}\nm = {}\nD = {}\nσ = {}".format(N, m, D, sigma)

# bins 
delta = 0.03
x_min = 1.355
x_max = 1.625
bins = [x_min + i * delta for i in range(int((x_max - x_min) / delta) + 1)]

# istogramma
n, r_bins, patches = plt.hist(xs, bins, (x_min, x_max),
    normed=True, color=(0, 0.65, 1), alpha=0.7)

t = plt.title('Periodo del pendolo', fontsize=16)
t.set_y(1.15) 
plt.suptitle('100 measures by a single operator', x=0.52, y=0.91)
plt.xlabel('Periodo [s]', fontsize=14)
plt.ylabel(u'Probabilità', fontsize=14)
plt.grid(True)
plt.xticks(rotation=30)
plt.gca().set_yticklabels(("0", "0.02", "0.04", "0.06", "0.08", "0.1", "0.12", "0.14"))

plt.axis((1.35, 1.65, 0, 15))

plt.vlines(m, 0, 100, linestyles='dashed', linewidth=2, color=(0, 0, 1))
plt.axvspan(m - sigma, m + sigma, color=(0.7, 0.7, 0.7), alpha=0.5, zorder=-5)

plt.text(m - 0.003, 15.4, "m")
plt.text(m - sigma - 0.01, 15.4, u"m - σ")
plt.text(m + sigma - 0.01, 15.4, u"m + σ")

# make sure nothing goes outside the screen
plt.tight_layout()

plt.show()
