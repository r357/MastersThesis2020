# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

        
        
def PairsDescriptiveInfo(pairs, ETFs, UIs, ProfileReport=True):
    from scipy.stats import describe
    import pandas_profiling as pp
    
    for i, pair in enumerate(pairs):
        print(ETFs[i], "\n", describe(pair["Return_x"]), "\n")
        print(UIs[i], "\n", describe(pair["Return_y"]), "\n")
        
        if ProfileReport:
            edaHTML = pp.ProfileReport(pair).to_html()
            name = UIs[i] + "_" + ETFs[i]
            saveDescriptiveHTML(edaHTML, name)



def saveDescriptiveHTML(edaHTML, filename):
    '''
    profile reports to HTML into a folder:
        ./DescriptiveHTMLs/

    '''
    print("---  GENERATING PROFILE REPORT, THIS CAN TAKE SOME TIME  ---")
    import os
    path = os.path.abspath(os.getcwd())
    _filename = path + "/DescriptiveHTMLs/" + filename + ".html"
    with open(_filename, 'w') as file:
        file.write(edaHTML)




