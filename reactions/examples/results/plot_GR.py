import numpy as np
import matplotlib.pyplot as plt

data_GR = np.loadtxt("../F5_EFT-PPF_z0.dat")
k_GR = data_GR[:,0]          
P_lin_GR = data_GR[:,1]      
P_nl_GR = data_GR[:,4]

plt.loglog(k_GR, P_lin_GR, label='Linear GR', linestyle='--')
plt.loglog(k_GR, P_nl_GR, label='Non-linear GR', linestyle='-')
#plt.xscale('log')
plt.xlabel(r"$k \; [h/\mathrm{Mpc}]$", fontsize=18)
plt.ylabel(r"$P_{\Lambda CDM}(k)$", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.show()