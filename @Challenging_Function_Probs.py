
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


        
--------------------------------------------------

### Summer 69 ###
#Within such array, do not add 6 and 9 and numbers inbetween. If there is a 6, it always ends with a 9

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
    
#OR

def summer_69(arr):
    
    total = 0
    add = True
    
    for num in arr:
        if add:
            if num != 6:
                total += num
            else:
                add = False
        else:
            if num == 9:
                add = True
    return total
    
    
#The second way is better one since in professional people tend to use while loop for something they do not want to stop 
#until they get the outcome they want or til the condition is met and return some value or simply print something out. 
-----------------------------------------------

 def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
