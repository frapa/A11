#	input dati
dati = csvread("../dati/sorted_temp_vs_h.csv");
posizione = dati(:,2)' ./ 100;
temperatura = dati(:,1)';

p0 = 0.98;