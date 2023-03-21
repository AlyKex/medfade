%my_dir = 'C:\Users\user\Desktop\medfade_13_02_2022\medfade\hinten umfallen.txt';

cd C:\Users\user\Desktop\medfade_13_02_2022\medfade\Testaaunahmen_neu_neu

listing  = dir('*.txt');
plocation = zeros(length(listing),1);

val = readmatrix(my_dir);


boxplot(val(:,2));

