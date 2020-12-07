#Final Project - Search Function

import pandas as pd

def createDic():
    beerStyles = pd.read_csv('beerstyles.csv')
    beerStyles['Keys'] = beerStyles.fillna('').astype(str).apply(','.join, axis=1) 
    keys = beerStyles['Keys'].tolist()
    beerStyles['Values'] = beerStyles.fillna('').apply(lambda x: list([x['Web'], x['Datafile'], x['API']]), axis=1)
    values = beerStyles['Values'].tolist()
    styleDic = dict(zip(keys,values))
    return styleDic

def search(styleDic):
    userInput = input("Search a beer style: ")
    resultList = list()
    while len(resultList) == 0:
        for key in styleDic:
            if userInput.upper() in key.upper():
                resultList.append(key)
        if len(resultList) == 0:
            userInput = input("Style doesn't exist in the app. Search a beer style: ")
        elif len(resultList) == 1:
            print("Here is what we have for you for %s:" % (styleDic[resultList[0]][0]))
            return styleDic[resultList[0]]
        else:
            i = 1
            for result in resultList:
                print("%d. %s" % (i, styleDic[result][0]))
                i += 1
            userOption = int(input("Here are the potential styles you are looking for. Pick one option: "))
            while userOption not in range(1, len(resultList)+1):
                userOption = int(input("Invalid option. Pick one option: "))
            print("Here is what we have for you for %s:" % (styleDic[resultList[userOption-1]][0]))
            return styleDic[resultList[userOption-1]]

print(search(createDic()))
                
            
        
    
    
