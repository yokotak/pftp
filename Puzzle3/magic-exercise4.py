#Programming for the Puzzled -- Srini Devadas
#You Can Read Minds (With a Little Calibration)
#Five random cards are chosen and one of them is hidden.
#Given four cards in a particular order, you can figure out what the fifth card is!

#Exercise 1: Make sure 5 distinct cards are "randomly" generated.

#Deck is are a list of strings, each string is a card
#The order of cards in the list matters.
deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S', '3_C', '3_D', '3_H', '3_S',
        '4_C', '4_D', '4_H', '4_S', '5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S',
        '7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S', '9_C', '9_D', '9_H', '9_S',
        '10_C', '10_D', '10_H', '10_S', 'J_C', 'J_D', 'J_H', 'J_S',
        'Q_C', 'Q_D', 'Q_H', 'Q_S', 'K_C', 'K_D', 'K_H', 'K_S']


#This procedure figures out which card should be hidden based on the distance
#between the two cards that have the same suit.
#It returns the hidden card, the first exposed card, and the distance
def outputFirstCard(numbers, cards):
    encode = 13
    for ni in range(len(numbers)):
        for nj in range(len(numbers)):
            if ni == nj:
                continue
            n_encode = (numbers[ni] - numbers[nj]) % 13
            if n_encode < encode:
                encode = n_encode
                hidden = ni
                other = nj

##    #The following print statement is just for debugging!
##    print ('Hidden card is:', cards[hidden], 'and need to encode', encode)
    print ('First card is:', cards[other])

    return hidden, other, encode


#This procedure orders three cards depending on the number "code" that
#needs to be encoded. 
def outputNext3Cards(code, ind, f_b, cardsuit):
    
    if code == 0:
        second, third, fourth = ind[0], ind[1], f_b[0]
    elif code == 1:
        second, third, fourth = ind[0], ind[1], f_b[1]
    elif code == 2:
        second, third, fourth = ind[1], ind[0], f_b[0]       
    elif code == 3:
        second, third, fourth = ind[1], ind[2], f_b[1]

    if cardsuit == 0:
        s_lr = 'left'
        th_lr = 'left'
    elif cardsuit == 1:
        s_lr = 'left'
        th_lr = 'right'
    elif cardsuit == 2:
        s_lr = 'right'
        th_lr = 'left'
    elif cardsuit == 3:
        s_lr = 'right'
        th_lr = 'right'

    print ('Second card is:', deck[second], s_lr)
    print ('Third card is:', deck[third], s_lr)
    print ('all cards put ', fourth)

    
#Sorts elements in tlist in ascending order.
def sortList(tlist):
    for index in range(0, len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            if tlist[ismall] > tlist[i]:
                ismall = i
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]
    
    return


#This procedure is similar to AssistantOrdersCards() except it
#takes in a large number and "randomly" generates five cards.
def ComputerAssistant4Cards():
    f_b = ['front', 'back']
    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind, cnumbers = [], [], []
    numsuits = [0, 0, 0, 0]
    number = 0
    while number < 99999:
        number = int(input('Please give random number of at least 6 digits:'))


    #Generate five "random" numbers from the input number
    clist = []
    i = 0
    while len(clist) < 4:
        number = number * (i + 1) // (i + 2)
        n = number % 52
        i += 1
        if not n in clist:
            clist.append(n)

    print (clist)

    for i in range(4):
        n = clist[i]
        cards.append(deck[n])
        cind.append(n)
        # cardsuits.append(n % 4)
        cnumbers.append(n // 4)
        # numsuits[n % 4] += 1
        # if numsuits[n % 4] > 1:
        #     pairsuit = n % 4
            
##    #Just for debugging
    print ('cards: ', cards)
    print ('cind: ', cind)
    # print ('cardsuits: ', cardsuits)
    print ('cnumbers: ', cnumbers)
    # print ('pairsuit: ', pairsuit)

    hidden, other, encode = outputFirstCard(cnumbers, cards)

    cardsuit = other % 4
    remindices = []
    for i in range(4):
        if i != hidden and i != other:
            remindices.append(cind[i])

    sortList(remindices)
    outputNext3Cards(encode, remindices, f_b, cardsuit)

    guess = input('What is the hidden card?')
    if guess == cards[hidden]:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed!')

    return


ComputerAssistant4Cards()
