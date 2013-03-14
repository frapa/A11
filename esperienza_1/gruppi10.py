# -*- encoding: utf-8 -*-

from math import *
import csv
import itertools

def mean(data):
    return sum(data) / len(data)

# leggi i dati
header = []
meas = []
groups = [[], [], [], [], [], [], [], [], [], []]
with open('pendolo/n100.csv') as csvfile:
    data = csv.reader(csvfile)

    for n, row in enumerate(data):
        meas.append(float(row[0]))
        groups[n // 10].append(float(row[0]))

means = []
for group in groups:
    # compute some stuff
    Nk = len(group)
    mk = mean(group)
    means.append(mk)

    print "Nk = {}\nmk = {}\n".format(Nk, mk)

m_x = mean(meas)
m_mk = mean(means)
print "m_x = {}\nm_mk = {}".format(m_x, m_mk)

sigma_x = sqrt(sum([(x - m_x)**2 for x in meas]) / (len(meas) - 1))
sigma_mk = sqrt(sum([(x - m_mk)**2 for x in means]) / (len(means) - 1))
print "σ_x = {}\nσ_mk = {}\n1/sqrt(N)*σ_x = {}".format(sigma_x, sigma_mk, 1/sqrt(10)*sigma_x)
