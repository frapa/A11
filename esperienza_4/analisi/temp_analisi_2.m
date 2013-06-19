source('utils.m');

% input dati
fixed_point_format(1);

% 0,11 discesa1 12,22 salita1 
% 23,34 discesa2 35,35 salita2

dati = csvread("../dati/temp_vs_pos.csv");
posizione = dati(:,1)';	% posizione in metri
temperatura = dati(:,2)';	% temperatura in °C
T1 = temperatura(1:22);
T2 = temperatura(23:end);

T1 = temperatura(1:22);
T1g = T1(1:11);
T1s = T1(12:end);
T2 = temperatura(23:end);
T2g = T2(1:11);
T2s = T2(12:end);

% serie 1 residuo 1
T1r1 = [T1(1:3), T1(19:end)];
% serie 1 residuo 2
T1r2 = T1(4:18);
% serie 2 residuo 1
T2r1 = [T2(1:5), T2(18:end)];
% serie 2 residuo 2
T2r2 = T2(6:17);

% errori di risoluzione

% temperatura
delta_T_ris = 0.01;
sigma_T_ris = delta_T_ris / sqrt(12);

% posizione
delta_pos_ris = 0.001;
sigma_pos_ris = delta_pos_ris / sqrt(12);


%	definizioni preliminari
%	accelerazione di gravità
g = 9.807;
%	densità dell'acqua
d = 1000;	% kg * m^(-3)
%	posizione iniziale
pos0 = 0.980;
%	pressione atmosferica ideale
Pa = 0.97*10^5; #?????????????????? mettere dati veri!
Pa1 = 0.96*10^5;
Pa2 = 0.97*10^5;


% dislivello h:
H = posizione .- pos0;
H1 = H(1:22); # primo giorno
H1g = H1(1:11);
H1s = H1(12:end);
H2 = H(23:end); # secondo giorno
H2g = H2(1:11);
H2s = H2(12:end);

% serie 1 residuo 1
H1r1 = [H1(1:3), H1(19:end)];
% serie 1 residuo 2
H1r2 = H1(4:18);
% serie 2 residuo 1
H2r1 = [H2(1:5), H2(18:end)];
% serie 2 residuo 2
H2r2 = H2(6:17);

% errori
sigma_H = sqrt(2) .* sigma_pos_ris

% tiro via un dato
T1_meno = [T1(3:7), T1(9:end)];
H1_meno = [H1(3:7), H1(9:end)];
% stessa cosa su altro set
T1r2_meno = [T1r2(1:5), T1r2(7:end)];
H1r2_meno = [H1r2(1:5), H1r2(7:end)];


%
%
%
% stime stime stime
%
%
%

% stimo l'errore trasferito
display(" ");
[A1, B1, sA1, sB1] = fit(H1, T1, ones(1, 22)*sigma_H^(-2))
% stima per il Io set di dati
sigma_H1_tot = sqrt(sigma_H^2 + B1^2 * sigma_T_ris^2)

display(" ");
[A2, B2, sA2, sB2] = fit(H2, T2, ones(1, 23)*sigma_H^(-2))
% stima per il IIo set di dati
sigma_H2_tot = sqrt(sigma_H^2 + B2^2 * sigma_T_ris^2)

% residuiiiiiiiiiiiiiii
display(" ");
[A1r1, B1r1, sA1r1, sB1r1] = fit(H1r1, T1r1, ones(1, 7)*sigma_H^(-2))
% stima per il Io set di dati
sigma_H1r1_tot = sqrt(sigma_H^2 + B1r1^2 * sigma_T_ris^2)

display(" ");
[A1r2, B1r2, sA1r2, sB1r2] = fit(H1r2, T1r2, ones(1, 15)*sigma_H^(-2))
% stima per il IIo set di dati
sigma_H1r2_tot = sqrt(sigma_H^2 + B1r2^2 * sigma_T_ris^2)

display(" ");
[A2r1, B2r1, sA2r1, sB2r1] = fit(H2r1, T2r1, ones(1, 11)*sigma_H^(-2))
% stima per il Io set di dati
sigma_H2r1_tot = sqrt(sigma_H^2 + B2r1^2 * sigma_T_ris^2)

display(" ");
[A2r2, B2r2, sA2r2, sB2r2] = fit(H2r2, T2r2, ones(1, 12)*sigma_H^(-2))
% stima per il IIo set di dati
sigma_H2r2_tot = sqrt(sigma_H^2 + B2r2^2 * sigma_T_ris^2)

% meno dati
display(" ");
[A1_meno, B1_meno, sA1_meno, sB1_meno] = fit(H1_meno, T1_meno, ones(1, 19)*sigma_H^(-2))
% stima per il Io set di dati
sigma_H1_tot_meno = sqrt(sigma_H^2 + B1_meno^2 * sigma_T_ris^2)

