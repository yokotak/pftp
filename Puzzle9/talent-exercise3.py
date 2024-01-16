#Programming for the Puzzled -- Srini Devadas
#America Has Got Talent
#Given a group of candidates, each with a set of talents and
#given a list of talents that need to be displayed on the show
#choose a minimum number of candidates so they can display the entire
#list of talents on the show.

#Exercise 1: Dominated candidates are eliminated prior to starting the search.

#This procedure checks a given combination to see if the combination
#fails to cover any of the talents in AllTalents that need to be covered.
def Good(Comb, candList, candTalents, AllTalents):
    for tal in AllTalents:
        cover = False
        for cand in Comb:
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:
                cover = True
        if not cover:
            return False 
    return True

#Remove candidates whose talents are all covered by some other candidate
#It returns new candidate and new candidate to talent lists
def removeDominatedCandidates(cList, cTalents):
    newClist = []
    newTlist = []
    for i in range(len(cList)):
        dominated = False
        for j in range(len(cList)):
            if i == j:
                continue
            #Check if j dominates i, if so don't include i
            iTalent = cTalents[i]
            jTalent = cTalents[j]
            if contained(iTalent, jTalent):
                dominated = True
                print ('Candidate', cList[i], 'dominated by', cList[j])
        if not dominated:
            newClist.append(cList[i])
            newTlist.append(cTalents[i])

    return newClist, newTlist

#Check if each element of list1 is contained in list2
def contained(list1, list2):
    for elm in list1:
        if elm not in list2:
            return False
    return True

def SepareteOnlyTalentCand(candList, candTalents, talentList):
    only_clist = []
    only_tlist = []
    new_clist = []
    new_tlist = []
    for i in range(len(candList)):
        remain_talent = candTalents[i]
        for j in range(len(candList)):
            if i == j:
                continue
            j_talent = candTalents[j]
            remain_talent = contained_2(remain_talent, j_talent)
        if remain_talent == []:
            new_clist.append(candList[i])
            new_tlist.append(candTalents[i])
            continue
        only_clist.append(candList[i])
        only_tlist.append(candTalents[i])
        for k in candTalents[i]:
            if k in talentList:
                talentList.remove(k)
    return only_clist, only_tlist, new_clist, new_tlist, talentList

def contained_2(list1, list2):
    remain_talent = []
    for elm in list1:
        if elm not in list2:
            remain_talent.append(elm)
    return remain_talent

def weight(comb):
    return sum(c[1] for c in comb)
            
#This procedure finds the combination with the minimum number of candidates
#that cover all the required talents
def Hire4Show(candList, candTalents, talentList):
    candidates = candList
    # candList, candTalents = removeDominatedCandidates(candList, candTalents)
    # d_candList, d_candTalents, candList, candTalents, talentList = SepareteOnlyTalentCand(candList, candTalents, talentList)
    # print(d_candList, d_candTalents, candList, candTalents, talentList)
    n = len(candList)
    hire = candList[:]
    guarantee = sum([i[1] for i in candList])
    # print('guarantee:', guarantee)
    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n): 
            if (num % 2 == 1):
                Combination = [candList[n-1-j]] + Combination
            num = num // 2
        
        Combination_g = sum([i[1] for i in Combination])
        
        if Good(Combination, candList, candTalents, talentList):
            if guarantee > Combination_g:
                hire = Combination
                guarantee = Combination_g
                # print('Combination_g:', Combination_g)
    #並び替え
    # final_dicision = []
    # for i in candidates:
    #     if i in hire or i in d_candList:
    #         final_dicision.append(i)
    # print(candidates)
    # print(hire)
    # print(final_dicision)
    
    print ('Optimum Solution:', hire)
    print ('Weight is:', guarantee)

ShowTalentW = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateListW = [('A', 3), ('B', 2), ('C', 1), ('D', 4), ('E', 5), ('F', 2), ('G', 7)]
CandToTalentsW = [[1, 5], [1, 2, 8], [2, 3, 6, 9], [4, 6, 8], [2, 3, 9], [7, 8, 9],[1, 3, 5]]

Hire4Show(CandidateListW, CandToTalentsW, ShowTalentW)
