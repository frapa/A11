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
                header.append(name.strip())
                meas[name.strip()] = []
        else:
            for i, value in enumerate(row):
                meas[header[i]].append(float(value) / 10.0)
                tab[i].append(value.strip())

    tex += "\\begin{{table}}\n\t\\begin{{tabular}} {{{}}}\n\t\t\\toprule\n".format(" | ".join(["c c c c"] * 3))
    tex += "\t\t\\multicolumn{12}{c}{Periodo del pendolo [s]} \\\\\n"
    tex += "\t\t" + " & ".join(map(lambda x: "\\multicolumn{4}{c}{" + x + "}", meas.keys())) + " \\\\\n\t\t\midrule\n"

    for i in range(5):
        t = []
        for h in range(3):
            t.append(" & ".join([x for n, x in enumerate(tab[h]) if ((n - i) % 5) == 0]))

        tex += "\t\t" + " & ".join(t) + " \\\\\n"

tex += '\t\t\\bottomrule\n\t\\end{tabular}\n\\end{table}'

print tex
print

xs_single = tuple(itertools.chain(*meas.values()))
N = len(xs_single)
m = mean(xs_single)
D = sum([(x - m)**2 for x in xs_single]) / (N - 1)
sigma = sqrt(D)

xs = meas.values()
xs1, xs2, xs3 = xs
N1, N2, N3 = map(len, xs)
m1, m2, m3 = map(mean, xs)
D1, D2, D3 = map(lambda xxs: sum([(x - mean(xxs))**2 for x in xxs]) / (len(xxs) - 1), xs)
sigma1, sigma2, sigma3 = map(sqrt, (D1, D2, D3))

#print "N = {}\nm = {}\nD = {}\nσ = {}".format(N, m, D, sigma)

# bins 
delta = 0.003
x_min = 1.4835
x_max = 1.5135
bins = [x_min + i * delta for i in range(int((x_max - x_min) / delta) + 1)]

if mpl:
    # istogramma
    f1 = plt.figure(figsize=(9, 6))

    n, r_bins, patches = plt.hist(xs, bins, (x_min, x_max), rwidth=0.9,
        normed=True, color=((0, 0.65, 1), (0.4, 0.8, 0), (.95, 0.5, 0.1)), alpha=0.7)
    n0, r_bins0, patches0 = plt.hist(xs_single, bins, (x_min, x_max), rwidth=0.9,
        normed=True, color=(0.85, 0.85, 0.85), alpha=0.7, zorder=-5, edgecolor=(0.6, 0.6, 0.6),
        linestyle="dashed")

    plt.gca().set_ylim((0, 160))
    t = plt.title('Periodo del pendolo', fontsize=16)
    t.set_y(1.15)
    plt.suptitle('Differenza tra i 3 operatori', x=0.50, y=0.89)
    xlab = plt.xlabel('Periodo [s]', fontsize=14)
    plt.ylabel(u'Densità campionaria $[\\frac{1}{s}]$', fontsize=14)
    plt.grid(True)
#    plt.xticks(rotation=30)

    plt.vlines(m, 0, 160, linestyles='dashed', linewidth=1, color=(0, 0, 0))
    plt.vlines(m - sigma - 0.00003, 0, 160, linestyles='dashed', linewidth=1, color=(0.8, 0.8, 0.2), zorder=-14)
    plt.vlines(m + sigma - 0.00003, 0, 160, linestyles='dashed', linewidth=1, color=(0.8, 0.8, 0.2), zorder=-14)
    plt.axvspan(m - sigma, m + sigma, color=(0.9, 0.9, 0.3), alpha=0.2, zorder=-15)

    plt.text(m - 0.0003, 162, "m")
    plt.text(m - sigma - 0.0013, 162, u"m - σ")
    plt.text(m + sigma - 0.0013, 162, u"m + σ")

    prob = plt.twinx()
    prob.set_ylim((0, 0.48))
    prob.set_ylabel(u"Frequenza campionaria", fontsize=14)
    prob.set_yticks((0, 0.06, 0.12, 0.18, 0.24, 0.30, 0.36, 0.42, 0.48))

    plt.gca().set_xticks([1.485, 1.490, 1.495, 1.5, 1.505, 1.510])
    plt.gca().set_xlim((1.480, 1.515))

    plt.legend(patches, ["Francesco", "Davide", "Andrea"], loc=2)

    # make sure nothing goes outside the screen
    plt.subplots_adjust(left=0.12, right=0.88, top=0.8, bottom=0.15)

    plt.show()
