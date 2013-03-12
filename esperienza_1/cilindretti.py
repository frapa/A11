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
with open('cilindretti/misure_cilindretti.csv') as csvfile:
    data = csv.reader(csvfile)

    for n, row in enumerate(data):
        if n == 0:
            for i, name in enumerate(row):
                header.append(name.strip())
                meas[name.strip()] = []
        else:
            for i, value in enumerate(row):
                meas[header[i]].append(float(value))

# compute some stuff
# Metro
xs_metro = meas["METRO"]
N_metro = len(xs_metro)
m_metro = mean(xs_metro)
D_metro = sum([(x - m_metro)**2 for x in xs_metro]) / (N_metro - 1)
sigma_metro = sqrt(D_metro)

print "METRO:\nN = {}\nm = {}\nD = {}\nσ = {}\n\n".format(N_metro, m_metro, D_metro, sigma_metro)

# calibro
xs_calibro = meas["CALIBRO"]
N_calibro = len(xs_calibro)
m_calibro = mean(xs_calibro)
D_calibro = sum([(x - m_calibro)**2 for x in xs_calibro]) / (N_calibro - 1)
sigma_calibro = sqrt(D_calibro)

print "CALIBRO:\nN = {}\nm = {}\nD = {}\nσ = {}\n\n".format(N_calibro, m_calibro, D_calibro, sigma_calibro)

# micrometro
xs_micro = meas["MICROMETRO"]
N_micro = len(xs_micro)
m_micro = mean(xs_micro)
D_micro = sum([(x - m_micro)**2 for x in xs_micro]) / (N_micro - 1)
sigma_micro = sqrt(D_micro)

print "MICROMETRO:\nN = {}\nm = {}\nD = {}\nσ = {}".format(N_micro, m_micro, D_micro, sigma_micro)

# bins metro
delta_metro = 1
x_min_metro = 12.5
x_max_metro = 14.5
bins_metro = [x_min_metro + i * delta_metro for i in range(int((x_max_metro - x_min_metro) / delta_metro) + 1)]

# bins (calibro micrometro -> cm)
delta_cm = 0.05
x_min_cm = 13.675
x_max_cm = 13.975
bins_cm = [x_min_cm + i * delta_cm for i in range(int(round((x_max_cm - x_min_cm) / delta_cm)) + 1)]

# istogramma
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

plt.subplot(1, 2, 1)
n_metro, r_bins_metro, patches_metro = plt.hist(xs_metro, bins_metro,
    normed=True, color=(0, 0.65, 1), alpha=0.7)

plt.locator_params(axis='x', nbins=4)

ax1.set_xlim(left=12, right=15)
t = plt.title("Metro a nastro", fontsize=15)
t.set_y(1.05)
plt.xlabel(u'Lunghezza [mm]')
plt.ylabel(u'Probabilità')
ax1.set_yticklabels(("0", "0.2", "0.4", "0.6", "0.8", "1"))
plt.grid(True)

plt.subplot(1, 2, 2)
n_calibro, r_bins_calibro, patches_calibro = plt.hist(xs_calibro, bins_cm,
    normed=True, color=(0, 0.65, 1), alpha=0.5)

plt.locator_params(axis='x', nbins=5)

n_micro, r_bins_micro, patches_micro = plt.hist(xs_micro, bins_cm,
    normed=True, color=(0.4, 0.8, 0), alpha=0.5)

ax2.set_xlim(left=13.6, right=14.05)
t = plt.title("Calibro e micrometro", fontsize=15)
t.set_y(1.05)
plt.xlabel(u'Lunghezza [mm]')
plt.xticks(rotation=30)
ax2.set_yticklabels(("0", "0.2", "0.4", "0.6", "0.8", "1"))
plt.ylabel(u'Probabilità')
plt.grid(True)

# personalize ticks
ax2.set_xticklabels(("13.7"))
ax2.set_xticks([13.7, 13.8])

plt.suptitle('Lunghezza dei cilindretti', y=0.95, fontsize=16)
plt.subplots_adjust(left=0.11, right=0.89, top=0.8, bottom=0.15, wspace=0.35)

plt.show()
