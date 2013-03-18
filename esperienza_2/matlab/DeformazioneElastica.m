
% 1) Esempio di calcolo di una media pesata
% 
% Vettore dei pesi
P = [10:10:100];

% Vettore delle deformazioni
x = [1:1:10] + 0.1*randn(size(x));
 
% Incertezza nelle deformazioni
dx = 0.03 * rand(size(x));

% Stime della costante elastica
k = P./x;

% Calcolo dei pesi 
w = 1./(dx.^2);

% Stima della costante elastica: media pesata
k0 = media_pesata(k, w);

% Incertezza nella stima della costante elastica: propagazione dell'errore 
dk = 1 ./ sqrt(sum(w));

% Plot con barre d'errore sulle ordinate: errorbar
fig = figure();
h = errorbar(P, x, dx);
set(h, 'linestyle', 'none');
set(h, 'marker', '.');
grid on
hold on

% 3) regressione lineare (prop diretta)
% Implemento la formula nel testo ;)
b0 = sum(P .* x) / sum(P.^2);

% 4) Calcolo del modello
model = b0 * P;

% 5) Test del chi^2
chi2 = sum((model - x).^2 ./ dx.^2);

% 6) Plot del modello:
figure(fig)
p = plot(P, model);
set(p, 'color', [1 0 0])
