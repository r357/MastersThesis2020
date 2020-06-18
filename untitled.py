




def detrendVolume(pairs, colname="lnVolume_x"):
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
		L = pd.DataFrame(lowess(col, np.arange(len(v)), frac=0.05, return_sorted=False), index=col.index)
		pair[new] = col-L[0]

	return pairs
