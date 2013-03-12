function hist_cil(data1, data2, data3)
    % ISTOGRAMMA crea un istogramma
    %    ISTOGRAMMA(data) usa un vettore con i dati per generare un istogramma

    % Chiudo tutte le figure aperte
    close all

    % Definiamo i bins del metro
     delta_x1 = 1; % larghezza dei bins
     x_min1 = 12.5;
     x_max1 = 14.5;
     bins1 = [x_min1: delta_x1 : x_max1]

    % Definiamo i bins del calibro
     delta_x2 = 0.05; % larghezza dei bins
     x_min2 = 13.675;
     x_max2 = 13.975;
     bins2 = [x_min2: delta_x2 : x_max2]

    % Definiamo i bins del micrometro
     delta_x3 = 0.05; % larghezza dei bins
     x_min3 = 13.675;
     x_max3 = 13.975;
     bins3 = [x_min3: delta_x3 : x_max3]

    % calcoliamo i conteggi e blah blah
     counts1 = histc(data1, bins1);
    % f_norm_counts = counts / sum(counts);
    % norm_counts = counts / ;

     counts2 = histc(data2, bins2);
    % f_norm_counts = counts / sum(counts);
    % norm_counts = counts / ;

     counts3 = histc(data3, bins3);
    % f_norm_counts = counts / sum(counts);
    % norm_counts = counts / ;

    fig = figure();

    % istogramma
    
    %ist_metro = bar(bins1, counts1, 0.8, 'histc');
    %hold on
    %ist2 = bar(bins2, [counts2 counts3], 1, 'grouped');
    %hold on
    %ist_micrometro = bar(bins3, counts3, 0.6, 'grouped');
   
    % ist = plotyy(bins1, counts1, bins2, [counts2 counts3], 'bar')
    
    subplot(1,2,1);
    H1 = bar(bins1,counts1);
    subplot(1,2,2);
    H2 = bar(bins2, counts2);
    set(H2, 'FaceColor', [1 0 0]);
    set(H2, 'FaceAlpha', 0.5);    
    hold on
    H3 = bar(bins3, counts3);
    
    % Personalizziamo
%    set(H2, 'FaceColor', [1 0 0]);
%    set(H2, 'FaceAlpha', 0.5);
    set(H3, 'FaceColor', [0 1 0]);
    set(H3, 'FaceAlpha', 0.5);

    % Asse y
    ly = ylabel('Conteggi');
    set(ly, 'FontName', 'DroidSans');
    set(ly, 'FontSize', 32);
    % Asse x
    lx = xlabel('l [mm]');
    set(lx, 'FontSize', 24);

    % titolo
    t = title('Lunghezza cilindri');
    set(t, 'FontSize', 24);

end
