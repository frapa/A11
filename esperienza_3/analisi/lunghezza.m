# dati in input
dati = csvread("../dati/lunghezza.csv");
dati_masse = csvread("../dati/pendolo_masse_num.csv");

# in ordine BIANCO, ARGENTO, ORO GRANDE, ORO PICCOLO
# dati(1,:) ./ 1000;
# prendiamo 10 dati dalla colonna ORO GRANDE
periodi_105 = dati_masse(2:11,3) ./ 5;

# altri dati importanti
# lunghezza filo
Lf_g = 1.057; # grandi
Lf_p = 1.071; # piccolo
# morsetto
L_mors = 0.028;
# errori risoluzione
delta_ris_L = 0.001;
sigma_ris_L = delta_ris_L / sqrt(12);

# altezza cilindri grandi
h_g = 0.0471;
# cilindro piccolo
h_p = 0.01905;
# errore risoluzione (calibro)
delta_ris_h = 0.00005;
sigma_ris_h = delta_ris_h / sqrt(12);

L_g = Lf_g - L_mors + h_g / 2;
L_p = Lf_p - L_mors + h_p / 2;
# dato che sono uguali
L = L_g
# incertezza totale
sigma_L = sqrt(4 * sigma_ris_L^2 + sigma_ris_h^2)

# estraiamo i dati e li integriamo con quelli delle masse
lunghezze = [Lf_g, dati(1,:) ./ 100];
periodi = [periodi_105, dati(2:end,:) ./ 5];

# numero dati
N = length(periodi(:, 1))

# Mettiamo a posto le lunghezze
Ls = lunghezze - L_mors + h_g / 2;

# incertezze periodi
delta_ris_T = 0.002;
sigma_ris_T = delta_ris_T / sqrt(12);

# medie dei periodi
T = mean(periodi);
sigma_T = sigma(periodi, T);
sigma_tot_T = sqrt(sigma_T.^2 + sigma_ris_T^2);

# Bon, facciamo il fit
# calcoliamo i logaritmi
X = log(Ls);
delta_X = (Ls).^(-1) * sigma_L;
Y = log(T);
delta_Y = (T).^(-1) .* sigma_tot_T;

#errorbar(X, Y, delta_X, delta_Y, '~>')
# trasferimento incertezza
stima_b = 0.5
delta_Y_tot = sqrt(delta_Y .^ 2 + (stima_b .* delta_X) .^ 2);
w = delta_Y_tot .^ -2;

# regressione lineare (anche se ce stanno logaritmi)
[A, b, sigma_A, sigma_b] = fit(Y, X, w)

# chi quadro per vedere se siamo inchiappettati
chi_2 = chi2(Y, X, delta_Y_tot, A, b)
# ok, siamo inchiappettati
# rifacciamo i conti sulle incertezze
p = chi_2 / 8
w_corr = w ./ p;

[A, b, sigma_A, sigma_b] = fit(Y, X, w_corr)

# chi quadro per vedere se tutto torna
chi_2_corr = chi2(Y, X, delta_Y_tot .* sqrt(p), A, b)

# ricavo a (fattore)
a = exp(A)
sigma_a = exp(A) * sigma_A