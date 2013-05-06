#	dati in input
dati = csvread("../dati/sorted_temp_vs_h.csv");
dati2 = csvread("../dati/pressure.csv");
%temp_cresc = csvread("../dati/cresc_temp.csv");
%temp_disc = csvread("../dati/disc_temp.csv");
temperatura = dati(:,1)';
posizione = dati(:,2)' ./100;
%pos_cresc = temp_cresc(:,2)' ./100
%pos_disc = temp_disc(:,2)' ./100
pos_ini = 0.98;

#	errori di risoluzione
%	temperatura
delta_T_ris = 0.01;
sigma_t_ris = delta_T_ris / 2;
%	posizione
pos_delta_ris = 0.001;
pos_sigma_ris = pos_delta_ris ./2;

#	altezza h:
%	valori
H = posizione .- pos_ini;
%H_disc = pos_disc .- pos_ini;
%H_cresc = pos_cresc .- pos_ini;
%	errori
sigma_H_ris = sqrt(2) .* pos_sigma_ris;	% <-- sqrt(2*pos_sigma_ris^2)

t = 0:0.1:6.3;
          plot (t, cos(t), "-;cos(t);", t, sin(t), "+3;sin(t);");
%plot(temperatura,posizione);
%gtemp = plotyy(temperatura,H_disc,0:1:22,0:1:22)%temperatura,H_cresc)
%plot(temperatura,H_disc);
%[A, B, sA, sB] = fit(H,temperatura,sigma_H_ris^(-2))
%plot(temperatura, H-A-B.*temperatura)
%C = chi2(H, temperatura, sigma_H_ris, A, B)