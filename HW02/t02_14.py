#--------a----------
def a(n):
    sum = 0                     #O(1)
    for i in range(1, n + 1):   #O(n)
        sum += i                #O(n)
    return sum                  #O(1)
#O(n)

#--------b----------
def b(n):
    sum = 0                     #O(1)
    for i in range(1, n + 1):   #O(n)
        sum += i*i              #O(n)
    return sum                  #O(1)
#O(n)

#--------c---------
def c(n, a):
    sum = 0                     #O(1)
    for i in range(1, n + 1):   #O(n)
        sum += a**i             #O(n)
    return sum                  #O(1)
#O(n)

#--------d---------
def d(n):
    sum = 0                     #O(1)
    for i in range(1, n + 1):   #O(n)
        power = 1               #O(n)
        for _ in range(i):      #O(n^2)
            power *= i          #O(n^2)
        sum += power            #O(n)
    return sum                  #O(1)
#O(n^2)

#---------e--------
def e(n):
    prod = 1                    #O(1)
    for i in range(1, n + 1):   #O(n)
        prod *= 1/(1 + i)       #O(n)
    return prod                 #O(1)
#O(n)
#--------f---------
def f(n):
    prod = 1                    #O(1)
    fact = 1                    #O(1)
    for i in range(1, n + 1):   #O(n)
        fact *= i               #O(n)
        prod *= 1/(1 + fact)    #O(n)
    return prod                 #O(1)
#O(n)

#---------g----------
def g(n, a):
    prod = 1                    #O(1)
    fact = 1                    #O(1)
    for i in range(1, n + 1):   #O(n)
        fact *= i               #O(n)
        prod *= a**i/(1 + fact) #O(n)
    return prod                 #O(1)
#O(n)

#----------h----------
def h(n,m):
    prod = 1                    #O(1)
    for i in range(1, n + 1):   #O(n)
        prod *= 1/(1 + i**m)     #O(nm)
    return prod                 #O(1)
#O(nm)

#----------i----------
def i(n):
    prod = 1                        #O(1)
    for i in range(1, n + 1):       #O(n)
        power = 1                   #O(n)
        for _ in range(1, i):       #O(n^2)
            power *= i              #O(n^2)
        prod *= 1 / (1 + power)     #O(n)
    return prod                     #O(1)
# O(n^2)