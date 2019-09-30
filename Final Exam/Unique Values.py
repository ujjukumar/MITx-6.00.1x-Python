def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    newList =[]

    for i in aDict.keys():
        ListValues = list(aDict.values())
        j = aDict[i]
        ListValues.remove(j)
        if j not in ListValues:
            newList.append(i)
        
    return newList