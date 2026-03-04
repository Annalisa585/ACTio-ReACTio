import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#parameters: w_0=-1, wa=0,  alphaB0=0.1, M2_over_Mpl2 = 0.01
df_mu5 = pd.read_csv("../mu_log_proof5.csv")
df_mymgf5 = pd.read_csv("../mymgF_log_proof5.csv")
#parameters: w_0=-1, wa=0,  alphaB0=0.1, M2_over_Mpl2=0.1
df_mu6 = pd.read_csv("../mu_log_proof6.csv")
df_mymgf6 = pd.read_csv("../mymgF_log_proof6.csv")
#parameters: w_0=-1, wa=0,  alphaB0=0.1, M2_over_Mpl2=-0.1
df_mu7 = pd.read_csv("../mu_log_proof7.csv")
df_mymgf7 = pd.read_csv("../mymgF_log_proof7.csv")
#parameters: w_0=-1, wa=0,  alphaB0=0.1, M2_over_Mpl2=0.5
df_mu8 = pd.read_csv("../mu_log_proof8.csv")
df_mymgf8 = pd.read_csv("../mymgF_log_proof8.csv")
#parameters: w_0=-1, wa=0,  alphaB0=0.1, M2_over_Mpl2=-0.5
df_mu9 = pd.read_csv("../mu_log_proof9.csv")
df_mymgf9 = pd.read_csv("../mymgF_log_proof9.csv")
#parameters: w_0=-1, wa=0,  alphaB0=0.1, M2_over_Mpl2=0.
df_mu10 = pd.read_csv("../mu_log_proof10.csv")
df_mymgf10 = pd.read_csv("../mymgF_log_proof10.csv")

last_call_mu5 = df_mu5.tail(170)
last_call_mu6 = df_mu6.tail(170)
last_call_mu7 = df_mu7.tail(170)
last_call_mu8 = df_mu8.tail(170)
last_call_mu9 = df_mu9.tail(170)
last_call_mu10 = df_mu10.tail(170)

last_call_mymgf5 = df_mymgf5.tail(166)
last_call_mymgf6 = df_mymgf6.tail(165)
last_call_mymgf7 = df_mymgf7.tail(134)
last_call_mymgf8 = df_mymgf8.tail(166)
last_call_mymgf9 = df_mymgf9.tail(135)
last_call_mymgf10 = df_mymgf10.tail(165)

