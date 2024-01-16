#Programming for the Puzzled -- Srini Devadas
#America Has Got Talent
#Given a group of candidates, each with a set of talents and
#given a list of talents that need to be displayed on the show
#choose a minimum number of candidates so they can display the entire
#list of talents on the show


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

def smallestSol(chosen, elts, candList, candTalents, AllTalents, Sol):
    """
    Input: chosen is a (possibly empty) list of elements chosen so far.
           elts is a (possibly empty) list of elements yet to consider.
           dinnerCheck(chosen, x, dislikes) return True if it is OK to append x to chosen.
           Sol is list of all largest Sol found so far.
    Return list of all largest Sol found.
    """
    # print(elts)
    if len(elts) == 0:
        return Sol
    if Good(chosen + [elts[0]], candList, candTalents, AllTalents):
        if len(chosen + [elts[0]]) < len(Sol):
            Sol = chosen + [elts[0]]
        Sol = smallestSol(chosen[:-1], elts[1:], candList, candTalents, AllTalents, Sol)
    else:
        Sol = smallestSol(chosen + [elts[0]], elts[1:], candList, candTalents, AllTalents, Sol)
    return smallestSol(chosen, elts[1:], candList, candTalents, AllTalents, Sol)

#This procedure finds the combination with the minimum number of candidates
#that cover all the required talents by generating all the combinations
#one at a time.
def Hire4Show(candList, candTalents, talentList):
    hire = smallestSol([], candList, candList, candTalents, talentList, candList)
    print ('Optimum Solution:', hire)


Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalents = [ ['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'],
                  ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code'] ]

ShowTalent2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateList2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
CandToTalents2 = [ [4, 5, 7], [1, 2, 8], [2, 4, 6, 9], [3, 6, 9], [2, 3, 9],
                   [7, 8, 9], [1, 3, 7] ]

#Suppose one picked candidate C, we would get this problem to solve
ShowTalent3 = [1, 3, 5, 7, 8]
CandidateList3 = ['A', 'B', 'D', 'E', 'F', 'G']
CandToTalents3 = [ [5, 7], [1, 8], [3], [3],
                   [7, 8], [1, 3, 7] ]

#If one picked candidate G in the above problem, we would get this problem to solve
ShowTalent4 = [5, 8]
CandidateList4 = ['A', 'B', 'D', 'E', 'F']
CandToTalents4 = [ [5], [8], [], [], [8]]


Hire4Show(Candidates, CandidateTalents, Talents)
Hire4Show(CandidateList2, CandToTalents2, ShowTalent2)
Hire4Show(CandidateList3, CandToTalents3, ShowTalent3)
Hire4Show(CandidateList4, CandToTalents4, ShowTalent4)
