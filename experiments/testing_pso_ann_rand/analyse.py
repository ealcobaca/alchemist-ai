import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

AMOUNT_COMP = 10
MAXTG = 1452.0

def get_data(alg, tg, time):
    tg = round(tg/MAXTG,2)
    data = []
    for comp in range(2,AMOUNT_COMP+2):
        filename = alg+'-tg'+str(round(tg,2))+'-c'+str(comp)+'-time'+str(time)+'.csv'
        path_name = 'result/'+alg+'/tg'+str(round(tg,2))+'/c'+str(comp)+'/time'+str(time)+'/'+filename
        col_tg = pd.read_csv(path_name)['TG'].tolist()
        # print(col_tg)
        if alg == 'pso': data.append([float(i[1:(len(i)-1)]) * MAXTG for i in col_tg])
        else: data.append([i*MAXTG for i in col_tg])
    return data

def boxplot(alg, title, file_name, zoom=False):

    nrows = ncols = 4
    labels = ['SiO2 + B2O3', '+ Na2O', '+ Al2O3', '+ P2O5', '+ Li2O', '+ ZnO', '+ CaO', '+ K2O', '+ BaO', '+ MgO']
    time_names = ['30 (sec)', '60 (sec)', '300 (sec)', '600 (sec)']
    time = [30, 60, 300, 600]
    tg = [1100, 900, 750, 400]
    tg_names = ['TG 1100', 'TG 900', 'TG 750', 'TG 400']

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(25, 25), sharey=False)

    for i in range(nrows):
        for j in range(ncols):
            data = get_data(alg, tg[i], time[j])
            axes[i][j].boxplot(x=data,
                               notch=True,  # notch shape
                               labels = labels,
                               vert=True)  # vertical box alignment
            axes[i][j].grid(axis='y', which='major', linestyle='-', linewidth='0.5', color='gray')
            axes[i][j].axhline(y=tg[i], color='r', linestyle='--')

            if zoom == False: axes[i][j].set_ylim(300,1200)

            axes[i][j].tick_params('y', labelsize=16)

            for tick in axes[i][j].get_xticklabels():
                tick.set_rotation(45)

            if i == 0:
                axes[i][j].set_title(time_names[j], fontsize=30)

            if i == 3:
                axes[i][j].set_xlabel('Compounds',fontsize=30)

            if j == 0:
                axes[i][j].set_ylabel('TG ($^\circ$K)', rotation=90, fontsize=30)

            if j == 3:
                ax = axes[i][j].twinx()
                ax.set_ylabel(tg_names[i], rotation=90, fontsize=30, fontweight='bold')
                ax.set_yticklabels([], grid=False)

            axes[i][j].get_yaxis().set_visible(True)

    # fig.text(x=0.92, y=0.21, s="TG 400",fontsize=30, rotation=90, fontweight='bold')
    # fig.text(x=0.92, y=0.41, s="TG 750",fontsize=30, rotation=90, fontweight='bold')
    # fig.text(x=0.92, y=0.61, s="TG 900",fontsize=30, rotation=90, fontweight='bold')
    # fig.text(x=0.92, y=0.81, s="TG 1100",fontsize=30, rotation=90, fontweight='bold')
    fig.suptitle(title,fontsize=44, fontweight='bold')
    fig.savefig(file_name)
    #plt.show()

