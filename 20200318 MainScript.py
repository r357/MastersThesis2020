import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# Custom functions
from functions.Bloomberg import BloombergTickers, GetDataBloomberg
from functions.YFinance import YFTickers, GetDataYF
from functions.DataWork import GetPairs, DateCUT
import functions.Descriptives as descriptives
import functions.Econometrics as econometrics
import functions.Plots as plots


importData = 0
CUTdate = 0
Descr = 0
Plot = 0
ecm = 0

####    IMPORT USING YF
# ETFs, UIs, MSCI = YFinance.YFTickers()
# data_etf, data_ui, data_world = YFinance.GetDataYF()


####     IMPORT USING BLOOMBERG EXPORT
if importData:
    ETFs, UIs, MSCI = BloombergTickers()
    data_etf, data_ui, data_world = GetDataBloomberg("/Users/alenrozac/Desktop/Code/20200310 Bloomberg OHLCV.xlsx")
    FullData = GetPairs(data_etf, data_ui)
    
    
    
if CUTdate: pairs = DateCUT(FullData, Dmin="2010-01-01", Dmax=None)
else: pairs = FullData



if Descr:
    # descriptives.PairsDescriptiveInfo(pairs, ETFs, UIs, ProfileReport=True)
    # descriptives.GenerateDescHTMLs(pairs, ETFs, UIs)
    descriptives.DescribeColumns(pairs, "Return_x", ETFs)
    descriptives.DescribeColumns(pairs, "Return_y", UIs)



if Plot:
    # N.B. Plotted returns are not log returns
    plots.Price(pairs, ETFs, UIs)
    plots.PriceIndex(pairs, ETFs, UIs, paired=True)
    plots.Returns(pairs, ETFs, UIs)
    plots.ReturnsDist(pairs, ETFs, UIs, hist=False, xlim=(-0.05, 0.05), ylim=(0, 80))
    plots.DiffGap(pairs, ETFs, UIs)
    plots.Joint(pairs, ETFs, UIs)



# Econometrics
if ecm:
    reg1, resids1, Tab1 = econometrics.Regress1(pairs, ETFs, UIs, plot=False, HTMLsave=True)
    adf_c = econometrics.StationarityADF(pairs, ETFs, UIs, "c")
    adf_ct = econometrics.StationarityADF(pairs, ETFs, UIs, "ct") 



# =============================================================================
#  TESTING / BUILDING


#######    Cointegration
# https://towardsdatascience.com/vector-autoregressions-vector-error-correction-multivariate-model-a69daf6ab618"


from statsmodels.tsa.stattools import coint

for i, pair in enumerate(pairs):
    y0 = np.log(pair["Close_x"])
    y1 = np.log(pair["Close_y"])
    score, pval, _ = coint(y0, y1, trend="ct")
    print(i, "\t", round(pval,3), "\t",  ETFs[i])
    

a = pairs[2]["DIFF"]
b = np.log(pairs[2]["Close_y"])-np.log(pairs[2]["Close_x"])
plt.plot(b)




# =============================================================================
#   TO-DO LIST

# 1. Detrend volume
# 2. Writ out hypotheses
# 3. define steps for each h
# 4. Code Model 2
# 5. Code cointegration again.
    # Model 1 - Error Correction Model.
    # Cointegration test





