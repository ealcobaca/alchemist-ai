import matplotlib.pyplot as plt
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


def main():
    boxplot('ann', "Experiment 1: Annealing", "Experiment1_Annealing.pdf")
    boxplot('pso', "Experiment 1: PSO", "Experiment1_PSO.pdf")
    boxplot('ran', "Experiment 1: Random", "Experiment1_RAN.pdf")

    boxplot('ann', "Experiment 1: Annealing zoom", "Experiment1_Annealing_zoom.pdf", True)
    boxplot('pso', "Experiment 1: PSO zoom", "Experiment1_PSO_zoom.pdf", True)
    boxplot('ran', "Experiment 1: Random zoom", "Experiment1_RAN_zoom.pdf", True)


if __name__ == "__main__":
    main()
