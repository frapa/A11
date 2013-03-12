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

f1 = plt.figure()
f2 = plt.figure(figsize=(6, 8))

ax = f1.add_subplot(1, 1, 1)
n_metro, r_bins_metro, patches_metro = ax.hist(xs_metro, bins_metro,
    normed=True, color=(0, 0.65, 1), alpha=0.7)

prob = ax.twinx()
prob.set_ylabel(ur"Frequenza campionaria", fontsize=14)

ax.locator_params(axis='x', nbins=4)

ax.set_xlim(left=12, right=15)
t = ax.set_title("Metro a nastro", fontsize=15)
t.set_y(1.05)
ax.set_xlabel(u'Lunghezza [mm]', fontsize=14)
ax.set_ylabel(ur'Densità campionaria $[\frac{1}{mm}]$', fontsize=14)
ax.grid(True)

f1.suptitle('Lunghezza dei cilindretti', y=0.95, fontsize=16)
f1.subplots_adjust(left=0.12, right=0.88, top=0.8, bottom=0.15, wspace=0.35)

# istogramma
ax1 = f2.add_subplot(2, 1, 1)
ax2 = f2.add_subplot(2, 1, 2)

n_calibro, r_bins_calibro, patches_calibro = ax1.hist(xs_calibro, bins_cm,
    normed=True, color=(0, 0.65, 1), alpha=0.5)

ax1.set_xlim(left=13.65, right=14)
ax1.set_ylim(bottom=0, top=8)
t = ax1.set_title("Calibro", fontsize=15)
t.set_y(1.05)
ax1.set_xlabel(u'Lunghezza [mm]')
ax1.set_ylabel(ur'Densità campionaria')
ax1.grid(True)

n_micro, r_bins_micro, patches_micro = ax2.hist(xs_micro, bins_cm,
    normed=True, color=(0.4, 0.8, 0), alpha=0.5)

ax2.set_xlim(left=13.65, right=14)
ax2.set_ylim(bottom=0, top=8)
t = ax2.set_title("Micrometro", fontsize=15)
t.set_y(1.05)
ax2.set_xlabel(u'Lunghezza [mm]')
ax2.set_ylabel(u'Densità campionaria')
ax2.grid(True)

f2.suptitle('Lunghezza dei cilindretti', y=0.95, fontsize=16)
f2.subplots_adjust(left=0.11, right=0.89, top=0.86, bottom=0.1, hspace=0.4)

plt.show()
