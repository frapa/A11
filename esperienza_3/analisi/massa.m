# dati in input
dati = csvread("../dati/pendolo_masse_num.csv");

# in ordine BIANCO, ARGENTO, ORO GRANDE, ORO PICCOLO
masse = dati(1,:) ./ 1000;
periodi = dati(2:end,:) ./ 5;

# numero dati
N = length(periodi(:, 1))

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

# incertezze periodi
delta_ris_T = 0.01
sigma_ris_T = delta_ris_T / sqrt(12);

# medie dei periodi
T = mean(periodi)
sigma_T = sigma(periodi, T);
sigma_tot_T = sqrt(sigma_T.^2 + sigma_ris_T^2)

# pesi
w = sigma_tot_T.^-2;

media_T = sum(w .* T) / sum(w)
sigma_media_T = sum(w)^-0.5

#errorbar(masse, T, sigma_tot_T, "~")

chi2(T, masse, sigma_tot_T, media_T, 0)

[A, B, sigma_A, sigma_B] = fit(T, masse, w)