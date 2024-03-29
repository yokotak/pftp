#Programming for the Puzzled -- Srini Devadas
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]

def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    for i in range(1,len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                start = i
            else:
                if i-1 != start:
                    print('People in positions', start, 'through', i-1, 'flip your caps!')
                else:
                    print('Person at position', i-1, 'flip your cap!')
                    
pleaseConformOnepass(caps)
pleaseConformOnepass(cap2)
