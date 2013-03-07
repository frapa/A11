function  [m, D, sigma, mediana, q10, q90] = parametri(data)
% parametri(data)
% Calcola media, varianza campionaria, errore standard
% mediana e percentile 10% e 90%

m = mean(data);
D = var(data); % usa N - 1
sigma = std(data); % errore standard
mediana = median(data);
q10 = quantile(data, 0.1);
q90 = quantile(data, 0.9);

end

