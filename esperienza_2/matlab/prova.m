% mi posiziono nella cartella dati
cd ../
cd dati

g = 9.806;
k = 9.64;

dati = csvread("dyn_masse.csv")(2:end,:);
periodi = dati(:,2:end) / 10;
masse = dati(:,1) / 1000;
pesi = masse .* g;

N = length(periodi(1,:));

medie_periodi = mean(periodi, 2);
d = zeros(length(periodi(:,1)), 1);
for i = 1:N
	d += (periodi(:,i) - medie_periodi) .^ 2;
endfor
sigma_periodi = sqrt(d ./ (N - 1));

medie_periodi_2 = medie_periodi .^ 2;
sigma_periodi_2 = 2 * medie_periodi .* sigma_periodi;

% funziona, non toccare!
m1 = sum(sigma_periodi_2 .^ -2);
m2 = sum(masse ./ (sigma_periodi_2 .^ 2));
m3 = sum(masse ./ (sigma_periodi_2 .^ 2));
m4 = sum((masse ./ sigma_periodi_2) .^ 2);
M = [m1, m2; m3, m4];

% termine noto
noto =  [sum(medie_periodi_2 ./ (sigma_periodi_2 .^ 2));
	sum(masse .* medie_periodi_2 ./ (sigma_periodi_2 .^ 2))];

risultato = inv(M) * noto;
A = risultato(1);
B = risultato(2);

m_e = (A * k) / (2 * pi) ^ 2
k_n = (2 * pi) ^ 2 / B