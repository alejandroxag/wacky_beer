# Search Function

import pandas as pd

def bs_relation():
    beerStyles = pd.read_csv('data/beerstyles.csv')
    beerStyles['Keys'] = beerStyles.fillna('').astype(str).apply(','.join, axis=1)
    keys = beerStyles['Keys'].tolist()
    beerStyles['Values'] = beerStyles.fillna('').apply(lambda x: list([x['Web'], x['Datafile'], x['API']]), axis=1)
    values = beerStyles['Values'].tolist()
    styleDic = dict(zip(keys,values))
    return styleDic

def bs_search(styleDic, style):
    resultList = list()
    for key in styleDic:
        if style.upper() in key.upper(): resultList.append(key)
    if len(resultList) == 0: return resultList, []
    else: return resultList, [styleDic[st] for st in resultList]
