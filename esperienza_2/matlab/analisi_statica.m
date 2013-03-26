% mi posiziono nella cartella dati
cd ../
cd dati

% carico i dati
load masse.csv
load pos_molla1.csv
% load pos_molla2.csv
g = 9.806;

% porto i dati nelle unità del SI
masse = masse ./ 1000;
pesi = masse .* g;
pos_molla1 = (pos_molla1 - 50) ./ (-100);
% pos_molla2 = (pos_molla2 - 50) ./ (-100);
% pos_molla1 = pos_molla2;

% incertezza tipo
dmi = (ones(13, 1) .* 0.0001) ./ sqrt(12); % incertezze sulle masse
dpi = dmi .* g;

dz = 0.001;
dxi = ones(13, 1) * (dz / sqrt(6));

% plotto il grafico
errorbar(pesi, pos_molla1, dpi, dxi, "~>")

ki = pesi ./ pos_molla1;
dki = ki .* (sqrt((dpi ./ pesi).^2 + (dxi ./ pos_molla1).^2));
[pesi dpi pos_molla1 dxi dki]

% calcolo di k dalla tabella dati
% procedura (a)
wi = dki.^(-2)
k0a = sum(wi .* ki) / sum(wi)
dka = (sum(wi))^(-0.5)

% procedura (b)
k0b = sum(ki) / length(ki)
dkb = sqrt(sum((ki-k0b).^2) / length(ki))

% calcolo di k dal grafico
% metodo (a)
% da fare sulla carta con riga e goniometro!

% metodo (b): regressione lineare
b0 = sum(pesi .* pos_molla1) / sum(pesi.^2)
db = (dz * sqrt(2)) / sum(pesi.^2)

chi2 = sum(((pos_molla1 .- (pesi * b0)).^2) ./ (dxi.^2))
