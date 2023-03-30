listing  = dir('*.txt');



for i=1:length(listing)
    
    f_name = listing(i).name;
    my_v_read(f_name);

end 
