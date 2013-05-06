% 	mi posiziono nella cartella dati
cd ../
cd dati

% 	carico i dati
lunghezze = [105.700 ,csvread("lunghezza.csv")(1,:) ];
periodi = [csvread("pendolo_masse.csv")(2:11,3), csvread("lunghezza.csv")(2:end,:) ];
% g = 9.806;

%	rielaboro i dati in SI
lunghezze = lunghezze ./ 100
periodi = periodi ./ 5

%	calcolo il periodo medio
rms_periodi = sqrt( sum(periodi .^2) ./ 10)
sigma_periodi = (rms_periodi .- periodi).^2
ris_periodi = 0.01 / sqrt(12) / 5;