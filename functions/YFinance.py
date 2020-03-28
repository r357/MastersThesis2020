import yfinance as yf
import numpy as np
import pandas as pd


def GetData(ticker, start="2000-01-01", end = "2019-09-01"):
    Ticker = yf.Ticker(ticker)
    df = pd.DataFrame(Ticker.history(start=start))
    
    # Calculate Sigma, Returns, Indices - Adjusted data
    df["Sigma"] = np.log( df["High"] / df["Low"] )
    df["Return"] = df["Close"].pct_change()
    df["LnClose"] = np.log(df["Close"])
    return(df)




def YFTickers():
	ETFs = ["IVV", "IYY", "IWM", "ISF.L", "EXS1.DE", "EUE.MI", "1329.T", "2800.HK", "510210.SS", "ES3.SI"]
	UIs = ["^GSPC", "^DJI", "^RUT", "^FTSE", "^GDAXI", "^STOXX50E", "^N225", "^HSI", "^SSEC", "^STI"]
	MSCI = "URTH"
	return(ETFs, UIs, MSCI)




def GetDataYF():
	ETFs, UIs, MSCI = YFTickers()
	data_etf = [GetData(etf) for etf in ETFs]
	data_ui = [GetData(ui) for ui in UIs]
	data_world = GetData(MSCI)
	return(data_etf, data_ui, data_world)
