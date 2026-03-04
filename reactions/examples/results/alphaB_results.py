import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#parameters: w_0=-1, wa=0, M2_over_Mpl2 = 0.01, alphaB0=0.1
df_mu1 = pd.read_csv("../mu_log_proof1.copy.csv")
df_mymgf1 = pd.read_csv("../mymgf_log_proof1.copy.csv")
#parameters: w_0=-1, wa=0, M2_over_Mpl2 = 0.01, alphaB0=0.5
df_mu2 = pd.read_csv("../mu_log_proof2.csv")
df_mymgf2 = pd.read_csv("../mymgf_log_proof2.csv")
#parameters: w_0=-1, wa=0, M2_over_Mpl2 = 0.01, alphaB0=1.2
df_mu3 = pd.read_csv("../mu_log_proof3.csv")
df_mymgf3 = pd.read_csv("../mymgf_log_proof3.csv")
#parameters: w_0=-1, wa=0, M2_over_Mpl2 = 0.01, alphaB0=2.3
df_mu4 = pd.read_csv("../mu_log_proof4.csv")
df_mymgf4 = pd.read_csv("../mymgf_log_proof4.csv")

last_call_mu1 = df_mu1.tail(170)
last_call_mu2 = df_mu2.tail(170)
last_call_mu3 = df_mu3.tail(170)
last_call_mu4 = df_mu4.tail(182)
last_call_mu4.sort_values(by = 'a', ascending = True, inplace = True)

last_call_mymgf1 = df_mymgf1.tail(166)
last_call_mymgf2 = df_mymgf2.tail(166)
last_call_mymgf3 = df_mymgf3.tail(166)
last_call_mymgf4 = df_mymgf4.tail(166)

plt.figure(figsize=(10, 6))
plt.plot(last_call_mu1['a'], last_call_mu1['result'], label=r'$\alpha_{B,0}=0.1$', color = 'pink', linewidth=2)
plt.plot(last_call_mu2['a'], last_call_mu2['result'], label=r'$\alpha_{B,0}=0.5$', color = 'orange', linewidth=2)
plt.plot(last_call_mu3['a'], last_call_mu3['result'], label=r'$\alpha_{B,0}=1.2$', color = 'blue', linewidth=2)
plt.plot(last_call_mu4['a'], last_call_mu4['result'], label=r'$\alpha_{B,0}=2.3$', color = 'green', linewidth=2)
plt.xlabel('a', fontsize = 18)
plt.ylabel(r"$\mu_{L}$", fontsize = 18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title(r"$\mu_{L}$ evolution", fontsize = 18)
plt.grid(True)
plt.legend(fontsize=14)

plt.figure(figsize=(10, 6))
plt.plot(last_call_mymgf1['a'], 1+last_call_mymgf1['result'], label=r'$\alpha_{B,0}=0.1$', color = 'pink', linewidth=2)
plt.plot(last_call_mymgf2['a'], 1+last_call_mymgf2['result'], label=r'$\alpha_{B,0}=0.5$', color = 'orange', linewidth=2)
plt.plot(last_call_mymgf3['a'], 1+last_call_mymgf3['result'], label=r'$\alpha_{B,0}=1.2$', color = 'blue', linewidth=2)
plt.plot(last_call_mymgf4['a'], 1+last_call_mymgf4['result'], label=r'$\alpha_{B,0}=2.3$', color = 'green', linewidth=2)
plt.xlabel('a', fontsize = 18)
plt.ylabel(r"$\mu_{NL}$", fontsize = 18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title(r"$\mu_{NL}$ evolution",fontsize = 18)
plt.grid(True)
plt.legend(fontsize=14)

plt.figure(figsize=(10, 6))
plt.plot(last_call_mymgf4['a'], 1+last_call_mymgf4['result'], label=r'$\mu_{NL}$', color = 'green')
plt.plot(last_call_mymgf4['a'], 1/last_call_mymgf4['M2_over_Mpl2'], label=r'$Mpl2_over_M2$', color = 'black')
plt.plot(last_call_mu4['a'], last_call_mu4['result'], label=r'$\mu_{L}$', color = 'purple')
plt.xlabel('a')
plt.ylabel('Values')
plt.title(r"$\mu_{L}$ evolution")
plt.grid(True)
plt.legend()


data_GR = np.loadtxt("../case18_z0_1.dat")
data1 = np.loadtxt("../case18_z0_1.dat")
data2 = np.loadtxt("../case18_z0_2.dat")
data3 = np.loadtxt("../case18_z0_3.dat")
data4 = np.loadtxt("../case18_z0_4.dat")

k_GR = data_GR[:,0]          
P_lin_GR = data_GR[:,1]      
P_nl_GR = data_GR[:,4]

k1 = data1[:,0]          
P_lin1 = data1[:,1]   
P_nl1 = data1[:,4]

k2 = data2[:,0]          
P_lin2 = data2[:,1]   
P_nl2 = data2[:,4]

k3 = data3[:,0]          
P_lin3 = data3[:,1]   
P_nl3 = data3[:,4]

k4 = data4[:,0]          
P_lin4 = data4[:,1]   
P_nl4 = data4[:,4]

plt.figure(figsize=(9,5))
plt.plot(k1, P_lin1/P_lin_GR, label=r'$\alpha_{B,0}=0.1\, linear$', color = 'pink', linewidth=2)
plt.plot(k1, P_nl1/P_nl_GR, label=r'$\alpha_{B,0}=0.1\, non-linear$', color = 'pink', linestyle = 'dashed', linewidth=2)
plt.plot(k2, P_lin2/P_lin_GR, label=r'$\alpha_{B,0}=0.5\, linear$', color = 'orange', linewidth=2)
plt.plot(k2, P_nl2/P_nl_GR, label=r'$\alpha_{B,0}=0.5\, non-linear$', color = 'orange', linestyle = 'dashed', linewidth=2)
plt.plot(k3, P_lin3/P_lin_GR, label=r'$\alpha_{B,0}=1.2\, linear$', color = 'blue', linewidth=2)
plt.plot(k3, P_nl3/P_nl_GR, label=r'$\alpha_{B,0}=1.2\, non-linear$', color = 'blue', linestyle = 'dashed', linewidth=2)
plt.plot(k4, P_lin4/P_lin_GR, label=r'$\alpha_{B,0}=2.3\, linear$', color = 'green', linewidth=2)
plt.plot(k4, P_nl4/P_nl_GR, label=r'$\alpha_{B,0}=2.3\, non-linear$', color = 'green', linestyle = 'dashed', linewidth=2)
plt.xscale('log')
plt.xlabel(r"$k \; [h/\mathrm{Mpc}]$", fontsize=18)
plt.ylabel(r"$\frac{P(k)}{P_{\Lambda CDM}(k)}$", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.show()