plt.figure(figsize=(10, 6))
plt.plot(last_call_mu5['a'], last_call_mu5['result'], label=r'$M_0=0.01$', color = 'pink', linewidth=2)
plt.plot(last_call_mu6['a'], last_call_mu6['result'], label=r'$M_0=0.1$', color = 'orange', linewidth=2)
plt.plot(last_call_mu7['a'], last_call_mu7['result'], label=r'$M_0=-0.1$', color = 'blue', linewidth=2)
plt.plot(last_call_mu8['a'], last_call_mu8['result'], label=r'$M_0=0.5$', color = 'green', linewidth=2)
plt.plot(last_call_mu9['a'], last_call_mu9['result'], label=r'$M_0=-0.5$', color = 'red', linewidth=2)
plt.plot(last_call_mu10['a'], last_call_mu10['result'], label=r'$M_0=0$', color = 'black', linewidth=2)
plt.xlabel('a', fontsize = 18)
plt.ylabel(r"$\mu_{L}$",fontsize = 18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title(r"$\mu_{L}$ evolution", fontsize = 18)
plt.grid(True)
plt.legend(fontsize=14)

plt.figure(figsize=(10, 6))
plt.plot(last_call_mymgf5['a'], 1+last_call_mymgf5['result'], label=r'$M_0=0.01$', color = 'pink', linewidth=2)
plt.plot(last_call_mymgf6['a'], 1+last_call_mymgf6['result'], label=r'$M_0=0.1$', color = 'orange', linewidth=2)
plt.plot(last_call_mymgf7['a'], 1+last_call_mymgf7['result'], label=r'$M_0=-0.1$', color = 'blue', linewidth=2)
plt.plot(last_call_mymgf8['a'], 1+last_call_mymgf8['result'], label=r'$M_0=0.5$', color = 'green', linewidth=2)
plt.plot(last_call_mymgf9['a'], 1+last_call_mymgf9['result'], label=r'$M_0=-0.5$', color = 'red', linewidth=2)
plt.plot(last_call_mymgf10['a'], 1+last_call_mymgf10['result'], label=r'$M_0=0$', color = 'black', linewidth=2)
plt.xlabel('a', fontsize = 18)
plt.ylabel(r"$\mu_{NL}$", fontsize = 18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title(r"$\mu_{NL}$ evolution", fontsize = 18)
plt.grid(True)
plt.legend(fontsize=14)

data_GR = np.loadtxt("../F5_EFT-PPF_z0.dat")
data5 = np.loadtxt("../case18_z0_5.dat")
data6 = np.loadtxt("../case18_z0_6.dat")
data7 = np.loadtxt("../case18_z0_7.dat")
data8 = np.loadtxt("../case18_z0_8.dat")
data9 = np.loadtxt("../case18_z0_9.dat")
data10 = np.loadtxt("../case18_z0_10.dat")

k_GR = data_GR[:,0]          
P_lin_GR = data_GR[:,1]      
P_nl_GR = data_GR[:,4]

k5 = data5[:,0]          
P_lin5 = data5[:,1]   
P_nl5 = data5[:,4]

k6 = data6[:,0]         
P_lin6 = data6[:,1] 
P_nl6 = data6[:,4]

k7 = data7[:,0]
P_lin7 = data7[:,1]
P_nl7 = data7[:,4]

k8 = data8[:,0]
P_lin8 = data8[:,1]
P_nl8 = data8[:,4]

k9 = data9[:,0]
P_lin9 = data9[:,1]
P_nl9 = data9[:,4]     

k10 = data10[:,0]
P_lin10 = data10[:,1]
P_nl10 = data10[:,4]


plt.figure(figsize=(9,5))
plt.plot(k5, P_lin5/P_lin_GR, label=r'$M_0=0.01\, linear$', color = 'pink', linewidth=2)
plt.plot(k5, P_nl5/P_nl_GR, label=r'$M_0=0.01\, non-linear$', color = 'pink', linestyle = 'dashed', linewidth=2)
plt.plot(k6, P_lin6/P_lin_GR, label=r'$M_0=0.1\, linear$', color = 'orange', linewidth=2)
plt.plot(k6, P_nl6/P_nl_GR, label=r'$M_0=0.1\, non-linear$', color = 'orange', linestyle = 'dashed', linewidth=2)
plt.plot(k8, P_lin8/P_lin_GR, label=r'$M_0=0.5\, linear$', color = 'green', linewidth=2)
plt.plot(k8, P_nl8/P_nl_GR, label=r'$M_0=0.5\, non-linear$', color = 'green', linestyle = 'dashed', linewidth=2)
plt.xscale('log')
plt.xlabel(r"$k \; [h/\mathrm{Mpc}]$", fontsize=18)
plt.ylabel(r"$\frac{P(k)}{P_{\Lambda CDM}(k)}$", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()

plt.figure(figsize=(9,5))
plt.plot(k7, P_lin7/P_lin_GR, label=r'$M_0=-0.1\, linear$', color = 'blue', linewidth=2)
plt.plot(k7, P_nl7/P_nl_GR, label=r'$M_0=-0.1\, non-linear$', color = 'blue', linestyle = 'dashed', linewidth=2)
plt.plot(k9, P_lin9/P_lin_GR, label=r'$M_0=-0.5\, linear$', color = 'red', linewidth=2)
plt.plot(k9, P_nl9/P_nl_GR, label=r'$M_0=-0.5\, non-linear$', color = 'red', linestyle = 'dashed', linewidth=2)
plt.plot(k10, P_lin10/P_lin_GR, label=r'$M_0=0\, linear$', color = 'black', linewidth=2)
plt.plot(k10, P_nl10/P_nl_GR, label=r'$M_0=0\, non-linear$', color = 'black', linestyle = 'dashed', linewidth=2)
plt.xscale('log')
plt.xlabel(r"$k \; [h/\mathrm{Mpc}]$", fontsize=18)
plt.ylabel(r"$\frac{P(k)}{P_{\Lambda CDM}(k)}$", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.show()