# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np



def PairUp1(ETF, UI):
    pair = pd.merge(ETF, UI, how='inner', left_index=True, right_index=True)
    pair.dropna(inplace=True)
    
    # Discard anomalies
    pair = pair[(pair["Return_x"] < 0.5) & (pair["Return_x"] > -0.5)]
    pair["DIFF"] = pair["lnClose_y"] - pair["lnClose_x"]
    pair["absGAP"] = np.abs(pair["lnReturn_y"] - pair["lnReturn_x"])
    
    # Indices
    pair["Close_x_INDEX"] = pair["Close_x"]/pair["Close_x"][0]
    pair["Close_y_INDEX"] = pair["Close_y"]/pair["Close_y"][0]
    return(pair)



def GetPairs(data_etf, data_ui):
    if len(data_etf) == len(data_ui):
        pairs = [PairUp1(data_etf[i], data_ui[i]) for i, _ in enumerate(data_etf)]
    return(pairs)
 
    


def DateCUT(pairs, Dmin=None, Dmax=None):
    new = []
    for i, pair in enumerate(pairs):
        new.append(pair.loc[Dmin:Dmax])
    return new



