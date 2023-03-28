function [val] = rval
orpath = cd
[file,path] = uigetfile({'*.*'});

npath = path;

cd(npath)
val = readmatrix(file);


plot(val(:,1));

cd(orpath)
end