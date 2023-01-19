from math import floor

def choose_parameters_TransConv(input,output):
    kernel, stride, padding, dilatation = 0,0,0,0
    #dictionnaire de toutes les combinaisons possibles
    for k in range(1,5):
        for s in range(1,5):
            for p in range(0,3):
                for d in range(0,3):
                    if output == (input - 1) * s - 2* p + d*(k-1) + 1:
                        return k,s,p,d
    return 'no solution found'

def choose_parameters_Conv(input,output):
    kernel, stride, padding, dilatation = 0,0,0,0
    #dictionnaire de toutes les combinaisons possibles
    for k in range(3,6):
        for s in range(1,5):
            for p in range(0,3):
                for d in range(0,3):
                    if output == floor((input + 2*p - d*(k-1)-1)/s + 1 ) :
                        return k,s,p,d
    return 'no solution found'
