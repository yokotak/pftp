#Programming for the Puzzled -- Srini Devadas
#Tile that Courtyard, Please
#Given n in a 2^n x 2^n checkyard with a missing square at position (r, c), 
#find tiling of yard with trominoes (L-shaped dominoes)
#This exercise deals with 4 missing tiles and checks if
#3 of those form a tromino.


#This procedure checks if 3 of the four tiles can be tiled using a tromino
def tileFourMissingYard(n, missList):

    for t in missList:
        if t[0] < 0 or t[0] >= 2 ** n:
            return False
        if t[1] < 0 or t[1] >= 2 ** n:
            return False

    if len(missList) != 4:
        return False
    
    if checkQuad(2**n, missList):
        return True
    else:
        for i in range(len(missList)):
            tmpList = missList[:]

            #Remove this particular square
            remSquare = missList[i]
            tmpList.remove(remSquare)

            if checkTromino(tmpList):
                print (tmpList, 'forms a tromino')
                return True
            
        print (missList, 'squares do not form a tromino')
    return False

def checkTromino(tList):
    #There are four cases. In all four cases, the center square is (x, y).
    # (x, y-1), (x, y), (x+1, y)
    # (x-1, y), (x, y), (x, y+1)
    # (x, y+1), (x, y), (x+1, y)
    # (x-1, y), (x, y), (x, y-1)

    #Simply choose one of the squares in the list as the center
    #Create the other two squares and see if they match up!
    for i in range(len(tList)):
        center = tList[i]
        other1 = tList[(i + 1) % 3]
        other2 = tList[(i + 2) % 3]

        #First case
        create1 = (center[0], center[1]-1)
        create2 = (center[0]+1, center[1])
        if (create1 == other1 and create2 == other2) or\
           (create1 == other2 and create2 == other1):
            return True

        #Second case
        create1 = (center[0]-1, center[1])
        create2 = (center[0], center[1]+1)
        if (create1 == other1 and create2 == other2) or\
           (create1 == other2 and create2 == other1):
            return True

        #Third case
        create1 = (center[0], center[1]+1)
        create2 = (center[0]+1, center[1])
        if (create1 == other1 and create2 == other2) or\
           (create1 == other2 and create2 == other1):
            return True

        #Fourth case
        create1 = (center[0]-1, center[1])
        create2 = (center[0], center[1]-1)
        if (create1 == other1 and create2 == other2) or\
           (create1 == other2 and create2 == other1):
            return True

    return False

def checkQuad(size, missList):
    missquad_list = []
    for i in range(len(missList)):
        Miss = missList[i]
        rMiss = Miss[0]
        cMiss = Miss[1]
        count_0 = count_1 = 0
        while True:
            rMiss = rMiss//2
            count_0 += 1
            if rMiss == 0:
                break
        while True:
            cMiss = cMiss//2
            count_1 += 1
            if cMiss == 0:
                break
        missquad_list.append((count_0, count_1))
    # print (missquad_list)
    # print (set(missquad_list))
    if len(missquad_list) != len(set(missquad_list)):
        print("miss not separated.")
        return False
    
    print("all miss in other quad.")
    return True

tileFourMissingYard(3, [(4, 4), (1, 1), (2, 1), (1, 2)])
tileFourMissingYard(3, [(4, 4), (3, 1), (2, 1), (1, 2)])
tileFourMissingYard(3, [(3, 7), (4, 4), (4, 6), (4, 7)])
tileFourMissingYard(3, [(0, 1), (1, 0), (1, 1), (7, 7)])
tileFourMissingYard(3, [(0, 0), (7, 0), (0, 7), (7, 7)])