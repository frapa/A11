dati = csvread("../dati/temp_vs_pos_con_pressure.csv");

posizione = dati(:,1)';
temperatura = dati(:,2)';
pressione_atm = dati(:, 3)';

Pa = pressione_atm;

T = temperatura;
T1 = temperatura(1:22);
T1g = T1(1:11);
T1s = T1(12:end);
T2 = temperatura(23:end);
T2g = T2(1:11);
T2s = T2(12:end);

# errori risoluzione
% temperatura
delta_T_ris = 0.01;
sigma_T_ris = delta_T_ris / sqrt(12);

% posizione
delta_pos_ris = 0.001;
sigma_pos_ris = delta_pos_ris / sqrt(12);


# accelerazione di gravità
g = 9.807;
# densità dell'acqua
d = 1000;	
# posizione iniziale
pos0 = 0.980;

# dislivello h:
H = posizione .- pos0;

H1 = H(1:22); # primo giorno
H1g = H1(1:11);
H1s = H1(12:end);
H2 = H(23:end); # secondo giorno
H2g = H2(1:11);
H2s = H2(12:end);

% errori
sigma_H = sqrt(2) .* sigma_pos_ris;


# calcola pressione parziale vapore acqua (ppva) in pascal
# ad occhio!
function p = ppva(t)
	p = 611 .* 10.^((7.5 .* t)./(237.7 + t));
endfunction

P = Pa + d*g*H;
P1 = P(1:22);
P1g = P1(1:11);
P1s = P1(12:end);
P2 = P(23:end);
P2g = P2(1:11);
P2s = P2(12:end);

sigma_P = d * g * sigma_H;

[A1, B1, dA1, dB1] = fit(P1, T1, ones(1, 22) * sigma_P .^ -2)
[A2, B2, dA2, dB2] = fit(P2, T2, ones(1, 23) * sigma_P .^ -2)

#[A2, B2, dA2, dB2] = fit(P2g(6:11), T2g(6:11), ones(1, 6) * sigma_P .^ -2)

T0_1 =  - A1 / B1
T0_2 =  - A2 / B2
