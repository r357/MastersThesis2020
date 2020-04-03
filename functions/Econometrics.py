import numpy as npimport pandas as pdimport matplotlib.pyplot as pltimport statsmodels.formula.api as smffrom stargazer.stargazer import Stargazerdef Regress1(pairs, ETFs, UIs, plot=False, HTMLsave=False):    Regression1, Resids1 = [], []     for i, pair in enumerate(pairs):                # Shift Diff 1 fwd (t-1)        pair["_DIFF"] = pair["DIFF"].shift(1)                # Regress and append results        model = smf.ols(formula = "lnReturn_x ~ lnReturn_y + _DIFF",                         data = pair, missing = "drop")                # Contd        model.data.xnames = ["0_Const", "1_Return_UI", "2_DIFF_t-1"]        model1 = model.fit()        Regression1.append(model1)        Resids1.append(model1.resid)        print(model1.summary(yname=ETFs[i], xname=["Const", UIs[i],"_DIFF"]))        print()                if plot:            plt.figure()            plt.plot(model1.resid)            plt.show();    # Tabulate results                tab1 = Stargazer([reg for reg in Regression1])    tab1.custom_columns(ETFs, [1]*len(ETFs))    tab1.show_model_numbers(False)    tab1.show_degrees_of_freedom(False)    # tab1.title("Regression 1 Results")    Tab1 = tab1.render_html()    # Save HTML    if HTMLsave:        from functions.Descriptives import saveHTML        saveHTML(Tab1, "Regress1", folder="Results")    return(Regression1, Resids1, Tab1)    def StationarityADF(pairs, ETFs, UIs, regression="c"):    ''' "c" or "ct" for constant/constant w trend '''    from statsmodels.tsa.stattools import adfuller            adf1 = []        testing = ["lnReturn_x", "lnReturn_y", "DIFF", "GAP"]        for i, pair in enumerate(pairs):        _adf = []                for t in testing:            adf = list(adfuller(pair[t], regression=regression))            _adf.append(round(adf[1],3))                print(_adf)        adf1.append(_adf)    return adf1    