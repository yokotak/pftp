#Programming for the Puzzled -- Srini Devadas
#Guess Who is Coming to Dinner
#Given a graph where vertices are friends and edges are dislikes relationships
#select a maximum number of friends such that no two friends dislike each other

#This procedure converts each number from 0 to 2^n - 1 into binary
#and uses the binary representation to determine the combination of guests
#and returns all possible combinations
def Combinations(n, guestList):
    allCombL = []
    for i in range(2**n):
        num = i
        cList = []
        for j in range(n): 
            if (num % 2 == 1):
                cList = [guestList[n-1-j]] + cList
            num = num // 2
        allCombL.append(cList)
    return allCombL

#This procedure checks the given combinations to see if the combination
#contains any pair of guests who dislike each other and removes the
#combination if that is the case
def removeBadCombinations(allCombL, dislikePairs):
    allGoodCombinations = []
    for i in allCombL:
        good = True
        for j in dislikePairs:
            #Check that each element of j is in i
            if j[0] in i and j[1] in i:
                good = False
        if good:
            allGoodCombinations.append(i)          
    return allGoodCombinations

def SerchDislikePairs(dislikePairs):
    red_list = []
    for d_list in dislikePairs:
        print("d_list:", d_list)
        if not d_list[0] in red_list:
            red_list.append(d_list[0])
        if not d_list[1] in red_list:
            red_list.append(d_list[1])
    print("red_list:", red_list)
    return red_list

def NoDislikeMembers(guestList, dislikePairs):
    red_list = SerchDislikePairs(dislikePairs)
    print('red_list:', red_list)
    use_list = []
    invite = []
    for i in guestList:
        if i in red_list:
            use_list.append(i)
        else:
            invite.append(i)
    return use_list, invite

#This procedure finds the combination with the maximum number of guests       
def InviteDinner(guestList, dislikePairs):
    use_list, invite = NoDislikeMembers(guestList,dislikePairs)
    print("use_list, invite:", use_list, invite)
    allCombL = Combinations(len(use_list), use_list)
    allGoodCombinations = removeBadCombinations(allCombL, dislikePairs)
    for i in allGoodCombinations:
        if len(i) > len(invite):
            invite.extend(i)
##    invite = max(allGoodCombinations, key=len)
    print ('Optimum Solution:', invite)


dislikePairs = [['Alice','Bob'],['Bob','Eve']]
guestList = ['Alice','Bob','Cleo','Don','Eve']
# print(Combinations(len(guestList), guestList))
InviteDinner(guestList, dislikePairs)

dislikePairs = [['Alice','Bob'],['Bob','Eve']]
guestList = ['Alice','Bob','Eve']
InviteDinner(guestList, dislikePairs)

LargeDislikes = [ ['B', 'C'], ['C', 'D'], ['D', 'E'],
                  ['F', 'G'], ['F', 'H'], ['F', 'I'], ['G', 'H'] ]
LargeGuestList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
InviteDinner(LargeGuestList, LargeDislikes)
