% A script to introduce basic concpets:
%   histogram plotting
%   plot customization
%
% M Hueller 03/2013
%
% $Id: Examples_01.m 3851 2013-03-04 15:18:58Z mauro.hueller $


% Chiudo tutte le figure aperte
close all

% Analisi dei dati: metro a nastro
% TODO create a function here and use real data here
dati_metro = [13.5:0.01:14.5];

% Risoluzione per istogrammi metro a nastro
deltaX_metro = 0.5;

% Definizione del vettore dei bins
x_metro_min = 13.5;
x_metro_max = 14.5;
X_metro = [x_metro_min : deltaX_metro: x_metro_max]';

% Calcolo dei conteggi: bordi
Nb_metro = histc(dati_metro, X_metro);

% Calcolo dei conteggi: centri
Nc_metro = hist(dati_metro, X_metro);

% Uso i dati di bordo
N_metro = Nb_metro;

% Rappresentazione grafica: figura
fig1 = figure();

% Rappresentazione grafica: istogramma misure metro a nastro
h_metro = bar(X_metro, N_metro, 'histc');
% Accediamo agli assi
axs1 = gca;
% Personalizzazione: colore
set(h_metro, 'FaceColor', 'g');
% Personalizzazione: trasparenza
set(h_metro, 'FaceAlpha', 0.5);
% Specifico pi? plot negli stessi assi
hold on
% Oppure, meglio: specifico pi? plot negli stessi assi, e faccio cambiare il colore
set(axs1, 'NextPlot', 'add');
% Personalizzazione: label y
yl = ylabel('Counts');
set(yl, 'FontSize', 24);
% Personalizzazione: label x
xl = xlabel('L [mm]');
set(xl, 'FontSize', 24);
% Personalizzazione: titolo
tl = title('Misure lunghezza');
set(tl, 'fontsize', 24);
% Rappresentazione grafica: istogramma misure calibro
h_calibro = bar(X_metro, 2*N_metro, 'histc');
% Personalizzazione: colore
set(h_calibro, 'FaceColor', 'b');
% Personalizzazione: trasparenza
set(h_metro, 'FaceAlpha', 0.5);
% Personalizzazione: legenda
ll = legend([h_calibro, h_metro], 'Calibro', 'Metro a nastro');
set(ll, 'FontSize', 18, 'Location', 'NorthWest');

% Calcolo frequenza campionaria:
f_metro = N_metro / sum(N_metro);

% Verifico:
disp(sprintf('Somma dei conteggi: %d', sum(N_metro)));
disp(sprintf('Somma delle frequenze campionarie: %d', sum(f_metro)));

% Calcolo frequenza normalizzata:
f_norm_metro = f_metro / deltaX_metro;

% Verifico:
disp(sprintf('Somma frequenze normalizzate: %d', sum(f_norm_metro .* deltaX_metro)));

% Calcolo parametri statistici:
mean_m = mean(dati_metro);
var_m = var(dati_metro);
std_m = std(dati_metro);
median_m = median(dati_metro);
disp(sprintf('Media: %d', mean_m));
disp(sprintf('Varianza campionaria: %d', var_m));
disp(sprintf('Scarto quadratico medio campionario: %d', std_m));
disp(sprintf('Mediana: %d', median_m));

% Plot diverse grandezze nello stesso grafico
fig2 = figure();
[axs, h_left, h_right] = plotyy(X_metro, N_metro, X_metro, f_norm_metro, 'bar');
set(get(axs(1), 'Ylabel'), 'String', 'N []', 'FontSize', 24);
set(get(axs(2), 'Ylabel'), 'String', 'f [mm^-1]', 'FontSize', 24);

