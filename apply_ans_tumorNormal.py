# ans_tumorNormal.py
# 
# Applying ANS on cancer-normal pair 
# Cancer type 32: Breast Invasive Carcinoma
# Normal cells 33: Breast Normal-Breast Invasive Carcinoma
#
# Available cancer types:
# Major cancer types = 
# [28,30,32,34,36,38,42,44,46]
# Type names = 
# ['Prostate','Lung squamous cell','Breast','Thyroid','Lung adenocarcinoma','Kidney','Colorectal','Head & neck','Liver']
#===================================================================================================

import matplotlib as mpl
#mpl.use('Agg')
mpl.rcParams['font.family']='Times'
import numpy as np
import matplotlib.pyplot as plt
from ans import ans

#=============
# Parameters
#=============
name ='Breast'
numBins = 10

#======================================
# Load activation on breast cancer
#======================================
cellTypeIdx = 2
cellType = 32

#--------------------------------
# Generate labels (L)
# Cancer first, normal last
#--------------------------------
L = np.load('./Data/L_c'+str(cellType)+'.npy')

#--------------------------------
# Get activation values (A)
#--------------------------------
A = np.load('./Data/A_c'+str(cellType)+'.npy')

#==================================
# Applying ANS on breast cancer
#==================================
NED, NED0, NED1, sns_incr, sns_bi, g0Count, g1Count = ans(A, L, numBins)

#------------------------------------------------
# Sort accoring to sns with binary distribution
#------------------------------------------------

CE_idx = sns_bi.argsort()
sortedCE = sns_bi[sns_bi.argsort()]

#-----------------------------------------------
# A stacked bar plot on bin counts - Combined
#-----------------------------------------------
myblue = '#%02x%02x%02x' % (0,107,164)
myred = '#%02x%02x%02x' % (214,39,40)

width = 0.7 # width of the bars
numBins = 10
label1 = 1
label2 = 0
lNames = ['Cancer','Normal']

#------------------------------
# Histogram of the best node
#------------------------------
targetNode = CE_idx[0]
ind = np.arange(numBins)

fig = plt.figure(figsize=(5,5))
p1 = plt.bar(ind,g1Count[targetNode,],width,color=myred,bottom=g0Count[targetNode,],hatch='//')
p2 = plt.bar(ind,g0Count[targetNode,],width,color=myblue)

plt.ylabel('Counts',fontsize=17)
plt.xlabel('Activation bin middle value ($10^{-2}$)',fontsize=17)
plt.title('Node '+str(targetNode+1)+', SNS=%.4f' %(sns_bi[targetNode]),fontsize=17)
plt.xticks(ind,(' 5',' 15',' 25',' 35',' 45',' 55',' 65',' 75',' 85',' 95'))
plt.tick_params(labelsize=15)
plt.tight_layout()

lg = plt.legend((p1[0],p2[0]),(lNames[0],lNames[1]),loc='upper center',title=name)
plt.setp(lg.get_title(),fontsize=15)

plt.show()
fig.savefig('./Plots/tumNor_c'+str(cellType)+'_best.png')

#--------------
# SNS curve
#--------------
fig = plt.figure(figsize=(10,3))

ceox = np.arange(len(sns_bi))
plt.plot(ceox,sortedCE,'k', linewidth=2, label='SNS with binary distr.')

plt.legend(loc='lower right')

xlocation = np.arange(0,len(sns_bi),10)
xlabels = CE_idx[xlocation] + 1
plt.xticks(xlocation, xlabels, rotation='vertical')

plt.ylabel('SNS',fontsize=17)
plt.xlabel('Sorted nodes (in original node number)',fontsize=17)
plt.title(name,fontsize=17)
plt.xlim([-3,260])
plt.ylim([0,1.05])
plt.tight_layout()
plt.show()
fig.savefig('./Plots/tumNor_c'+str(cellType)+'_sns.png')

#--------------
# Plot NED
#--------------
fig = plt.figure(figsize=(10,3))

nedRed = '#%02x%02x%02x' % (214,39,40)
nedx = np.arange(len(NED))
plt.plot(nedx,NED[CE_idx],'k', linewidth=2, label='NED')
plt.plot(nedx,NED0[CE_idx],':',mfc=myblue, linewidth=2,label='$NED_0$')
plt.plot(nedx,NED1[CE_idx],'--',mfc=nedRed,linewidth=2, label='$NED_1$')

plt.legend(loc='lower right')

plt.ylabel('NED',fontsize=17)
plt.xlabel('Sorted by SNS',fontsize=17)
plt.title(name,fontsize=17)
plt.xlim([-3,305])
plt.tight_layout()
plt.show()
fig.savefig('./Plots/tumNor_c'+str(cellType)+'_NED.png')






