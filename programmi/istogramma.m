function istogramma(data)
    % ISTOGRAMMA crea un istogramma
    %    ISTOGRAMMA(data) usa un vettore con i dati per generare un istogramma

    % Chiudo tutte le figure aperte
    close all

    % Definiamo i bins
    delta_x = 0.003; % larghezza dei bins
    x_min = 1.4835;
    x_max = 1.5135;
    bins = [x_min: delta_x : x_max]

    % delta_x = 0.03; % larghezza dei bins
    % x_min = 1.355;
    % x_max = 1.625;
    % bins = [x_min: delta_x : x_max]

    % calcoliamo i conteggi
    counts = histc(data, bins);

    fig = figure();

    % istogramma
    ist = bar(bins, counts, 1, 'histc');

    % Personalizziamo
    set(ist, 'FaceColor', [0.9 0.25 0]);
    set(ist, 'FaceAlpha', 0.5);

    % Asse y
    ly = ylabel('Conteggi');
    set(ly, 'FontName', 'DroidSans');
    set(ly, 'FontSize', 32);
    % Asse x
    lx = xlabel('t [s]');
    set(lx, 'FontSize', 24);

    % titolo
    t = title('Periodo del pendolo');
    set(t, 'FontSize', 24);

end

