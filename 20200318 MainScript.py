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


importData = 0
CUTdate = 1
Descr = 0
Plot = 0
ecm = 0


##  IMPORT USING YF
# ETFs, UIs, MSCI = YFinance.YFTickers()
# data_etf, data_ui, data_world = YFinance.GetDataYF()

##  IMPORT USING BLOOMBERG EXPORT XLS
if importData:
    ETFs, UIs, MSCI = BloombergTickers()
    data_etf, data_ui, data_world = GetDataBloomberg("/Users/alenrozac/Desktop/Code/20200310 Bloomberg OHLCV.xlsx")
    FullData = GetPairs(data_etf, data_ui)
    

# Good window: 2018-01-01 >    
if CUTdate: pairs = DateCUT(FullData, Dmin="2015-01-01", Dmax="2020-01-01")
else: pairs = FullData


# Descriptives - describing Log Returns
if Descr:
    # descriptives.PairsDescriptiveInfo(pairs, ETFs, UIs, ProfileReport=True)
    # descriptives.GenerateDescHTMLs(pairs, ETFs, UIs)
    descriptives.DescribeColumns(pairs, "lnReturn_x", ETFs)
    descriptives.DescribeColumns(pairs, "lnReturn_y", UIs)


# Plots
if Plot:
    # Plotted returns & Distributions are for Log Returns
    plots.Price(pairs, ETFs, UIs)
    plots.PriceIndex(pairs, ETFs, UIs, paired=True)
    plots.Returns(pairs, ETFs, UIs)
    plots.ReturnsDist(pairs, ETFs, UIs, hist=False, xlim=(-0.05, 0.05), ylim=(0, 80))
    plots.DiffGap(pairs, ETFs, UIs)
    plots.Joint(pairs, ETFs, UIs)
    plots.WorldIndex(data_world)


# Econometrics
if ecm:
    # Stationarity tests on input data
    adf_c = econometrics.StationarityADF(pairs, ETFs, UIs, "c")
    adf_ct = econometrics.StationarityADF(pairs, ETFs, UIs, "ct") 
    
    #Regression 1
    reg1, resids1, Tab1 = econometrics.Regress1(pairs, ETFs, UIs, plot=False, HTMLsave=True)

    # !!! Stationarity test on (write)
    

    # Regression 2
    pairs2 = PairUp2(pairs, data_world)
    reg2, Tab2 = econometrics.Regress2(pairs2, ETFs, UIs, data_world)






# =============================================================================
#  TESTING / BUILDING


plt.plot(pairs[0]["detVolume_x"])
plt.plot(pairs[0]["lnVolume_x"])







def cointTest (pairs, ETFs, display=True):
    from statsmodels.tsa.stattools import coint
    
    cointResults = []
    for i, pair in enumerate(pairs):
        score, pval, _ = coint(pair["Close_x"], pair["Close_y"], trend="ct", autolag="bic")
        print(i, "\t", round(pval, 3), "\t", ETFs[i], "\t", score)
        cointResults.append(pval)
    return(pd.DataFrame(pval, index=ETFs))



# 2-step Engle-Granger (1987)  !!! this works!, use BIC
# Must be under 0.05 
# works 2015-2020
# Performed on price difference, not return difference!
from statsmodels.tsa.stattools import coint
for i, pair in enumerate(pairs):
    y0 = pair["lnClose_x"]
    y1 = pair["lnClose_y"]
    score, pval, _ = coint(y0, y1, trend="ct", autolag="bic")
    print(i, "\t", round(pval,3), "\t",  ETFs[i], "\t", score)
    




def detrend (v, frac=0.05):
    from statsmodels.nonparametric.smoothers_lowess import lowess
    L = pd.DataFrame(lowess(v, np.arange(len(v)), frac=frac, return_sorted=False), index=v.index)
    return (v-L[0])


d1 = detrend(pairs[0]["lnVolume_x"])
d2 = detrend(pairs[0]["lnVolume_x"], frac=2/3)

plt.plot(d1)
plt.plot(d2)
 


# =============================================================================
'''   TO-DO LIST

1. add KPSS to testing?
    
2. Code cointegration again.
    - Cointegration test
    1. show I(1) {not stationary} lnClose_x and lnClose_y
    2. Perform ECM reg1
    3. ADF on resids of reg1
        if I(0): cointegrated series.

'''
# =============================================================================
'''   COMMENTS

1. The plots are not log diffs, but only 1-period diffs
2. Volume is already de-trended as-is (Qadan & Yagil, p.9), used lnUI. - look at notes.
3. GAP is already absolute.
4. Using smf over sm makes it easier for work with constants in regressions.



'''
# =============================================================================
'''   HYPOTHESES

H1: Presence of long run equilibirum (on an efficient market)
    - Stationarity
    - Cointegration
    - ECM performs well (reg1)
    
H2: TE are +corr w Volatility, -corr w Volume
    - coeffs (reg2)

H3: World index can explain TE
    - coeffs (reg2)
    

'''

