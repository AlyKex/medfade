orpath = cd;
[file,path] = uigetfile({'*.*'});

npath = path;

cd(npath)
val = readmatrix(file);

ytval = val(:,1);
plot(ytval);
title('Beschleunigungsverlauf')
xlabel('Samples [10 ms]')
ylabel('Beschleunigung [m/s^2]')



cd(orpath)


