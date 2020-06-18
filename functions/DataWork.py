# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np



def PairUp1 (ETF, UI):
    pair = pd.merge(ETF, UI, how='inner', left_index=True, right_index=True)
    pair.dropna(inplace=True)
    
    # Discard anomalies
    pair = pair[(pair["Return_x"] < 0.5) & (pair["Return_x"] > -0.5)]
    pair["DIFF"] = pair["lnClose_y"] - pair["lnClose_x"]
    pair["GAP"] = np.abs(pair["lnReturn_y"] - pair["lnReturn_x"])
    
    # Indices
    pair["Close_x_INDEX"] = pair["Close_x"]/pair["Close_x"][0]
    pair["Close_y_INDEX"] = pair["Close_y"]/pair["Close_y"][0]

    # Generate Detrended Volume
    pair["detVolume_x"] = detrend(pair["lnVolume_x"], frac=2/3)/1000

    return pair



def PairUp2 (pairs, data_world, detrend=True):
    pairs2 = []
    dw = pd.DataFrame()
    
    dw["lnReturn_world"] = data_world[0]["lnReturn"]
    
    for i, pair in enumerate(pairs):
    
        pair2 = pd.merge(pair, dw, how="inner", left_index=True, right_index=True)
        pairs2.append(pair2)
    
    return pairs2





def GetPairs (data_etf, data_ui):
    if len(data_etf) == len(data_ui):
        pairs = [PairUp1(data_etf[i], data_ui[i]) for i, _ in enumerate(data_etf)]
    return(pairs)
 
    



def DateCUT (pairs, Dmin=None, Dmax=None):
    new = []
    for i, pair in enumerate(pairs):
        
        # Make new lists of pairs with new date range
        new.append(pair.loc[Dmin:Dmax])

        # Reindex close for plotting for each pair
        new[i]["Close_x_INDEX"] = new[i]["Close_x"]/new[i]["Close_x"][0]
        new[i]["Close_y_INDEX"] = new[i]["Close_y"]/new[i]["Close_y"][0]
    return new





def detrend (v, frac=0.05):
    from statsmodels.nonparametric.smoothers_lowess import lowess
    L = pd.DataFrame(lowess(v, np.arange(len(v)), frac=frac, return_sorted=False), index=v.index)
    return (v-L[0])






def detrendVolumeLOESS (pairs, colname="lnVolume_x", frac=0.05):
    ''' 
    This function de-trends volume with LOESS nonparametric regression
    Default col name can be changed.
    Default LOESS frac=0.666666666

    https://en.wikipedia.org/wiki/Local_regression
    https://www.statsmodels.org/stable/generated/statsmodels.nonparametric.smoothers_lowess.lowess.html

    '''
    from statsmodels.nonparametric.smoothers_lowess import lowess
    new = "detr_"+colname

    for pair, i in enumerate(pairs):
        col = pairs[colname]
        L = pd.DataFrame(lowess(col, np.arange(len(v)), frac=frac, return_sorted=False), index=col.index)
        pair[new] = col-L[0]

    return pairs





def detrendVolumeAVG (pairs, colname="lnVolume_x", window=30):
    for i, pair in enumerate(pairs):
        pair["detr_AVG_x"] = pair["lnVolume_x"].rolling(window=window).mean()
    return pairs



