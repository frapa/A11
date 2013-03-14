# -*- encoding: utf-8 -*-

from math import *
import csv
import itertools

mpl = False
try:
    import matplotlib.pyplot as plt
    from matplotlib import rc
    mpl = True
except:
    pass

def mean(data):
    return sum(data) / len(data)

tex = "\\begin{table}\n\t\\begin{tabular} {" + " | ".join(["c c c c c"] * 2) + "}\n\t\t\\toprule\n"
tex += "\t\t\multicolumn{10}{c}{Periodo del pendolo - Misure di un operatore [s]} \\\\\n\t\t\\midrule\n"

# leggi i dati
header = []
meas = []
meas_txt = []
with open('pendolo/n100.csv') as csvfile:
    data = csv.reader(csvfile)

    for row in data:
        meas.append(float(row[0]))
        meas_txt.append(row[0])

    l = 0
    for i in range(10):
        if l == 5:
            tex += "\t\t\\midrule\n"

        tex += "\t\t" + " & ".join([x for n, x in enumerate(meas_txt) if ((n - i) % 10) == 0]) + " \\\\\n"

        l += 1

tex += "\t\\bottomrule\n\t\\end{tabular}\n\\end{table}"

print tex
print

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

if mpl:
    # istogramma
    n, r_bins, patches = plt.hist(xs, bins, (x_min, x_max),
        normed=True, color=(0, 0.65, 1), alpha=0.7, zorder=2)

    t = plt.title('Periodo del pendolo', fontsize=16)
    t.set_y(1.14) 
    plt.suptitle('100 misure di un singolo sperimentatore', x=0.50, y=0.90)
    plt.xlabel('Periodo [s]', fontsize=14)
    plt.ylabel(ur'Densità campionaria $[\frac{1}{s}]$', fontsize=14)
    plt.gca().set_ylim((0, 11))
    plt.grid(True)

    plt.vlines(m, 0, 100, linestyles='dashed', linewidth=2, color=(0, 0, 1), zorder=5)
    plt.axvspan(m - sigma, m + sigma, color=(0.7, 0.7, 0.7), alpha=0.5, zorder=-5)

    plt.text(m - 0.003, 11.2, "m")
    plt.vlines(m - sigma - 0.00025, 0, 100, linestyles='dashed', linewidth=1, color=(0.55, 0.55, 0.55), zorder=-4)
    plt.vlines(m + sigma - 0.00025, 0, 100, linestyles='dashed', linewidth=1, color=(0.55, 0.55, 0.55), zorder=-4)
    plt.text(m - sigma - 0.012, 11.2, u"m - σ")
    plt.text(m + sigma - 0.014, 11.2, u"m + σ")

    prob = plt.twinx()
    prob.set_ylim((0, 0.33))
    prob.set_ylabel(u"Frequenza campionaria", fontsize=14)
    prob.set_yticks((0, 0.06, 0.12, 0.18, 0.24, 0.3))

    plt.gca().set_xlim((1.33, 1.65))

    # make sure nothing goes outside the screen
    plt.subplots_adjust(left=0.11, right=0.89, top=0.81, bottom=0.13)

    plt.show()
