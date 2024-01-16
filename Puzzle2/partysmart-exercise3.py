# (開始時刻, 終了時刻, 好み)
sched3 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2), (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2), 
          (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4), (10.0, 11.0, 2), (10.0, 12.0, 3),(11.0, 12.0, 7)]

def bestTimeToPartySmart(schedule):

    times = []
    for c in schedule:
        times.append((c[0], c[2], 'start'))
        times.append((c[1], c[2], 'end'))

    #Sort the list of times.
    #Each time is a start or end time of a celebrity sighting.
    sortList(times)

    maxcount, time = chooseTime(times)

    #Output best time to party
    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxcount, 'celebrities will be attending!')


#Sort the elements of tlist in ascending order
#Sorting is based on the value of the first item of the element tuple
def sortList(tlist):
    for index in range(len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            #Sort based on first item of tuple
            if tlist[ismall][0] > tlist[i][0]:
                ismall = i
        #Swap the positions of the elements at index and ismall indices
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]
    
    return

def chooseTime(times):
    
    rcount = 0
    maxcount = 0
    time = 0
    
    #Range through the times computing a running count of celebrities
    for t in times:
        if t[2] == 'start':
            rcount = rcount + t[1]
        elif t[2] == 'end':
            rcount = rcount - t[1]
        if rcount > maxcount:
            maxcount = rcount
            time = t[0]
            
    return maxcount, time

bestTimeToPartySmart(sched3)