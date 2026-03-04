import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#PASSIAMO DIRETTAMENTE AL CASO n°18
#parameters: w0=-1,  alphaB0=0.1, M2_over_Mpl2 = 0.1, wa = -1.
df_mu18 = pd.read_csv("../mu_log_proof18.csv")
df_mymgf18 = pd.read_csv("../mymgF_log_proof18.csv")
#parameters: w0=-1,  alphaB0=0.1, M2_over_Mpl2 = 0.1, wa = 0.04
df_mu19 = pd.read_csv("../mu_log_proof19.csv")
df_mymgf19 = pd.read_csv("../mymgF_log_proof19.csv")

last_call_mu18 = df_mu18.tail(183)
last_call_mu18.sort_values(by = 'a', ascending = True, inplace = True)
last_call_mu19 = df_mu19.tail(170)

last_call_mymgf18 = df_mymgf18.tail(133)
last_call_mymgf19 = df_mymgf19.tail(133)

plt.figure(figsize=(10, 6))
plt.plot(last_call_mu18['a'], last_call_mu18['result'], label=r'$wa=-1.0$', color = 'orange', linewidth=2)
plt.plot(last_call_mu19['a'], last_call_mu19['result'], label=r'$wa=0.04$', color = 'blue', linewidth=2)
plt.xlabel('a', fontsize = 18)
plt.ylabel(r"$\mu_{L}$", fontsize = 18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title(r"$\mu_{L}$ evolution", fontsize = 18)
plt.grid(True)
plt.legend(fontsize=14)

plt.figure(figsize=(10, 6))
plt.plot(last_call_mymgf18['a'], 1+last_call_mymgf18['result'], label=r'$wa=-1.0$', color = 'orange', linewidth=2)
plt.plot(last_call_mymgf19['a'], 1+last_call_mymgf19['result'], label=r'$wa=0.04$', color = 'blue', linewidth=2)
plt.xlabel('a', fontsize = 18)
plt.ylabel(r"$\mu_{NL}$", fontsize = 18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title(r"$\mu_{NL}$ evolution", fontsize = 18)
plt.grid(True)
plt.legend(fontsize=14)

data_GR = np.loadtxt("../F5_EFT-PPF_z0.dat")
data18 = np.loadtxt("../case18_z0_18.dat")
data19 = np.loadtxt("../case18_z0_19.dat")

k_GR = data_GR[:,0]          
P_lin_GR = data_GR[:,1]      
P_nl_GR = data_GR[:,4]

k18 = data18[:,0]          
P_lin18 = data18[:,1]   
P_nl18 = data18[:,4]

k19 = data19[:,0]        
P_lin19 = data19[:,1]   
P_nl19 = data19[:,4]

plt.figure(figsize=(9,5))
plt.plot(k18, P_lin18/P_lin_GR, label=r'$wa=-1\, linear$', color = 'orange', linewidth=2)
plt.plot(k18, P_nl18/P_nl_GR, label=r'$wa=-1\, non-linear$', color = 'orange', linestyle = 'dashed', linewidth=2)
plt.plot(k19, P_lin19/P_lin_GR, label=r'$wa=0.04\, linear$', color = 'blue', linewidth=2)
plt.plot(k19, P_nl19/P_nl_GR, label=r'$wa=0.04\, non-linear$', color = 'blue', linestyle = 'dashed', linewidth=2)
plt.xscale('log')
plt.xlabel(r"$k \; [h/\mathrm{Mpc}]$", fontsize=18)
plt.ylabel(r"$\frac{P(k)}{P_{\Lambda CDM}(k)}$", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.show()