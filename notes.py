''' # UI VOLUME: Since (natural) log volume is not stationary, detrending was considered:
    
- Some sources (CampbellGrossmanWang93)recommend detrending volume on a mean rolling window basis (n-day moving average)
    This is not ok for this study since we want to observe short-term movements.

- HP Filtering proved too cyclical and left out 2008 and other major trend movements


CONCLUSION:
Volume did not show signs of trends in the selected time window. lnVolume of the UI was used. 
During the coding phase, multiple detrending options were considered yielding similar results.




'''

# Data windows.
'''
- use 2018> for good result for reg2
 
 

'''