display(" ");
[A1r2_meno, B1r2_meno, sA1r2_meno, sB1r2_meno] = fit(H1r2_meno, T1r2_meno, ones(1, 14)*sigma_H^(-2))
% stima per il Io set di dati
sigma_H1r2_tot_meno = sqrt(sigma_H^2 + B1r2_meno^2 * sigma_T_ris^2)

%
%
%
% regressione
%
%
%

% regressione lineare
display(" ");
[A_1, B_1, sA_1, sB_1] = fit(H1, T1, ones(1, 22)*sigma_H1_tot^(-2))
display(" ");
[A_1_meno, B_1_meno, sA_1_meno, sB_1_meno] = fit(H1_meno, T1_meno, ones(1, 19)*sigma_H1_tot_meno^(-2))
display(" ");
[A_2, B_2, sA_2, sB_2] = fit(H2, T2, ones(1, 23)*sigma_H2_tot^(-2))

display(" ");
[A_1r1, B_1r1, sA_1r1, sB_1r1] = fit(H1r1, T1r1, ones(1, 7)*sigma_H1r1_tot^(-2))
display(" ");
[A_1r2, B_1r2, sA_1r2, sB_1r2] = fit(H1r2, T1r2, ones(1, 15)*sigma_H1r2_tot^(-2))
display(" ");
[A_1r2_meno, B_1r2_meno, sA_1r2_meno, sB_1r2_meno] = fit(H1r2_meno, T1r2_meno, ones(1, 14)*sigma_H1r2_tot_meno^(-2))

display(" ");
[A_2r1, B_2r1, sA_2r1, sB_2r1] = fit(H2r1, T2r1, ones(1, 11)*sigma_H2r1_tot^(-2))
display(" ");
[A_2r2, B_2r2, sA_2r2, sB_2r2] = fit(H2r2, T2r2, ones(1, 12)*sigma_H2r2_tot^(-2))

%
%
%
% chi chi chi chi chi
% 
%
%

display(" ");
chi_1 = chi2(H1, T1, sigma_H1_tot, A_1, B_1)
chi_1_meno = chi2(H1_meno, T1_meno, sigma_H1_tot_meno, A_1_meno, B_1_meno)
chi_2 = chi2(H2, T2, sigma_H2_tot, A_2, B_2)

chi_1r1 = chi2(H1r1, T1r1, sigma_H1r1_tot, A_1r1, B_1r1)
chi_1r2 = chi2(H1r2, T1r2, sigma_H1r2_tot, A_1r2, B_1r2)
chi_1r2_meno = chi2(H1r2_meno, T1r2_meno, sigma_H1r2_tot_meno, A_1r2_meno, B_1r2_meno)

chi_2r1 = chi2(H2r1, T2r1, sigma_H2r1_tot, A_2r1, B_2r1)
chi_2r2 = chi2(H2r2, T2r2, sigma_H2r2_tot, A_2r2, B_2r2)

%
%
%
% correzione
%
%
%

display("\n\n### Correzzioni ###");
sigma_H1_tot_corr = sqrt(sum((H1 - A_1 - B_1*T1).^2) / 20)
sigma_H1_tot_corr / sigma_H1_tot
sigma_H1_tot_corr_meno = sqrt(sum((H1_meno - A_1_meno - B_1_meno*T1_meno).^2) / 19)
sigma_H1_tot_corr_meno / sigma_H1_tot_meno
sigma_H2_tot_corr = sqrt(sum((H2 - A_2 - B_2*T2).^2) / 21)
sigma_H2_tot_corr / sigma_H2_tot

display(" ");
sigma_H1r1_tot_corr = sqrt(sum((H1r1 - A_1r1 - B_1r1*T1r1).^2) / 5)
sigma_H1r1_tot_corr / sigma_H1r1_tot
sigma_H1r2_tot_corr = sqrt(sum((H1r2 - A_1r2 - B_1r2*T1r2).^2) / 13)
sigma_H1r2_tot_corr / sigma_H1r2_tot
sigma_H1r2_tot_corr_meno = sqrt(sum((H1r2_meno - A_1r2_meno - B_1r2_meno*T1r2_meno).^2) / 12)
sigma_H1r2_tot_corr_meno / sigma_H1r2_tot_meno

display(" ");
sigma_H2r1_tot_corr = sqrt(sum((H2r1 - A_2r1 - B_2r1*T2r1).^2) / 9)
sigma_H2r1_tot_corr / sigma_H2r1_tot
sigma_H2r2_tot_corr = sqrt(sum((H2r2 - A_2r2 - B_2r2*T2r2).^2) / 10)
sigma_H2r2_tot_corr / sigma_H2r2_tot

