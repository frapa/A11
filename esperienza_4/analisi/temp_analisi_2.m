# input dati

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


# errori di risoluzione

% temperatura
delta_T_ris = 0.01;
sigma_T_ris = delta_T_ris / sqrt(12);

% posizione
delta_pos_ris = 0.001;
sigma_pos_ris = delta_pos_ris / sqrt(12);


#	definizioni preliminari
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


# dislivello h:
H = posizione .- pos0;
H1 = H(1:22); # primo giorno
H1g = H1(1:11);
H1s = H1(12:end);
H2 = H(23:end); # secondo giorno
H2g = H2(1:11);
H2s = H2(12:end);

% errori
sigma_H = sqrt(2) .* sigma_pos_ris


% stimo l'errore trasferito
display(" ");
[A1, B1, sA1, sB1] = fit(H1, T1, ones(1, 22)*sigma_H^(-2))
% stima per il Io set di dati
sigma_H1_tot = sqrt(sigma_H^2 + B1^2 * sigma_T_ris^2)

display(" ");
[A2, B2, sA2, sB2] = fit(H2, T2, ones(1, 23)*sigma_H^(-2))
% stima per il IIo set di dati
sigma_H2_tot = sqrt(sigma_H^2 + B2^2 * sigma_T_ris^2)

# regressione lineare
display(" ");
[A_1, B_1, sA_1, sB_1] = fit(H1, T1, ones(1, 22)*sigma_H1_tot^(-2))
display(" ");
[A_2, B_2, sA_2, sB_2] = fit(H2, T2, ones(1, 23)*sigma_H2_tot^(-2))

%[A_d1, B_d1, sA_d1, sB_d1] = fit(posizione(1:11),temperatura(1:11),sigma_H^(-2))
%[A_s1, B_s1, sA_s1, sB_s1] = fit(posizione(12:22),temperatura(12:22),sigma_H^(-2))
%[A_d2, B_d2, sA_d2, sB_d2] = fit(posizione(23:34),temperatura(23:34),sigma_H^(-2))
%[A_s2, B_s2, sA_s2, sB_s2] = fit(posizione(35:45),temperatura(35:45),sigma_H^(-2))

#	X^2
%chi = chi2(H(1:45),temperatura(1:45),sigma_H,A,B)

display(" ");
chi_1 = chi2(H1, T1, sigma_H1_tot, A_1, B_1)
chi_2 = chi2(H2, T2, sigma_H2_tot, A_2, B_2)

# tiro via un dato
T1_meno = [T1(3:7), T1(9:end)];
H1_meno = [H1(3:7), H1(9:end)];

chi_1 = chi2(H1_meno, T1_meno, sigma_H1_tot, A_1, B_1)

display(" ");
sigma_H1_tot_corr = sqrt(sum((H1 - A_1 - B_1*T1).^2) / 20)
sigma_H1_tot_corr_meno = sqrt(sum((H1_meno - A_1 - B_1*T1_meno).^2) / 20)
sigma_H2_tot_corr = sqrt(sum((H2 - A_2 - B_2*T2).^2) / 21)

sigma_H1_tot_corr / sigma_H1_tot
sigma_H1_tot_corr_meno / sigma_H2_tot

sigma_H2_tot_corr / sigma_H2_tot

%chi_d1 = chi2(H(1:11),temperatura(1:11),sigma_H,A_d1,B_d1)
%chi_s1 = chi2(H(12:22),temperatura(12:22),sigma_H,A_s1,B_s1)
%chi_d2 = chi2(H(23:34),temperatura(23:34),sigma_H,A_d2,B_d2)
%chi_s2 = chi2(H(35:45),temperatura(35:45),sigma_H,A_s2,B_s2)

# calcolo dello zero assoluto
display(" ");
T0_1 = -(Pa1 .+ d*g*A_1)./(d*g*B_1)
T0_2 = -(Pa2 .+ d*g*A_2)./(d*g*B_2)

%T0_d1 = (Pa .+d*g*A_d1)./(d*g*B_d1)
%T0_s1 = (Pa .+d*g*A_s1)./(d*g*B_s1)
%T0_d2 = (Pa .+d*g*A_d2)./(d*g*B_d2)
%T0_s2 = (Pa .+d*g*A_s2)./(d*g*B_s2)
