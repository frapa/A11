function m = media_pesata(dati, pesi)
  % function m = media_pesata(dati, pesi) 
  % Calcola la media pesata del vettore dati, pesata sul vettore pesi
  % 
  
  % M Hueller 18/03/2013
  
  % Verifico che il vettore pesi non sia vuoto
  if ~isempty(pesi)
    % Controllo le dimensioni del vettore pesi
    if ~isequal(size(dati), size(pesi))
      error('Vettore pesi e vettore dati devono avere le stesse dimensioni!')
    else
      % Tutto bene
      m = sum(dati .* pesi) ./ sum(pesi);
    end
  else
    % Nel caso il vettore pesi sia vuoto, ritorno la media 'classica'
    warning('Vettore pesi vuoto. Applico la media!');
    m = mean(dati);
  end
end