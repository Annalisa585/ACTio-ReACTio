import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#IL SEGUENTE CASO n°11 NON SERVE
#parameters: wa=0,  alphaB0=0.1, M2_over_Mpl2 = 0.1, w0 = -1.8
#parameters: wa=0,  alphaB0=0.1, M2_over_Mpl2 = 0.1, w0 = -1.1
df_mu12 = pd.read_csv("../mu_log_proof12.csv")
df_mymgf12 = pd.read_csv("../mymgF_log_proof12.csv")
#parameters: wa=0,  alphaB0=0.1, M2_over_Mpl2 = 0.1, w0 = -0.9
df_mu13 = pd.read_csv("../mu_log_proof13.csv")
df_mymgf13 = pd.read_csv("../mymgF_log_proof13.csv")
#parameters: wa=0,  alphaB0=0.1, M2_over_Mpl2 = 0.1, w0 = -0.7
df_mu14 = pd.read_csv("../mu_log_proof14.csv")
df_mymgf14 = pd.read_csv("../mymgF_log_proof14.csv")

last_call_mu12 = df_mu12.tail(n=157)
last_call_mu13 = df_mu13.tail(n=157)
last_call_mu14 = df_mu14.tail(n=157)

last_call_mymgf12 = df_mymgf12.tail(n=166)
last_call_mymgf13 = df_mymgf13.tail(n=166)
last_call_mymgf14 = df_mymgf14.tail(n=166)

plt.figure(figsize=(10, 6))
plt.plot(last_call_mu12['a'], last_call_mu12['result'], label=r'$w0=-1.1$', color = 'orange', linewidth=2)
plt.plot(last_call_mu13['a'], last_call_mu13['result'], label=r'$w0=-0.9$', color = 'blue', linewidth=2)
plt.plot(last_call_mu14['a'], last_call_mu14['result'], label=r'$w0=-0.7$', color = 'green', linewidth=2)
plt.xlabel('a', fontsize = 18)
plt.ylabel(r"$\mu_{L}$", fontsize = 18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title(r"$\mu_{L}$ evolution", fontsize = 18)
plt.grid(True)
plt.legend(fontsize=14)

plt.figure(figsize=(10, 6))
plt.plot(last_call_mymgf12['a'], 1+last_call_mymgf12['result'], label=r'$w0=-1.1$', color = 'orange',linewidth=2)
plt.plot(last_call_mymgf13['a'], 1+last_call_mymgf13['result'], label=r'$w0=-0.9$', color = 'blue',linewidth=2)
plt.plot(last_call_mymgf14['a'], 1+last_call_mymgf14['result'], label=r'$w0=-0.7$', color = 'green',linewidth=2)
plt.xlabel('a', fontsize = 18)
plt.ylabel(r"$\mu_{NL}$", fontsize = 18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title(r"$\mu_{NL}$ evolution", fontsize = 18)
plt.grid(True)
plt.legend(fontsize=14)

data_GR = np.loadtxt("../F5_EFT-PPF_z0.dat")
data12 = np.loadtxt("../case18_z0_12.dat")
data13 = np.loadtxt("../case18_z0_13.dat")
data14 = np.loadtxt("../case18_z0_14.dat")

k_GR = data_GR[:,0]          
P_lin_GR = data_GR[:,1]      
P_nl_GR = data_GR[:,4]

k12 = data12[:,0]          
P_lin12 = data12[:,1]   
P_nl12 = data12[:,4]

k13 = data13[:,0]        
P_lin13 = data13[:,1]   
P_nl13 = data13[:,4]

k14 = data14[:,0]
P_lin14 = data14[:,1]
P_nl14 = data14[:,4]

plt.figure(figsize=(9,5))
plt.plot(k12, P_lin12/P_lin_GR, label=r'$w0=-1.1\, linear$', color = 'orange', linewidth=2)
plt.plot(k12, P_nl12/P_nl_GR, label=r'$w0=-1.1\, non-linear$', color = 'orange', linestyle='--', linewidth=2)   
plt.plot(k13, P_lin13/P_lin_GR, label=r'$w0=-0.9\, linear$', color = 'blue', linewidth=2)
plt.plot(k13, P_nl13/P_nl_GR, label=r'$w0=-0.9\, non-linear$', color = 'blue', linestyle='--', linewidth=2)
plt.plot(k14, P_lin14/P_lin_GR, label=r'$w0=-0.7\, linear$', color = 'green', linewidth=2)
plt.plot(k14, P_nl14/P_nl_GR, label=r'$w0=-0.7\, non-linear$', color = 'green', linestyle='--', linewidth=2)
plt.xscale('log')
plt.xlabel(r"$k \; [h/\mathrm{Mpc}]$", fontsize=18)
plt.ylabel(r"$\frac{P(k)}{P_{\Lambda CDM}(k)}$", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=10)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.show()
