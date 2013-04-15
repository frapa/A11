% mi posiziono nella cartella dati
cd ../
cd dati

g = 9.806;
k = 9.64;

% dati in input
dati = csvread("dyn_masse.csv")(2:end,:);
periodi = dati(:,2:end) / 10;
masse = dati(:,1) / 1000;
pesi = masse .* g;

N = length(periodi(1,:));

% calcolo le medie dei periodi e relativi errori
medie_periodi = mean(periodi, 2);
d = zeros(length(periodi(:,1)), 1);
for i = 1:N
	d += (periodi(:,i) - medie_periodi) .^ 2;
endfor
sigma_periodi = sqrt(d ./ (N - 1));

% eleviamo al quadrato
medie_periodi_2 = medie_periodi .^ 2;
sigma_periodi_2 = 2 * medie_periodi .* sigma_periodi;

#errorbar(masse, medie_periodi, sigma_periodi)
#errorbar(masse, medie_periodi_2, sigma_periodi_2)

% funziona, non toccare!
% sto usando il metodo dell'inversa per calcolare le solzioni 
% e questo costruisce la matrice (non tutto oin una riga!)
m1 = sum(sigma_periodi_2 .^ -2);
m2 = sum(masse ./ (sigma_periodi_2 .^ 2));
m3 = sum(masse ./ (sigma_periodi_2 .^ 2));
m4 = sum((masse ./ sigma_periodi_2) .^ 2);
M = [m1, m2; m3, m4];

% termine noto
noto =  [sum(medie_periodi_2 ./ (sigma_periodi_2 .^ 2));
	sum(masse .* medie_periodi_2 ./ (sigma_periodi_2 .^ 2))];

risultato = inv(M) * noto;
A = risultato(1)
B = risultato(2)

C = sqrt(B * k)
m_e_C = (A * k) / C ^ 2
m_e_C = A / B % equivalente
k_n = (2 * pi) ^ 2 / B
m_e_2pi = (A * k) / (2 * pi) ^ 2

chi_2 = sum(((medie_periodi_2 - A - B*masse) .^ 2) ./ (sigma_periodi_2 .^ 2))

% prova correzione
nu = 12;
corr = chi_2 / nu

chi_2_corr = sum(((medie_periodi_2 - A - B*masse) .^ 2) ./
	(corr * (sigma_periodi_2 .^ 2)))