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
