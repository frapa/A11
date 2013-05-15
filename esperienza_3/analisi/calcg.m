#  dati in input
dati = csvread("../dati/lunghezza.csv");
dati_masse = csvread("../dati/pendolo_masse_num.csv");

#  in ordine BIANCO, ARGENTO, ORO GRANDE, ORO PICCOLO
#  dati(1,:) ./ 1000;
#  prendiamo 10 dati dalla colonna ORO GRANDE
periodi_105 = dati_masse(2:11,3) ./ 5;

#  altri dati importanti
#  lunghezza filo
Lf_g = 1.057; # grandi
#  morsetto
L_mors = 0.028;
#  errori risoluzione
delta_ris_L = 0.001;
sigma_ris_L = delta_ris_L / sqrt(12);

#  altezza cilindri grandi
h_g = 0.0471;
#  errore risoluzione (calibro)
delta_ris_h = 0.00005;
sigma_ris_h = delta_ris_h / sqrt(12);

L_g = Lf_g - L_mors + h_g / 2;
#  dato che sono uguali
L = L_g;
#  incertezza totale
sigma_L = sqrt(4 * sigma_ris_L^2 + (sigma_ris_h/2)^2);  % <<---

#  estraiamo i dati e li integriamo con quelli delle masse
lunghezze = [Lf_g, dati(1,:) ./ 100];
periodi = [periodi_105, dati(2:end,:) ./ 5];

#  numero dati
N = length(periodi(:, 1));

#  Mettiamo a posto le lunghezze
Ls = lunghezze - L_mors + h_g / 2;    % <<---

#  incertezze periodi
delta_ris_T = 0.002;
sigma_ris_T = delta_ris_T / sqrt(12);

#  medie dei periodi
T = mean(periodi);      % <<---
sigma_T = sigma(periodi, T);
sigma_tot_T = sqrt(sigma_T.^2 + sigma_ris_T^2);  % <<---

# Bon, facciamo il fit
# calcoliamo i logaritmi
X = log10(Ls);
delta_X = log10(e) .* (Ls).^(-1) * sigma_L;
Y = log10(T);
delta_Y = log10(e) .* (T).^(-1) .* sigma_tot_T;

#[X', delta_X', Y', delta_Y']

#errorbar(X, Y, delta_X, delta_Y, '~>')
# trasferimento incertezza
stima_w = delta_Y .^ -2;
[stima_A, stima_b, stima_sigma_A, stima_sigma_b] = fit(Y, X, w);

delta_Y_tot = sqrt(delta_Y .^ 2 + (stima_b .* delta_X) .^ 2);
w = delta_Y_tot .^ -2;

# regressione lineare (anche se ce stanno logaritmi)
[A, b, sigma_A, sigma_b] = fit(Y, X, w);

# chi quadro per vedere se siamo inchiappettati
chi_2 = chi2(Y, X, delta_Y_tot, A, b);
# ok, siamo inchiappettati
# rifacciamo i conti sulle incertezze
p = chi_2 / 8;
w_corr = w ./ p;

[A, b, sigma_A, sigma_b] = fit(Y, X, w_corr);

# chi quadro per vedere se tutto torna
chi_2_corr = chi2(Y, X, delta_Y_tot .* sqrt(p), A, b);

# ricavo a (fattore)
a = 10^A;
sigma_a = log(10) * a * sigma_A;
% - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

%  calcolo delta_g dalla tabella
gi = (2*pi./ T).^2 .* Ls;
delta_gi = sqrt ( ( (2*pi) ./ T).^4 .* (sigma_L).^2 + (( 8*pi^2) .* Ls ./ (T.^3)).^2 .* (sigma_tot_T).^2 );

%  metodo 1:
%  media pesata
wi = delta_gi.^(-2);

g1 = sum(gi .* wi) / sum(wi)
dg1 = 1 / sqrt(sum(wi))
chi_g1 = chi2(gi, Ls, delta_gi, g1, 0)
%	correzione chi2
" "
chi_g1_teo = 9;
corr = chi_g1 / chi_g1_teo
delta_gi_post = sqrt(corr)
chi_g1_corr = chi2(gi, Ls, 2.*delta_gi, g1, 0)	% <-- moltiplicare l'errore per 2 va bene!
	display(" ");
%  metodo 2:
%  distribuzione dei valori
g2 = mean(gi)
dg2 = sigma(gi', g2)
#sigma_g2 = sqrt( sum((gi .- g2).^2) / 9)
#dg2 = sqrt( sum((gi .- g2).^2) / 90) # == a dg2
chi_g2 = chi2(gi, Ls, delta_gi, g2, 0)
" "
chi_g2_corr = chi2(gi, Ls, 2.*delta_gi, g2, 0)	% <-- moltiplicare l'errore per 2 va bene!
	display(" ");
g3 = (2*pi/a)^2
dg3 = 8*pi^2*a^(-3)*sigma_a
chi_g3 = chi2(gi, Ls, delta_gi, g3, 0)
%	correzione chi2
" "
chi_g3_teo = 9;
corr = chi_g3 / chi_g3_teo
delta_gi_post = sqrt(corr)
chi_g3_corr = chi2(gi, Ls, 2.*delta_gi, g3, 0)	% <-- moltiplicare l'errore per 2 va bene!

	display(" ");
	display("l, dl, T, dT, g, dg");
[Ls' ones(10,1)*sigma_L T' sigma_tot_T' gi' delta_gi']