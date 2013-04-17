% 	mi posiziono nella cartella dati
cd ../
cd dati

% 	carico i dati
dyn_data = csvread("dyn_masse.csv")(2:end,:);
g = 9.806;

% 	porto i dati nelle unità del SI (g --> kg)
dyn_data(:,1) = dyn_data(:,1) ./ 1000;
% 	trasformo le masse in pesi (kg --> N) e traspongo la matrice
%dyn_data(:,1) = dyn_data(:,1)  .* g;
dyn_data = dyn_data';
dyn_data(2:16,:) = dyn_data(2:16,:) ./ 10;

%	calcolo l'errore sui pesi
dPi= ones(1,14) .* 0.1 /1000; %.*g;

% 	creo i valori medi di ogni periodo
mTi = mean(dyn_data(2:16,:));


% 	cerco la deviazione standard dei periodi
dTi = sqrt(sum( (dyn_data(2:16,:) .- (mTi .* ones(15,14))).^2 )./14);
%	e deviazione standard risoluzione
dTris = 0.001 * 0.3;
%dTi = sqrt((dTi.^2) .+ (dTris^2)) ./ sqrt(14);
%	sommo l'errore casuale a quello di risoluzione
%dTi = sqrt((dTi.^2) .+ (dTris^2)) ./ sqrt(14);
%dTi = sqrt( ((dTi.^2)./14) .+ ((dTris^2)/196) );
dTi = sqrt(dTi.^2./15 .+ dTris.^2);


%	calcolo la devazione standard di Tau^2
dTi2 = (mTi .* dTi) .* 2;

% 	plotto il grafico:
% 	parabola
%errorbar(dyn_data(1,:),mTi, dPi,dTi, '~>')
% 	retta
%errorbar(dyn_data(1,:), (mTi.^2), dPi, dTi2, '~>');

% 	---------------- 4.4.12 !!! roba nuova !!! ----------------
% 	calcolo i pesi wi per dTi2
wi = dTi2 .^(-2);

% 	inizio del calcolo di A e B; faccio osservare che
% 	xi = dyn_data(1,:) ---- yi = mTi.^2
% 	x ≡ m, y ≡ T^2 , A ≡ C^2 me /k, B ≡ C^2 /k.
% 	δxi ≡ δmi ---- δyi ≡ δTi2
%	osservo che δxi << δyi?	secondo me se...

%	{		secondo me no...
		 % asd = (dTi2)';  asd2 = (dPi)'; asd3 = [asd asd2]'
%	pertanto...

%	stimo il valore di B con i dai sulla molla ottenuti dalla precedente esperienza
%	poiché dPi non è trascurabile rispetto a dTi2, infatti

%mean(dPi' ./ dTi2')
%B = 4 * pi^2/ 9.64;
%[dPi' dTi2' (dPi'.* B ./ dTi2')]

%	ottengo quindi i valori per l'incertezza trasferita (dytr)
%dytr = dPi .* B;
%	e calcolo quindi la nuova incertezza totale (dyt) e i nuovi pesi (sovrascrivo wi)
%dyt = ((dytr.^2 + dTi2.^2)/2).^(0.5);

%wi = dyt .^ (-2);
%	}

%	attenzione! non sapendo che lettera mettere per il denominatore ho usato la 'Q' a caso
%	calcolo quindi A e B (finalmente?),
Q = sum(wi) * sum(wi .* (dyn_data(1,:).^2)) - sum(wi .* dyn_data(1,:))^2;
A = ( ( sum(wi .* (dyn_data(1,:)).^2) )*( sum(wi .* (mTi.^2)) ) - (sum(wi .* dyn_data(1,:)))*(sum(wi .* dyn_data(1,:) .* (mTi.^2) )) ) / Q;
B = ( ( sum(wi)*sum(wi .* dyn_data(1,:) .* (mTi.^2)) ) - ( sum(wi .* dyn_data(1,:))*sum(wi .* (mTi.^2)) ) ) / Q;

%	calcolo la deviazione di A e B
dA2 = sqrt(( sum(wi .* (dyn_data(1,:)).^2) ) / Q);
dB2 = sqrt(( sum(wi) ) / Q);

display( [A dA2] )
display( [B dB2] )

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
display("")
%	Calcolo C e me da A e B
k = 9.64;
C = sqrt(B * k)
dC = sqrt(k/B)*dB2/2
me = A  / B
dme = sqrt(B^(-2)*dA2^2 + A^2*B^(-4)*dB2^2)
mu = 3*me
dmu = 3*dme
'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
k = 4*(pi^2)/B;
dk = 4*pi^2*B^(-2)*dB2;

k
dk

chi2 = sum ((((mTi.^2) .- A .- ( B .* dyn_data(1,:) )).^2) .* (wi));
chi2 % adesso viene ~21

%	grafico della distanza tra la predizione e i dati
%errorbar(dyn_data(1,:),(mTi.^2) .- A .- ( B .* dyn_data(1,:) ),dPi,dTi2, '~>');