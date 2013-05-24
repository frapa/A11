dati1 = csvread("../dati/first/pressure.csv");
dati2 = csvread("../dati/second/pressure.csv");

press1 = dati1(:, 1) * 100; # conversione a Pascal
press2 = dati2(:, 1) * 100; # conversione a Pascal

temp1 = dati1(:, 2);
temp2 = dati2(:, 2);

umid1 = dati1(:, 3);
umid2 = dati2(:, 3);

ora1 = dati1(:, 4);
ora2 = dati2(:, 4);

# media pressioni
MP1 = [mean(press1(1:5)), mean(press1(6:10)), mean(press1(11:end))]
MP2 = [mean(press2(1:5)), mean(press2(6:10)), mean(press2(11:end))]