%
%
%
% temperatura
%
%
%

display("\n\n### Temperatura ###");
dT1_corr = sqrt(sigma_H1_tot_corr ^ 2 - sigma_H1_tot ^ 2) / B_1
dT1_corr_meno = sqrt(sigma_H1_tot_corr_meno ^ 2 - sigma_H1_tot_meno ^ 2) / B_1_meno
dT2_corr = sqrt(sigma_H2_tot_corr ^ 2 - sigma_H2_tot ^ 2) / B_2

display(" ");
dT1r1_corr = sqrt(sigma_H1r1_tot_corr ^ 2 - sigma_H1r1_tot ^ 2) / B_1r1
dT1r2_corr = sqrt(sigma_H1r2_tot_corr ^ 2 - sigma_H1r2_tot ^ 2) / B_1r2
dT1r2_corr_meno = sqrt(sigma_H1r2_tot_corr_meno ^ 2 - sigma_H1r2_tot_meno ^ 2) / B_1r2_meno

display(" ");
dT2r1_corr = sqrt(sigma_H2r1_tot_corr ^ 2 - sigma_H2r1_tot ^ 2) / B_2r1
dT2r2_corr = sqrt(sigma_H2r2_tot_corr ^ 2 - sigma_H2r2_tot ^ 2) / B_2r2


%
%
%
% Aggiustamento incertezze A e B
%
%
%
display("\n\n### Aggiustamendo dA e dB ###");
[A_1r1, B_1r1, sA_1r1, sB_1r1] = fit(H1r1, T1r1, ones(1, 7)*sigma_H1r1_tot_corr^(-2))
display(" ");
[A_1r2, B_1r2, sA_1r2, sB_1r2] = fit(H1r2, T1r2, ones(1, 15)*sigma_H1r2_tot_corr^(-2))
display(" ");
[A_1r2_meno, B_1r2_meno, sA_1r2_meno, sB_1r2_meno] = fit(H1r2_meno, T1r2_meno, ones(1, 14)*sigma_H1r2_tot_corr_meno^(-2))

display(" ");
[A_2r1, B_2r1, sA_2r1, sB_2r1] = fit(H2r1, T2r1, ones(1, 11)*sigma_H2r1_tot_corr^(-2))
display(" ");
[A_2r2, B_2r2, sA_2r2, sB_2r2] = fit(H2r2, T2r2, ones(1, 12)*sigma_H2r2_tot_corr^(-2))


%
%
%
% calcolo dello zero assoluto
%
%
%

display("\n\n### 0 assoluto ###");
source("pressioni.m")

Pa1 = mean(press1)
dPa1 = sigma(press1, Pa1)
Pa2 = mean(press2)
dPa2 = sigma(press2, Pa2)

T0_1 = -(Pa1 .+ d*g*A_1)./(d*g*B_1)
T0_1_meno = -(Pa1 .+ d*g*A_1_meno)./(d*g*B_1_meno)
T0_2 = -(Pa2 .+ d*g*A_2)./(d*g*B_2)

T0_1r1 = -(Pa1 .+ d*g*A_1r1)./(d*g*B_1r1)
dT0_1r1 = sqrt((B_1r1*d*g)^-2 * dPa1^2 + B_1r1^-2 *
	sA_1r1^2 + ((Pa1 + d*g*A1r1)/(d*g*B_1r1^2))^2 *
	sB_1r1^2)
	
T0_1r2 = -(Pa1 .+ d*g*A_1r2)./(d*g*B_1r2)

T0_1r2_meno = -(Pa1 .+ d*g*A_1r2_meno)./(d*g*B_1r2_meno)
dT0_1r2_meno = sqrt((B_1r2*d*g)^-2 * dPa1^2 + B_1r2^-2 *
	sA_1r2^2 + ((Pa1 + d*g*A1r2)/(d*g*B_1r2^2))^2 *
	sB_1r2^2)

T0_2r1 = -(Pa2 .+ d*g*A_2r1)./(d*g*B_2r1)
dT0_2r1 = sqrt((B_2r1*d*g)^-2 * dPa2^2 + B_2r1^-2 *
	sA_2r1^2 + ((Pa2 + d*g*A2r1)/(d*g*B_2r1^2))^2 *
	sB_2r1^2)
	
T0_2r2 = -(Pa2 .+ d*g*A_2r2)./(d*g*B_2r2)
dT0_2r2 = sqrt((B_2r2*d*g)^-2 * dPa2^2 + B_2r2^-2 *
	sA_2r2^2 + ((Pa2 + d*g*A2r2)/(d*g*B_2r2^2))^2 *
	sB_2r2^2)