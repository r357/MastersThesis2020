# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import os
s = os.getcwd()+"/Graphs/"

# Plot individual prices
def Price(pairs, ETFs, UIs, paired=False):
    for i, pair in enumerate(pairs):
        
        if paired:
            plt.figure()
            plt.plot(pair["Close_x"], label=ETFs[i])
            plt.legend()
            plt.savefig(s+"1_"+str(i)+"_PricePlot_"+ETFs[i])
            plt.show();
            plt.figure()
            plt.plot(pair["Close_y"], label=UIs[i])
            plt.legend()
            plt.savefig(s+"1_"+str(i)+"_PricePlot_"+UIs[i])
            plt.show();
        
        else: 
            fig, axs = plt.subplots(1,2, figsize=(8,4))
            axs[0].plot(pair["Close_x"], label=ETFs[i])
            axs[1].plot(pair["Close_y"], label=UIs[i], color="C1")
            fig.legend([ETFs[i], UIs[i]])
            plt.savefig(s+"1_"+str(i)+"_Price_"+ETFs[i]+"_"+UIs[i])
            fig.show();
        
        
        


# Plot indexed prices
def PriceIndex(pairs, ETFs, UIs, paired=True):
    for i, pair in enumerate(pairs):

        plt.figure()
        plt.plot(pair["Close_x_INDEX"], label=ETFs[i])
        plt.legend()
        
        if not paired: 
            plt.show();
            plt.figure()
        
        plt.plot(pair["Close_y_INDEX"], label=UIs[i])
        plt.legend()
        
        if paired: 
            plt.savefig(s+"2_"+str(i)+"_PricePlotIndex_"+ETFs[i]+"_"+UIs[i])
        plt.show();
        
        
    
        
# Plot returns
def Returns(pairs, ETFs, UIs, paired=False):
    for i, pair in enumerate(pairs):
        
        if paired:
            plt.figure()
            plt.plot(pair["Return_x"], label=ETFs[i])
            plt.legend()
            plt.plot(pair["Return_y"], label=UIs[i])
            plt.show();
        
        else:
            fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True, figsize=(8,4))
            axs[0].plot(pair["Return_x"], label=ETFs[i])
            axs[1].plot(pair["Return_y"], label=UIs[i], color="C1")
            fig.legend([ETFs[i], UIs[i]])
            plt.savefig(s+"3_"+str(i)+"_ReturnsPlot_"+ETFs[i]+"_"+UIs[i])
            fig.show();




# Plot returns histogram, kernel density
def ReturnsDist(pairs, ETFs, UIs, density=True, normed=True, bins=15, 
                paired=True, hist=True, xlim=False, ylim=False):
    for i, pair in enumerate(pairs):
       
        plt.figure()
        sns.distplot(pair["Return_x"],label=ETFs[i],
                     hist=hist, kde=density, norm_hist=normed, bins=bins)
        plt.legend()
        plt.ylabel("Density")
        
        if xlim: plt.xlim(xlim)
        if ylim: plt.ylim(ylim)
        
        if not paired: 
            plt.show();
            plt.figure()
            plt.ylabel("Density")
            if xlim: plt.xlim(xlim)
            if ylim: plt.ylim(ylim)
            
        sns.distplot(pair["Return_y"], label=UIs[i],
                     hist=hist, kde=density, norm_hist=normed, bins=bins)
        plt.legend()
        plt.savefig(s+"4_"+str(i)+"_ReturnDist_"+ETFs[i]+"_"+UIs[i])
        plt.show();




# Plot paired DIFF and GAP
def DiffGap(pairs, ETFs, UIs, paired=False):
    for i, pair in enumerate(pairs):
    
        if not paired:
            fig, axs = plt.subplots(1, 2, tight_layout=True, figsize=(8,4))
            axs[0].plot(pair["DIFF"])
            # axs[0].set_title("Difference in log prices: " + ETFs[i] + " and " + UIs[i])
            axs[0].set_title("DIFF")
            axs[1].plot(pair["absGAP"])
            # axs[1].set_title("Absolute GAP in log returns: "+ ETFs[i] + " and " + UIs[i])
            axs[1].set_title("|GAP|")
            plt.savefig(s+"5_"+str(i)+"_DiffGap_"+ETFs[i]+"_"+UIs[i])
            plt.show();
            


# Plot Jointplots
def Joint(pairs, ETFs, UIs):
    for i, pair in enumerate(pairs):
            
        plt.figure()
        joint = sns.jointplot(x=pair["Return_x"], y=pair["Return_y"])
        joint.set_axis_labels(ETFs[i], UIs[i])
        plt.tight_layout()
        plt.savefig(s+"6_"+str(i)+"_JointPlot_"+ETFs[i]+"_"+UIs[i])
        plt.show();












