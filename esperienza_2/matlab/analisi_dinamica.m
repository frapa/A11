% mi posiziono nella cartella dati
cd ../
cd dati

% carico i dati
dyn_data = csvread("dyn_masse.csv")(2:end,:);
g = 9.806;

% porto i dati nelle unità del SI (g --> kg)
dyn_data(:,1) = dyn_data(:,1) ./ 1000;
% trasformo le masse in pesi (kg --> N)
dyn_data(:,1) = dyn_data(:,1)  .* g;

dPi= ones(14,1) .* 0.1 /1000 .*g;

% creo i valori medi di ogni periodo
mTi = mean(dyn_data(:,2:end)');
mTi = mTi';

% cerco la deviazione standard dei periodi
D = sum(((dyn_data(:,2:end) - mTi).^2)')

%D = sum(((dyn_data(:,2:end) - mTi).^2)');
dTi = (D').^(0.5);
dTi
%dTi = 0.01;

%dTi = sqrt(sum((dyn_data(:,2:end) - mTi).^2) ./ 15);
%dTi= dTi'

errorbar(dyn_data(:,1),mTi, dPi,dTi, '~>');