team_name = 'PACK'
strategy_name = 'Traitor'
strategy_description = 'Look at their history'


numOfBME = 0
numOfCME = 0

numOfCTHEM = 0
numOfBTHEM = 0


'''We look at history to decide whether or not to betray or collude'''
def move(my_history, their_history, my_score, their_score):
    global numOfBME, numOfCME, numOfCTHEM, numOfBTHEM
    
  
    for moves in my_history:
        if moves == 'b':
            numOfBME += 1
            
        else:
            numOfCME += 1
            
    else:    
        for moves in their_history:
            if moves == 'b':
                numOfBTHEM += 1
            
            else:
                numOfCTHEM += 1
                
    
    if numOfBME < 10:
        return 'b'
        
    elif len(their_history) > 0:
        percentCOfThem = (float(numOfCTHEM) /  float((len(their_history)))) * 100
        
        if percentCOfThem >= 80:
            return 'c'
            
        else:
            return 'b'
