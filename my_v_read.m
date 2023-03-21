function my_v_read(f_name)


    val = readmatrix(f_name);

    figure
    tiledlayout(1,3,'TileSpacing','Compact');

    nexttile
    boxplot(val(:,1));
    title('Max Acc');

    nexttile
    boxplot(val(:,2));
    title('Min Acc');

    nexttile
    boxplot(val(:,3));
    title('Max Gyro Vel');

    f_name = erase(f_name,'.txt');
    sgtitle(f_name);

end