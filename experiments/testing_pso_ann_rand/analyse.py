import matplotlib.pyplot as plt
import numpy as np

rows = cols = 4
np.random.seed(123)
labels = ['SiO2 + B2O3', '+ Na2O', '+ Al2O3', '+ P2O5', '+ Li2O', '+ ZnO', '+ CaO', '+ K2O', '+ BaO', '+ MgO']
time = ['30sec', '60sec', '300sec', '600sec']
tg = [1100, 900, 750, 400]
tg_names = ['TG 1100', 'TG 900', 'TG 750', 'TG 400']

fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(25, 25), sharey=False)
for i in range(rows):
    for j in range(cols):
        all_data = [np.random.normal(tg[i], std*5, size=100) for std in range(1, 11)]
        axes[i][j].boxplot(x=all_data,
                           notch=True,  # notch shape
                           labels = labels,
                           vert=True)  # vertical box alignment
        #axes[i][j].yaxis.grid(True)
        axes[i][j].grid(axis='y', which='major', linestyle='-', linewidth='0.5', color='gray')
        axes[i][j].axhline(y=tg[i], color='r', linestyle='--')
        axes[i][j].set_ylim(300,1200)
        axes[i][j].set_yticks([300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200])
        axes[i][j].tick_params('y', labelsize=16)
        for tick in axes[i][j].get_xticklabels():
            tick.set_rotation(45)
        if i == 0:
            axes[i][j].set_title(time[j], fontsize=30)
        if i == 3:
            axes[i][j].set_xlabel('Compounds',fontsize=30)
        if j == 0:
            axes[i][j].set_ylabel('TG ($^\circ$K)', rotation=90, fontsize=30)
        # if j == 3:
        #     ax = axes[i][j].twinx()
        #     ax.set_ylabel(tg_names[i], rotation=90, fontsize=30, fontweight='bold')
        #     ax.set_yticklabels([], grid=False)
        axes[i][j].get_yaxis().set_visible(True)

fig.text(x=0.92, y=0.21, s="TG 400",fontsize=30, rotation=90, fontweight='bold')
fig.text(x=0.92, y=0.41, s="TG 750",fontsize=30, rotation=90, fontweight='bold')
fig.text(x=0.92, y=0.61, s="TG 900",fontsize=30, rotation=90, fontweight='bold')
fig.text(x=0.92, y=0.81, s="TG 1100",fontsize=30, rotation=90, fontweight='bold')
fig.suptitle("Experiment 1",fontsize=44, fontweight='bold')
fig.savefig('teste.pdf')
#plt.show()
