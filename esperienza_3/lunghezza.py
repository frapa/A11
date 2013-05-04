import csv

lunghezze = []
lunghezze_raw = []
lunghezze_raw_cm = []
periodi = [[] for i in range(10)]
periodi_raw = [[] for i in range(10)]

with open("dati/pendolo_masse_num.csv") as f:
    reader = csv.reader(f)
    for n, row in enumerate(reader):
        if n == 0:
            # cosa totalmente a caso XXX
            # potrebbe non essere qui, anzi, forse sarebbe pure meglio
            lunghezze.append(1.057)
            lunghezze_raw.append("1.057")
            lunghezze_raw_cm.append("105.7")
        elif n < 11:
            periodi[0].append(float(row[2]) / 5) # becco ORO GRANDE
            periodi_raw[0].append(str(periodi[0][n - 1]))

with open("dati/lunghezza.csv") as f:
    reader = csv.reader(f)
    for n, row in enumerate(reader):
        if n == 0:
            for i, l in enumerate(row):
                lunghezze.append(float(l) / 100)
                lunghezze_raw.append(str(lunghezze[i + 1]))
                lunghezze_raw_cm.append(l)
        else:
            for i, p in enumerate(row):
                periodi[i + 1].append(float(p) / 5)
                periodi_raw[i + 1].append(str(periodi[i + 1][n - 1]))

# stampa tabella
for i, l in enumerate(lunghezze_raw):
    print l + " & " + " & ".join(periodi_raw[i]) + " \\\\"

    print " & ".join(lunghezze_raw_cm)
