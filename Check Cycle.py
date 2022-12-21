def checkCycle ( arr ) :
    n, already_done = len(arr), set()
    #iterating over the array.
    for i in range(n):
        if i not in already_done:
            #maintaining this local set to check cycle.
            check_cycle = set()
            while True:
                #if element in local set retrun true because cycle exist.
                if i in check_cycle: 
                    return True
                #if already visited then break and continue.
                if i in already_done: 
                    break         
                already_done.add(i)
                check_cycle.add(i)
                #assigning the values to check cycle
                prev, i = i, (i + arr[i]) % n
                #this if condition is handling the condition of element pointing to itself
                if prev == i:
                    break
    return False