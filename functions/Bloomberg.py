# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np



def PrepareBloombergData(tickers, xls_filepath):
    data = []
    xl = pd.ExcelFile(xls_filepath)
    
    for i, sheetname in enumerate(tickers):
        df = pd.DataFrame()
        df = xl.parse(sheetname)
        df.set_index("Dates", inplace=True)
        
        df["Return"] = df["Close"].pct_change()
                
        # Natural logs
        df["Sigma"] = np.log( df["High"] / df["Low"] )
        df["lnClose"] = np.log(df["Close"])
        df["lnReturn"] = df["lnClose"].pct_change()
        df["lnVolume"] = np.log(df["Volume"])

        # Drop NAs and append      
        df = df.dropna()
        data.append(df)
    
    return(data)





def BloombergTickers():
    tickers = ["SPX Index",
               "IVV Equity",
               "DJUST Index",
               "IYY Equity",
               "RU20INTR Index",
               "IWM Equity",
               "UKX Index",
               "ISF LN Equity",
               "DAX Index",
               "DAXEX GY Equity",
               "SX5E Index",
               "EUN2 GY Equity",
               "NKY Index",
               "1329 JT Equity",
               "HSI Index",
               "2800 HK Equity",
               "SHCOMP Index",
               "510210 CH Equity",
               "STI Index",
               "STFF SP Equity"]
    
    world = ["MXWO Index"]
    return(tickers[1::2], tickers[::2], world)




def GetDataBloomberg(xls_filepath):
    
    ETFs, UIs, world = BloombergTickers()
    
    data_etf = PrepareBloombergData(ETFs, xls_filepath)
    data_ui = PrepareBloombergData(UIs, xls_filepath)
    data_world = PrepareBloombergData(world, xls_filepath)
    return(data_etf, data_ui, data_world)







