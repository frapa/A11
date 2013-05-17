source("lunghezza.m")

%  calcolo delta_g dalla tabella
gi = (2*pi./ T).^2 .* Ls;
delta_gi = sqrt ( ( (2*pi) ./ T).^4 .* (sigma_L).^2 + (( 8*pi^2) .* Ls ./ (T.^3)).^2 .* (delta_T_corr).^2 );

%  metodo 1:
%  media pesata
wi = delta_gi.^(-2);

g1 = sum(gi .* wi) / sum(wi)
dg1 = 1 / sqrt(sum(wi))
chi_g1 = chi2(gi, Ls, delta_gi, g1, 0)
%	correzione chi2
" "
chi_g1_teo = 9;
corr = chi_g1 / chi_g1_teo
delta_gi_post = sqrt(corr)
chi_g1_corr = chi2(gi, Ls, 2.*delta_gi, g1, 0)	% <-- moltiplicare l'errore per 2 va bene!
	display(" ");
%  metodo 2:
%  distribuzione dei valori
g2 = mean(gi)
dg2 = sigma(gi', g2)
#sigma_g2 = sqrt( sum((gi .- g2).^2) / 9)
#dg2 = sqrt( sum((gi .- g2).^2) / 90) # == a dg2
chi_g2 = chi2(gi, Ls, delta_gi, g2, 0)
" "
chi_g2_corr = chi2(gi, Ls, 2.*delta_gi, g2, 0)	% <-- moltiplicare l'errore per 2 va bene!
	display(" ");
g3 = (2*pi/a)^2
dg3 = 8*pi^2*a^(-3)*sigma_a
chi_g3 = chi2(gi, Ls, delta_gi, g3, 0)
%	correzione chi2
" "
chi_g3_teo = 9;
corr = chi_g3 / chi_g3_teo
delta_gi_post = sqrt(corr)
chi_g3_corr = chi2(gi, Ls, 2.*delta_gi, g3, 0)	% <-- moltiplicare l'errore per 2 va bene!

	display(" ");
	display("l, dl, T, dT, g, dg");
[Ls' ones(10,1)*sigma_L T' sigma_tot_T' gi' delta_gi']

R =  6.3671e+06
g40 = 9.80171
g50 = 9.81071
g46 = (4*g40 + 6*g50)/10
dg = -2*g46*400/R

