import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# Custom functions
from functions.Bloomberg import BloombergTickers, GetDataBloomberg
from functions.YFinance import YFTickers, GetDataYF
from functions.DataWork import GetPairs, DateCUT
from functions.Descriptives import PairsDescriptiveInfo
import functions.Econometrics as econometrics
import functions.Plots as plots


importData = 0
CUTdate = 1
ecm = 1

####    IMPORT USING YF
# ETFs, UIs, MSCI = YFinance.YFTickers()
# data_etf, data_ui, data_world = YFinance.GetDataYF()


####     IMPORT USING BLOOMBERG EXPORT
if importData:
    ETFs, UIs, MSCI = BloombergTickers()
    data_etf, data_ui, data_world = GetDataBloomberg("/Users/alenrozac/Desktop/Code/20200310 Bloomberg OHLCV.xlsx")
    FullData = GetPairs(data_etf, data_ui)
    
if CUTdate:
    pairs = DateCUT(FullData, Dmin="2010-01-01", Dmax = None)




## PLOTS
# PairsDescriptiveInfo(pairs, ETFs, UIs, ProfileReport=True)
# plots.Price(pairs, ETFs, UIs)
# plots.PriceIndex(pairs, ETFs, UIs, paired=True)
# plots.Returns(pairs, ETFs, UIs)
# plots.ReturnsDist(pairs, ETFs, UIs, hist=False, xlim=(-0.05, 0.05), ylim=(0, 80))
# plots.DiffGap(pairs, ETFs, UIs)
# plots.Joint(pairs, ETFs, UIs)



# Econometrics
if ecm:
    reg1, resids1, Tab1 = econometrics.Regress1(pairs, ETFs, UIs, plot=False, HTMLsave=True)






# =============================================================================
#  TESTING / BUILDING


#######    Cointegration

# from statsmodels.tsa.vector_ar.vecm import coint_johansen
# x = pairs[1][["Return_x", "Return_y"]] # dataframe of n series for cointegration analysis
# jres = coint_johansen(x, det_order=0, k_ar_diff=1)
















