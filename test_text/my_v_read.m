function my_v_read(f_name)



    val = readmatrix(f_name);

    figure('Name',f_name);
    tiledlayout(1,3,'TileSpacing','Compact');

    nexttile
    boxplot(val(:,1));
    title('Max. Beschleunigung');
    ylabel('Beschleunigung [m/s^2]')

    nexttile
    boxplot(val(:,2));
    title('Min. Beschleunigung');
    ylabel('Beschleunigung [m/s^2]')

    nexttile
    boxplot(val(:,3));
    title('Max Winkelgeschwindigkeit');
    ylabel('Winkelgeschwindigkeit [Grad/s]')

    f_name = erase(f_name,'.txt');
    %sgtitle(f_name);

end