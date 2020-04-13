''' # UI VOLUME: Since (natural) log volume is not stationary, detrending was considered:
    
- Some sources (CampbellGrossmanWang93)recommend detrending volume on a mean rolling window basis (n-day moving average)
    This is not ok for this study since we want to observe short-term movements.

- HP Filtering proved too cyclical and left out 2008 and other major trend movements


CONCLUSION:
Volume did not show signs of trends in the selected time window. lnVolume of the UI was used. 
During the coding phase, multiple detrending options were considered yielding similar results.




'''

# DATA WINDOWS
# !!! Dmin="2010-01-01", Dmax="2020-01-01")
'''
- use 2018> for good result for reg2
- Dmin="2010-01-01", Dmax="2020-01-01")
    for cointegrated series
 

'''

# Cointegration
'''
Procedure 1: Enders, W. (2008). Applied econometric time series. John Wiley & Sons.
In essence, the Engle-Granger procedure is a two-step regression approach
https://quant.stackexchange.com/questions/16782/dou-you-have-an-example-of-implementing-engle-granger-2-step-cointegration

- use 2-step & use bic


'''
