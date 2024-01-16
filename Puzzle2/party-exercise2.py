#Programming for the Puzzled -- Srini Devadas
#yThe Best Time to Party
#Given a list of intervals when celebrities will be at the party
#Output is the time that you want to go the party when the maximum number of
#celebrities are still there.
#Brute force algorithm implemented here

sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]

def bestTimeToParty(schedule):
    st_list = listStartTime(schedule)
    cfs_time = compairTime(schedule, st_list)
    max_count, time = maxcountCulc(cfs_time)

    print ('Best time to attend the party is at', time,\
        'o\'clock', ':', max_count, 'celebrities will be attending!')


#開始時刻リスト化
def listStartTime(schedule):
    start_time_list = []
    for ci in schedule:
        s_check_flag = 0
        for si in start_time_list:
            if ci[0] == si:
                s_check_flag = 1
                break
        if s_check_flag != 1:
            start_time_list.append(ci[0])
    print(start_time_list)
    return start_time_list
        
#開始時刻と滞在時間の比較
def compairTime(schedule, start_time_list):
    count_for_start_time = []
    for si in start_time_list:
        c_count = 0
        for ci in schedule:
            if si >= ci[0] and si < ci[1]:
                c_count += 1
        count_for_start_time.append((si, c_count))
    return count_for_start_time

#最大値とその時刻の表示
def maxcountCulc(count_for_start_time):
    max_count = 0
    time = 0
    for ci in count_for_start_time:
        if ci[1] > max_count:
            max_count = ci[1]
            time = ci[0]
    
    return max_count, time

bestTimeToParty(sched)       