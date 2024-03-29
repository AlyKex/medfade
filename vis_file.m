orpath = cd;
[file,path] = uigetfile({'*.*'});

npath = path;
cd(npath)
val = readmatrix(file);

val = val(450:600,1);

th = zeros(length(val), 2);
luth = zeros(length(val), 2);
sturz = zeros(length(val), 2);
sturz(59:65) = 1;

for i=1:length(val(:,1))
    luth(i,1) = 2.8;
    luth(i,2) = 60;
    
    if val(i,1) >= 60
        th(i,1) = 1;
    end
    if val(i,1) <= 2.8
        th(i,2) = 1;
    end
    
end

subplot(3,1,1);
hold on;
plot(val(:,1),'k');
plot(luth(:,1));
plot(luth(:,2),'b');
title('Beschleunigungsverlauf')
xlabel('Samples [10 ms]')
ylabel('Beschleunigung [m/s^2]')

subplot(3,1,2)
hold on;
area(th(:,1));
area(th(:,2));
ylabel('Threshhold Status');
xlabel('Samples [10 ms]');
ylim([0 1.5]);

subplot(3,1,3)
area(sturz);
ylabel('Sturzerkennungs Status');
xlabel('Samples [10 ms]');
ylim([0 1.5]);







cd(orpath)


