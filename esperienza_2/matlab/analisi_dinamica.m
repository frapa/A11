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
dyn_data = dyn_data';
dyn_data(2:16,:) = dyn_data(2:16,:) ./ 10;

dPi= ones(1,14) .* 0.1 /1000 .*g;

% creo i valori medi di ogni periodo
mTi = mean(dyn_data(2:16,:));
% mTi

% cerco la deviazione standard dei periodi

% bsxfun(@minus,dyn_data(2:16,:),mTi);
% (bsxfun(@minus,dyn_data(2:16,:),mTi)).^2;
% sum((bsxfun(@minus,dyn_data(2:16,:),mTi)).^2);
% sum((bsxfun(@minus,dyn_data(2:16,:),mTi)).^2) ./ 15;
dTi = sqrt(sum((bsxfun(@minus,dyn_data(2:16,:),mTi)).^2) ./ 15);
% dTi

errorbar(dyn_data(1,:),mTi, dPi,dTi, '~>')

dTi2 = (mTi .* dTi) .* 2