function out = chi2(data, dy, model)
  % function out = chi2(data, dy, model)
  % Calcola il chi^2 del set di dati fornito in ingresso come:
  % 
  % chi^2 = sum((model - data).^2 ./ dy.^2)
  % 
 
  % M Hueller 18/03/2013
  
  out = sum((model - data).^2 ./ dy.^2);
  
end