import matplotlib.pyplot as plt


def writefile(data_to_write):
    with open('test', 'w', encoding='UTF8') as f:
        f.writelines('\n'.join(data_to_write))


def pltdata(data_to_plot, ylim_low, ylim_high,subplots,pltx, plty):
    plt.subplot(subplots,pltx,plty)
    plt.ylim(ylim_low,ylim_high)
    plt.plot(data_to_plot)