def boxplot_x(title, file_name, tg, miny, maxy, sep=1):
    nrows = 4
    ncols = 1
    # data1 = [[1,2,3], [4,5,6], [7,9,11]]
    # data2 = [[10,20,30], [40,50,60], [70,90,110]]
    # data3 = [[15,25,35], [45,55,65], [75,95,115]]
    # ticks = ['A', 'B', 'C']
    ticks = ['SiO2 + B2O3', '+ Na2O', '+ Al2O3', '+ P2O5', '+ Li2O', '+ ZnO', '+ CaO', '+ K2O', '+ BaO', '+ MgO']
    time = [30, 60, 300, 600]
    time_names = ['30 (sec)', '60 (sec)', '300 (sec)', '600 (sec)']
    dist = 3.5
    widths = 1.0
    baseline_color = ['#c30101','#940000','#560d0d']

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(20, 25), sharey=False)
    for i in range(nrows):
        data1 = get_data('ann', tg, time[i])
        data2 = get_data('pso',tg, time[i])
        data3 = get_data('ran',tg, time[i])
        bp1 = axes[i].boxplot(data1, positions=np.array(range(len(data1)))*dist-sep, sym='',
                              vert=True, patch_artist=True, widths=widths)
        bp2 = axes[i].boxplot(data2, positions=np.array(range(len(data2)))*dist+0, sym='',
                              vert=True, patch_artist=True, widths=widths)
        bp3 = axes[i].boxplot(data3, positions=np.array(range(len(data3)))*dist+sep, sym='',
                              vert=True, patch_artist=True, widths=widths)

        axes[i].xaxis.set_major_locator(mpl.ticker.FixedLocator((np.array(range(len(ticks)))*dist)))
        axes[i].xaxis.set_major_formatter(mpl.ticker.FixedFormatter((ticks)))
        axes[i].axhline(y=tg - (tg*0.1), color=baseline_color[2], linestyle='-.')
        axes[i].axhline(y=tg - (tg*0.01), color=baseline_color[1], linestyle='--')
        axes[i].axhline(y=tg, color=baseline_color[0], linestyle='-')
        axes[i].axhline(y=tg + (tg*0.01), color=baseline_color[1], linestyle='--')
        axes[i].axhline(y=tg + (tg*0.1), color=baseline_color[2], linestyle='-.')
        axes[i].set_xlim(-2, len(ticks)*dist)
        axes[i].set_ylim(miny, maxy)
        axes[i].set_title(time_names[i], fontsize=20)
        axes[i].set_ylabel('TG ($^\circ$K)', rotation=90, fontsize=20)
        axes[i].grid(axis='y', which='major', linestyle='-', linewidth='0.5', color='gray')
        axes[i].tick_params('y', labelsize=14)

        for tick in axes[i].get_xticklabels():
                tick.set_rotation(45)

        colors = ['#2a4d69','#4b86b4','#adcbe3','#e7eff6','#63ace5']
        j=-1
        for bplot in (bp1, bp2, bp3):
            j+=1
            for patch in bplot['boxes']:
                patch.set_facecolor(colors[j])
        axes[i].legend((bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0]), ('Annealing', 'PSO', 'Random'), loc='upper right')

    axes[3].set_xlabel('Compounds',fontsize=20)
    fig.suptitle(title,fontsize=24, fontweight='bold')
    fig.savefig(file_name)
    #plt.show()

def main():
    boxplot('ann', "Experiment 1: Annealing", "Experiment1_Annealing.pdf")
    boxplot('pso', "Experiment 1: PSO", "Experiment1_PSO.pdf")
    boxplot('ran', "Experiment 1: Random", "Experiment1_RAN.pdf")

    boxplot('ann', "Experiment 1: Annealing zoom", "Experiment1_Annealing_zoom.pdf", True)
    boxplot('pso', "Experiment 1: PSO zoom", "Experiment1_PSO_zoom.pdf", True)
    boxplot('ran', "Experiment 1: Random zoom", "Experiment1_RAN_zoom.pdf", True)

    boxplot_x("Experiment 1: Annealing X PSO X Random (1100)",
              "Experiment1_AnnxPSOxRan_1100.pdf", 1100, 800, 1200)
    boxplot_x("Experiment 1: Annealing X PSO X Random (900)",
              "Experiment1_AnnxPSOxRan_900.pdf", 900, 800, 1000)
    boxplot_x("Experiment 1: Annealing X PSO X Random (750)",
              "Experiment1_AnnxPSOxRan_750.pdf", 750, 650, 850)
    boxplot_x("Experiment 1: Annealing X PSO X Random (400)",
              "Experiment1_AnnxPSOxRan_400.pdf", 400, 375, 600)


if __name__ == "__main__":
    main()
