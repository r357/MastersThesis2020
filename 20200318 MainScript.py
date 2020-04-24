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
CUTdate = 0
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
if CUTdate: pairs = DateCUT(FullData, Dmin="2010-01-01", Dmax="2020-01-01")
else: pairs = FullData


# Descriptives
if Descr:
    # descriptives.PairsDescriptiveInfo(pairs, ETFs, UIs, ProfileReport=True)
    # descriptives.GenerateDescHTMLs(pairs, ETFs, UIs)
    descriptives.DescriveColumns(pairs, "Return_x", ETFs)
    descriptives.DescriveColumns(pairs, "Return_y", UIs)


# Plots
if Plot:
    # N.B. Plotted returns are NOT log returns
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


# 2-step Engle-Granger (1987)  !!! this works!, use BIC
from statsmodels.tsa.stattools import coint
for i, pair in enumerate(pairs):
    y0 = pair["lnClose_x"]
    y1 = pair["lnClose_y"]
    score, pval, _ = coint(y0, y1, trend="ct", autolag="bic")
    print(i, "\t", round(pval,3), "\t",  ETFs[i])









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



# Detrended volume 



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

