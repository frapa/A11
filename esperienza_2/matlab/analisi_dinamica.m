% 	mi posiziono nella cartella dati
cd ../
cd dati

% 	carico i dati
dyn_data = csvread("dyn_masse.csv")(2:end,:);
g = 9.806;

% 	porto i dati nelle unità del SI (g --> kg)
dyn_data(:,1) = dyn_data(:,1) ./ 1000;
% 	trasformo le masse in pesi (kg --> N) e traspongo la matrice
dyn_data(:,1) = dyn_data(:,1)  .* g;
dyn_data = dyn_data';
dyn_data(2:16,:) = dyn_data(2:16,:) ./ 10;

%	calcolo l'errore sui pesi
dPi= ones(1,14) .* 0.1 /1000 .*g;

% 	creo i valori medi di ogni periodo
mTi = mean(dyn_data(2:16,:));


% 	cerco la deviazione standard dei periodi

% bsxfun(@minus,dyn_data(2:16,:),mTi);
% (bsxfun(@minus,dyn_data(2:16,:),mTi)).^2;
% sum((bsxfun(@minus,dyn_data(2:16,:),mTi)).^2);
% sum((bsxfun(@minus,dyn_data(2:16,:),mTi)).^2) ./ 15;
dTi = sqrt(sum((bsxfun(@minus,dyn_data(2:16,:),mTi)).^2) ./ 15);
%dTi = dTi .+ (0.0001*0.3);


% 	plotto il grafico:
% 	parabola
%errorbar(dyn_data(1,:),mTi, dPi,dTi, '~>')
% 	retta
%errorbar(dyn_data(1,:),(mTi.^2),dPi,(dTi.^2), '~>')

%	calcolo la devazione standard di Tau^2
dTi2 = (mTi .* dTi) .* 2;


% 	---------------- 4.4.12 !!! roba nuova !!! ----------------
% 	calcolo i pesi wi per dTi2
wi = dTi2 .^(-2);

% 	inizio del calcolo di A e B; faccio osservare che
% 	xi = dyn_data(1,:) ---- yi = mTi.^2
% 	x ≡ m, y ≡ T^2 , A ≡ C^2 me /k, B ≡ C^2 /k.
% 	δxi ≡ δmi ---- δyi ≡ δTi2
%	osservo che δxi << δyi? secondo me no...
		% asd = (dTi2)'; % asd2 = (dPi)'; % asd3 = [asd asd2]'
%	pertanto...

%	stimo il valore di B con i dai sulla molla ottenuti dalla precedente esperienza
%	poiché dPi non è trascurabile rispetto a dTi2, infatti
%[dPi' dTi2' (dPi' ./ dTi2')]
%mean(dPi' ./ dTi2')
B = 4 * pi^2/ 9.64;

%	ottengo quindi i valori per l'incertezza trasferita (dytr)
dytr = dPi .* B;
%	e calcolo quindi la nuova incertezza totale (dyt) e i nuovi pesi (sovrascrivo wi)
dyt = ((dytr.^2 + dTi2.^2)/2).^(0.5);

wi = dyt .^ (-2);

% 	attenzione! non sapendo che lettera mettere per il denominatore ho usato la 'Q' a caso
%	calcolo quindi A e B (finalmente?)
Q = (sum(wi)) * (sum(wi .* (dyn_data(1,:)).^2) ) - ( sum(wi .* dyn_data(1,:)) )^2;
A = ( ( sum(wi .* (dyn_data(1,:)).^2) )*( sum(wi .* (mTi.^2)) ) - (sum(wi .* dyn_data(1,:)))*(sum(wi .* dyn_data(1,:) .* (mTi.^2) )) ) / Q;
B = ( ( sum(wi) )*(sum(wi .* dyn_data(1,:) .* (mTi.^2) )) - (sum(wi .* dyn_data(1,:)))*( sum(wi .* (mTi.^2) ) ) ) / Q;

%	calcolo la deviazione di A e B
dA2 = ( sum(wi .* (dyn_data(1,:)).^2) ) / Q;
dB2 = ( sum(wi) ) / Q;

'A e dA2'
[A dA2]
'B e dB2'
[B dB2]

%	Calcolo C e me da A e B
k= 9.6;
C = sqrt(B * k);
me = A  / B;
%dC =
%dme =



%chi2 = sum ((((mTi.^2) .- A .- ( B .* dyn_data(1,:) )).^2) .* (wi));
chi2 = sum ((((mTi.^2) .- A .- ( B .* dyn_data(1,:) )).^2) ./ (dyt));
chi2 % adesso viene 0.01! ma che cavolo sta succedendo?

%errorbar(dyn_data(1,:),(mTi .- A .- ( B .* dyn_data(1,:) )), dyt,dTi, '~>')

%	che è sta formula?
%	A = sum( (mTi.^2 - dyn_data(1,:).*(4 * pi^2 / 9.64)) ./ (dTi2).^2 )