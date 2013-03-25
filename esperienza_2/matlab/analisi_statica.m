% mi posiziono nella cartella dati
cd /home/dejavu/Documents/Laboratorio/A11/esperienza_2/dati

% carico i dati
load masse.csv
load pos_molla1.csv
%load pos_molla2.csv
g = 9.806;

% porto i dati nelle unità del SI
masse = masse ./ 1000;
pesi = masse .* g;
pos_molla1 = (pos_molla1 - 50) ./ (-100);
%pos_molla2 = (pos_molla2 - 50) ./ (-100);
%pos_molla1 = pos_molla2;

% incertezza tipo
dmi = (([1:1:13]' .* 0) + 0.001) ./ sqrt(12);
dpi = dmi .* g;
dz = 0.001 / sqrt(12);
dxi = (([1:1:13]' .* 0) + dz) .* sqrt(2);

% plotto il grafico
errorbar(pesi,masse,dpi,dxi,"~>")

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
