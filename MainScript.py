import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
from functions.Bloomberg import BloombergTickers, GetDataBloomberg
from functions.YFinance import YFTickers, GetDataYF
from functions.DataWork import GetPairs, DateCUT, PairUp2
import functions.Descriptives as descriptives
import functions.Econometrics as econometrics
import functions.Plots as plots


importData = 1
CUTdate = 1
Descr = 1
Plot = 1
Ecm = 1


##  IMPORT USING YF
# ETFs, UIs, MSCI = YFinance.YFTickers()
# data_etf, data_ui, data_world = YFinance.GetDataYF()



if importData:    ETFs, UIs, MSCI = BloombergTickers()
    data_etf, data_ui, data_world = GetDataBloomberg("/Users/alenrozac/Desktop/Code/20200310 Bloomberg OHLCV.xlsx")
    FullData = GetPairs(data_etf, data_ui)  
   
    
   

if CUTdate: pairs = DateCUT(FullData, Dmin="2015-01-01", Dmax="2020-01-01")
else: pairs = FullData



if Descr: #logreturns
    # descriptives.PairsDescriptiveInfo(pairs, ETFs, UIs, ProfileReport=True)
    # descriptives.GenerateDescHTMLs(pairs, ETFs, UIs)
    descriptives.DescribeColumns(pairs, "lnReturn_x", ETFs)
    descriptives.DescribeColumns(pairs, "lnReturn_y", UIs)




if Plot:
    # Plotted returns & Distributions are for Log Returns
    plots.Price(pairs, ETFs, UIs)
    plots.PriceIndex(pairs, ETFs, UIs, paired=True)
    plots.Returns(pairs, ETFs, UIs)
    plots.ReturnsDist(pairs, ETFs, UIs, hist=False, xlim=(-0.05, 0.05), ylim=(0, 100))
    plots.DiffGap(pairs, ETFs, UIs)
    plots.Joint(pairs, ETFs, UIs)
    plots.WorldIndex(data_world)




if Ecm:
    # Stationarity tests on input data
    # adf_c = econometrics.StationarityADF(pairs, ETFs, UIs, "c")
    adf_ct = econometrics.StationarityADF(pairs, ETFs, UIs, "ct", display=True) 


    # Cointegration test: Engle-Granger 2-step
    e = econometrics.EngleGranger(pairs, ETFs, UIs, trend="c")

    #Regression 1
    reg1, resids1, Tab1 = econometrics.Regress1(pairs, ETFs, UIs, plot=False, HTMLsave=True)

    # Regression 2
    pairs2 = PairUp2(pairs, data_world)
    reg2, Tab2 = econometrics.Regress2(pairs2, ETFs, UIs, data_world)






# =============================================================================
#  TESTING / BUILDING






