
def service(take, dine, served):

    n = len(served)

    while n > 0:      
        if take[0] == served[0]:
            served.pop(0)
            take.pop(0)
        elif dine[0] == served[0]:
            served.pop(0)
            dine.pop(0)

    

    return served


print(service(take = [1, 3, 5], dine = [2, 6, 4], served = [1, 2, 4, 6, 5, 3]))


