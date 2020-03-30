# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

        
        
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





def saveHTML(HTML, filename):
    '''
    profile reports to HTML into a folder:
        ./HTMLs/

    '''

    import os    
    s = os.getcwd()+"/HTMLs/"
    _filename = s + filename + ".html"
    
    with open(_filename, 'w') as file:
        file.write(HTML)




