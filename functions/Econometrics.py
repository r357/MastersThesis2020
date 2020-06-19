import numpy as npimport pandas as pdimport matplotlib.pyplot as pltimport statsmodels.formula.api as smffrom stargazer.stargazer import Stargazerdef Regress1 (pairs, ETFs, UIs, plot=False, display=False, HTMLsave=False):    Regression1, Resids1 = [], []     for i, pair in enumerate(pairs):                # Shift Diff 1 fwd (t-1)        pair["_DIFF"] = pair["DIFF"].shift(1)                # Regress and append results        model = smf.ols(formula = "lnReturn_x ~ lnReturn_y + _DIFF",                         data=pair, missing="drop")                # Contd        model.data.xnames = ["0_Const", "1_Return_UI", "2_DIFF_t-1"]        model1 = model.fit(cov_type='HC3')        Regression1.append(model1)        Resids1.append(model1.resid)        if display: print(model1.summary(yname=ETFs[i],                             xname=["Const", UIs[i],"_DIFF"]))                    if plot:            plt.figure()            plt.plot(model1.resid)            plt.show();        # Tabulate results                tab1 = Stargazer([reg for reg in Regression1])    tab1.custom_columns(ETFs, [1]*len(ETFs))    tab1.show_model_numbers(False)    tab1.show_degrees_of_freedom(False)    # tab1.title("Regression 1 Results")    Tab1 = tab1.render_html()    # Save HTML    if HTMLsave:        from functions.Descriptives import saveHTML        saveHTML(Tab1, "Regress1", folder="Results")    return(Regression1, Resids1, Tab1)     def StationarityADF (pairs, ETFs, UIs, regression="c", toXls=True, display=True):    ''' "c" or "ct" for constant/constant w trend '''    from statsmodels.tsa.stattools import adfuller        print("ADF Stationarity test on lnReturn x, y, diff, gap, detVol")    print("Regression: " +regression)        adf1 = []        testing = ["lnReturn_x", "lnReturn_y", "DIFF", "GAP", "detVolume_x"]        for i, pair in enumerate(pairs):        _adf = []                for t in testing:            adf = list(adfuller(pair[t], regression=regression))            _adf.append(round(adf[1],3)) #pval                if display: print(_adf)        adf1.append(_adf)    if display: print()    adfResults = pd.DataFrame(adf1, index=ETFs, columns=testing)    if toXls:        import os        s = os.getcwd()+"/Results/"        adfResults.to_excel(s + "ADF_" + regression + ".xls")    return adfResults    def Regress2 (pairs2, ETFs, UIs, data_world,display=False, HTMLsave=True):    Regression2 = []    for i, pair in enumerate(pairs2):                # Regress Model 2        model = smf.ols(formula="GAP ~ lnReturn_world + detVolume_x + Sigma_x",                        data=pair, missing="drop")                    # Contd        model.data.xnames = ["0_Const", "1_Return_World", "2_Volume", "3_Volatility"]        model2 = model.fit(cov_type='HC3')        Regression2.append(model2)        if display: print(model2.summary(yname=ETFs[i],                             xname=["Const", "retWorld", "Volume", "Volatility"]))                # Multiply coefs by 100    for reg in Regression2:        reg.params = reg.params * 100    # Tabulate    tab2 = Stargazer([reg for reg in Regression2])    tab2.custom_columns(ETFs, [1]*len(ETFs))    tab2.show_model_numbers(False)    tab2.show_degrees_of_freedom(False)    tab2.add_custom_notes(["Reported coefficients are multiplied by 100."])    Tab2 = tab2.render_html()        # Save HTML    if HTMLsave:        from functions.Descriptives import saveHTML        saveHTML(Tab2, "Regress2", folder="Results")        return(Regression2, Tab2)    def EngleGranger (pairs, ETFs, UIs, trend="ct", display=True):    ''' H0: No cointegration.    Must be <0.05.    '''    from statsmodels.tsa.stattools import coint    cointResults = []        for i, pair in enumerate(pairs):        score, pval, _ = coint(pair["lnClose_x"], pair["lnClose_y"], trend=trend, autolag="bic")        if display: print(i, "\t", round(pval, 3), "\t", ETFs[i], "\t", score)        cointResults.append(pval)        return(pd.DataFrame([np.round(cointResults,4), ETFs, UIs], index=["P_Val", "ETF", "Index"]).T)