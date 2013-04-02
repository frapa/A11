# -*- encoding: utf-8 -*-

import csv
import sys
from math import *

mpl = False
try:
    from matplotlib import pyplot as plt
    mpl = True
except:
    pass


# LETTURA DATI E CALCOLO PARAMETRI
g = 9.806

masse = []
pesi = []
allungamenti_raw = []
allungamenti = []
with open("dati/frapa_statico.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        masse.append(row[0])
        allungamenti_raw.append(str(abs(float(row[1]) - 50)))

        pesi.append(round(float(row[0]) / 1000.0 * g, 5))
        allungamenti.append(round(abs(float(row[1]) - 50) / 100, 5))


# incertezze
res_p = 0.0001
res_l = 0.001
sigma_res_p = res_p / sqrt(12)
sigma_res_l = res_l / sqrt(6)

# metodo della tabella
ks = [p_i/x_i for p_i, x_i in zip(pesi, allungamenti)]
sigma_ks = [sqrt(sigma_res_p**2 / p_i**2 + sigma_res_l**2 / x_i**2) * k_i
    for p_i, x_i, k_i in zip(pesi, allungamenti, ks)]
sigma_ks_without = [sqrt(sigma_res_l**2 / x_i**2) * k_i
    for x_i, k_i in zip(allungamenti, ks)]

# media pesata
ws = [1 / dk_i**2 for dk_i in sigma_ks]
k0_w = sum([k_i*w_i for k_i, w_i in zip(ks, ws)]) / sum(ws)
dk_w = 1 / sqrt(sum(ws))

# parametri statistici
k0_s = sum(ks) / len(ks)
# scarto quadratico standard
dk_s = sqrt(sum([(k_i - k0_s)**2 for k_i in ks]) / (len(ks) - 1))

# chi quadro
b = sum([p_i*x_i for p_i, x_i in zip(pesi, allungamenti)]) / \
    sum([p_i**2 for p_i in pesi])
sigma_b = sigma_res_l / sqrt(sum([p_i**2 for p_i in pesi]))

k0_chi = 1 / b
dk_chi = sigma_b / b**2

chi = sum([(x_i - b*p_i)**2 / sigma_res_l**2
    for p_i, x_i in zip(pesi, allungamenti)])

# aggiustiamo le incertezze per far tornare il chi^2
sigma_l_new = sqrt(sum([(x_i - b*p_i)**2 for p_i, x_i in zip(pesi, allungamenti)]) / (len(pesi) - 1))
sigma_b_new = sigma_l_new / sqrt(sum([p_i**2 for p_i in pesi]))

dk_chi_new = sigma_b_new / b**2


# INTERFACCIA
cmd = None
try:
    cmd = sys.argv[1]
except:
    cmd = ""

if cmd == "":
    print """Questo script genera i dati sull'esperimento di misura
della costante k della molla con il metodo statico."""

    print "\nÈ stato usato il valore g = {} m/s^2\n".format(g)

    print "METODO DELLA TABELLA"
    print "=" * 80, "\n"
    
    print "Ecco i dati usati. Il numero di dati è {}\n".format(len(pesi))

    print "\tN\tPesi [N]\tAllungamenti [m]\tk [N/m]\t\tδk [N/m]\tδk (no incertezza peso) [N/m]\n"
    # stampa la tabella in solo 2 righe! (lo so è incomprensibile)
    print "\t" + "\n\t".join(["{}\t{:.4}\t\t{}\t\t\t{:.3}\t\t{:.3}\t\t{:.3}".format(i+1, p_i, x_i, k_i, dk_i, dk_i_w)
        for i, (p_i, x_i, k_i, dk_i, dk_i_w) in enumerate(zip(pesi, allungamenti, ks, sigma_ks, sigma_ks_without))])
    print

    print """Nella tabella sopra sono riportati i valori k_i = p_i/x_i. Useremo questi valori
calcolare con il 'metodo della tabella' (paragrafo 4.4.5) la costante k della molla.
L'incertezza sui k_i non sono tutte uguali e sono riportate nella penultima colonna della tabella.
Nell'ultima colonna è stato riportato il valore dell'incertezza stimata senza tener
conto dell'incertezza sul peso (4.4.5 formula (3)). Come si vede il contributo dell'incertezza
sul peso sull'incertezza totale è trascurabile.
È stato usato il metodo descritto sulla scheda dell'esperienza.\n"""

    print "Sono state usate le seguenti incertezze:"
    print "\trisoluzione peso σ_res_p = {} N -> incertezza tipo sul peso σ(p) = {:.3} N".format(res_p, sigma_res_p)
    print "\trisoluzione lunghezza σ_res_x = {} m -> incertezza tipo sulla lunghezza σ(x) = {:.3} m".format(res_l, sigma_res_l)
    print "\t(si è tenuto conto dell'incertezza sul posizionamento a 50 cm dello zero)\n"

    print "Calcolo del k con metodo della tabella.\n   (a)  Media pesata:"
    print "\tk = {:.3} ∓ {:.3} N/m\n".format(k0_w, dk_w)

    print "   (b)  Parametri statistici:\n\tk = {:.3} ∓ {:.3} N/m\n".format(
        k0_s, dk_s)

    print "METODO DEL χ^2"
    print "=" * 80, "\n"

    print """Per il calcolo della pendenza è stata seguita la procedira del paragrafo 4.4.6.
Sono state ignorate le incertezze sul peso.\n"""

    print "Pendenza della retta di fit (b = 1/k della molla):\n\tb = {:.3} ∓ {:.3} m/N".format(b, sigma_b)
    print "\tCorrisponde a k = {:.3} ∓ {:.3} N/m".format(k0_chi, dk_chi)
    print """\t(Notare che il k ottenuto qui è uguale a quello ottenuto nel punto (a) precedente
\tcon la media pesata. Questo perché le due procedure sono equivalenti.)\n"""

    print """Il valore χ^2 = {:.3} è troppo alto. Dovrebbe essere χ^2 ≃ 12, ovvero numero_dati - 1
(1 è stato usato per calcolare b). Proviamo ad aggiustare le incertezze per far tornare il χ^2.\n""".format(chi)
    
    print "Il nuovo valore dell'incertezza sulla lunghezza è:"
    print "\tσ_m(x) = {:.3} m".format(sigma_l_new)
    print "\tCorrisponde a un incertezza massima di risoluzione (teorica, eh!) di {:.3} m\n".format(sigma_l_new * sqrt(6))
    
    print """Questo nuovo valore dell'incertezza è probabile poiché nell'incertezza precedente non si era
tenuto conto degli errori casuali e sistematici, ma solo dell'errore di risoluzione.
1.5 mm è un incertezza accettabile anche perché la molla non sta mai ferma.\n"""

    print "Il nuovi valori di b e di k tenuto conto della correzione sono:"
    print "\tb = {:.3} ∓ {:.3} m/N".format(b, sigma_b_new)
    print "\tk = {:.3} ∓ {:.3} N/m".format(k0_chi, dk_chi_new)
    print "\t(Sono cambiate solo le incertezze ovviamente)"

elif cmd in ("-h", "--help"):
    print "Se si esegue lo script senza argomenti, verrà stampata una descrizione con i calcoli effettuati.\n"
    print "Argomenti possibili:"
    print "\t-h\tMostra questo aiuto"
    print "\t-g\tDisegna il grafico"
    print "\t-t\tStampa la tabella per latex"

elif cmd == "-g":
    if not mpl:
        print "Non è installata la libraria per il disegno dei grafici. Si installa con:"
        print "\tsudo apt-get install python-matplotlib"
        sys.exit(1)

    f1 = plt.figure()

    ax = f1.add_subplot(1, 1, 1)
    ax.errorbar(x=pesi, y=allungamenti,
        #xerr=sigma_res_p, yerr=sigma_res_l,
        fmt='o')

    ax.errorbar(x=(0, 1.4), y=(0, b*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

    ax.set_xlabel(u'Peso [N]', fontsize=14)
    ax.set_ylabel(u'Allungamento [m]', fontsize=14)
    ax.grid(True)

    plt.show()
elif cmd == "-t":
    print "\\begin{table}\n\t\\centering"
    print "\t\\begin{{tabular}}{{l | {} }}\n\t\t\\toprule".format(" ".join("c" * len(pesi)))

    print "\t\tMasse [g] &", " & ".join(masse), "\\\\" 
    print "\t\tAllungamenti [cm] &", " & ".join(allungamenti_raw), "\\\\" 

    print "\t\t\\bottomrule\n\t\\end{tabular}"
    print "\\end{table}"
