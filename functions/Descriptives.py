# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os   

sns.set_style("whitegrid")

        
# Unused
def PairsDescriptiveInfo(pairs, ETFs, UIs, ProfileReport=True):
    from scipy.stats import describe
    import pandas_profiling as pp
    
    print("---  GENERATING PROFILE REPORTS, THIS CAN TAKE SOME TIME  ---")
    
    for i, pair in enumerate(pairs):
        print(ETFs[i], "\n", describe(pair["Return_x"]), "\n")
        print(UIs[i], "\n", describe(pair["Return_y"]), "\n")
        
        if ProfileReport:
            edaHTML = pp.ProfileReport(pair).to_html()
            name = UIs[i] + "_" + ETFs[i]
            saveHTML(edaHTML, name)



# Checked
def saveHTML(HTML, filename, folder=None):
    '''
    profile reports to HTML into a folder:
        ./Descriptives/

    '''
 
    if not folder: 
        s = os.getcwd()+"/Descriptives/" 
    else:
        s = os.getcwd()+"/"+folder+"/"
        
    _filename = s + filename + ".html"
    
    with open(_filename, 'w') as file:
        file.write(HTML)



# Unused
def GenerateDescriptiveDF(pairs, column, names):
    df = pd.DataFrame()
    for i, pair in enumerate(pairs):
        df[str(names[i])] = pair[column]
    return df




# Unused
def GenerateDescHTMLs(pairs, names):
    import pandas_profiling as pp
    returnsETF = GenerateDescriptiveDF(pairs, "Return_x", ETFs, UIs)    
    returnsUI = GenerateDescriptiveDF(pairs, "Return_y", ETFs, UIs)
    returnsETF_HTML = pp.ProfileReport(returnsETF, minimal=True).to_html()
    returnsUI_HTML = pp.ProfileReport(returnsUI, minimal=True).to_html()
    saveHTML(returnsETF_HTML, "returnsETF")
    saveHTML(returnsUI_HTML, "returnsUI")




# OK
def DescribeColumns(pairs, column, names):
    s = os.getcwd()+"/Descriptives/"
    columnDF = GenerateDescriptiveDF(pairs, column, names)
    stats_column = pd.DataFrame()
    
    for c in columnDF.columns:
        stats_column[str(c)] = stats.describe(columnDF[c].dropna().round(5))
        
    a = stats_column.transpose()
    a.columns=["N", "Min_Max", "Mean", "Std", "Skewness", "Kurtosis"]
    a = a.drop("Min_Max", 1)
    a.to_excel(s + column + ".xls")
    
    
    
    
    
    
    
    