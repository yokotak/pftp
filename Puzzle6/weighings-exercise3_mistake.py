#Programming for the Puzzled -- Srini Devadas
#Find the Fake
#Given a collection of coins, one of which is fake and is slightly heavier
#find the counterfeit using a minimum number of weighings.

#The procedure splits coin pile into 3 groups
def splitCoins(coinsList):
    length = len(coinsList)
    group1 = coinsList[0:length//3]
    group2 = coinsList[length//3:length//3*2]
    group3 = coinsList[length//3*2:length]
    return group1, group2, group3
    
#This procedure compares the weight of 2 groups like a balance
def compare(groupA, groupB):
    if sum(groupA) > sum(groupB):
        result = 'left'
    elif sum(groupB) > sum(groupA):
        result = 'right'
    elif sum(groupB) == sum(groupA): #Could just be an else
        result = 'equal'
    return result

#This procedure finds the fake coin group, knowing that the
#fake coin is heavier
def findFakeGroup(group1, group2, group3):
    result1and2 = compare(group1, group2)
    
    if result1and2 == 'left':
        result1and3 = compare(group1, group3)
        if result1and3 == 'left':
            fakeGroup = [group1]
        else:
            fakeGroup = [group1, group3]
    elif result1and2 == 'right':
        result2and3 = compare(group2, group3)
        if result2and3 == 'left':
            fakeGroup = [group2]
        else:
            fakeGroup = [group2, group3]
    elif result1and2 == 'equal': #Could just be an else
        result1and3 = compare(group1, group3)
        if result1and3 == 'left':
            fakeGroup = [group1, group2]
        else:
            fakeGroup = [group3]
        
    return fakeGroup
    

#This procedure iteratively keeps dividing the pile into 3 smaller piles and
#using the balance to choose one of the smaller piles until the fake coin is found
def CoinComparison(coinsList):
    #Make a copy of coinsList
    currList = [coinsList]
    flag = 0
    while len(currList) == 1:
        group1, group2, group3 = splitCoins(currList[0])
        currList = findFakeGroup(group1, group2, group3)
        if len(currList[0]) == 1:
            fake = currList
            flag = 1
    if flag == 0:
        for i in range(2):
            while len(currList[i]) > 1:
                group1, group2, group3 = splitCoins(currList[i])
                currList[i] = findFakeGroup(group1, group2, group3)
        fake = currList
    
    print ('The fake coins is coin', coinsList.index(fake[0]) + 1, 'and', coinsList.index(fake[1]) + 1, 'in the original list')
    
#Pretend that you actually can't see the values in coinsList!
coinsList2 = [10, 10, 10, 10, 10, 10, 11, 10, 10]
coinsList = [10, 10, 10, 10, 10, 10, 11, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10]
coinsList_x = [10, 10, 10, 11, 10, 10, 11, 10, 10,
               10, 10, 10, 10, 10, 10, 10, 10, 10,
               10, 10, 10, 10, 10, 10, 10, 10, 10]

##coinComparison(coinsList2)
CoinComparison(coinsList_x)

