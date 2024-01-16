#Programming for the Puzzled -- Srini Devadas
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]

def encode(caps):
    #Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    #Determine intervals where caps are on in the same direction
    for i in range(len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i

    #Need to add the last interval after for loop completes execution
    intervals.append((start, len(caps) - 1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
 
    # print (intervals)
    # print (forward, backward)

    encode = ''
    for j in intervals:
        num_W = str(j[1] + 1 - j[0]) + j[2]
        encode += num_W

    print(encode)
    return encode

def decode(encode):
    num_change = ''
    decode = []
    for i in range(len(encode)):
        if encode[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num_change += encode[i]
        else:
            count = int(num_change)
            num_change = ''
            print(count)
            for j in range(count):
                decode += encode[i]
    print(decode)
    return decode

encode_caps = encode(caps)
decode(encode_caps)
