# -*- coding: utf-8 -*-



# SIMULATION of coefficients give timeframe

import datetime
def date_generator(d):
    from_date = datetime.date(2020,3,1)
    start_date = from_date - datetime.timedelta(days=1)
    return start_date

StartDate_list = []
for i in list(range(1,5000)):
    StartDate_list.append(date_generator(i))


counts = []
for i, start in enumerate(StartDate_list):
    data = DateCUT(FullData, Dmin=start)
    reg1 = econometrics.Regress1(pairs, ETFs, UIs, HTMLsave=False, plot=False)
    coefs=[]
    for r in reg1:
        coefs.append(r.pvalues[2])
    counts.append(sum([1 for i in coefs if i <= 0.05]))
    
for i,_ in enumerate(reg1):
    print(round(reg1[i].pvalues[1],3))

plt.plot(counts)







# =============================================================================

#  DUMP

# from functools import reduce
# df_merged = reduce(lambda left,right: pd.merge(left,right, how='inner', left_index=True, right_index=True), pairs)


# print(np.argmin([len(pair) for pair in pairs]))
# mindate = pairs[3].index[-1]

# for pair in pairs:
#     print(pair.index[0])

# maxdate = 



######   DETRENDING: Volume is already de-trended
t = pairs[0]["lnClose_x"].diff(1)
plt.plot(t)
print(pairs[0].columns)