def a(k, n):
    k+=1         #4
    i=n          #2
    while i > 0: #3*(n+1)
        i-=1     #4*n

"""
n = 1 -> while condition:2;   loop body:1
n = 2 -> while condition:3;   loop body:2
n     -> while condition:n+1; loop body:n

sum = 4 + 2 + 3*(n+1) + 4*n = 9+7n
"""

def b(k,n):
    i=n          #2
    while i > 1: #3*(m+1)
        k+=1     #4*m
        i//=2    #4*m

"""
n = 2^m -> m = log2n

n = 1, m = 0 -> while condition:1;   loop body:0
n = 2, m = 1 -> while condition:2;   loop body:1
n = 4, m = 2 -> while condition:3;   loop body:2
n      m     -> while condition:m+1; loop body:m

sum = 2 + 3*(m+1) + 4*m + 4*m = 5+11m = 5+11(log2(n))
"""

def c(k,n):
    i=0             #2
    while i<n:      #3*(m+1)
        j=0         #2*m
        while j<n:  #3*m*(m+1)
            k+=1    #4*m*m
            j+=2    #4*m*m
        i+=2        #4*m

"""
n = 2*m -> m = n/2

n = 2, m = 1 -> while condition:2;    loop body:1
n = 4, m = 2 -> while condition:3;    loop body:2
n = 6, m = 3 -> while condition:4;    loop body:3
n    , m     -> while condition:(m+1);loop body:m

sum = 2 + 3*(m+1) + 2*m + 3*m*(m+1) + 4*m*m + 4*m*m + 4*m = 5+12*m+11*m^2 =  5+6n+11n^2/4
"""

def d(n,k):
    i=0                #2
    while i<n:         #3*(n+1)
        j=0            #2*n
        while j < i*i: #5*(0*0 + 1*1 + ... + (n-1)*(n-1)) ->  5*((n-1)*n*(2*n-1)/6 + n)
            k+=1       #4*((n-1)*n*(2*n-1)/6)
            j+=1       #4*((n-1)*n*(2*n-1)/6)
        i+=1           #4*n

"""
n = 1 ->while condition:2;    loop body:1
n = 2 ->while condition:3;    loop body:2
n = 3 ->while condition:4;    loop body:3
n     ->while condition:n+1;  loop body:n

i = 0  -> 0 
i = 1  -> 1  
i = 2  -> 4  
i = 3  -> 9 
i = 4  -> 16
i = n-1-> (n-1)^2


sum = 2 + 3*(n+1) + 2*n + 5*((n-1)*n*(2*n-1)/6 + n) + 4*((n-1)*n*(2*n-1)/6) + 4*((n-1)*n*(2*n-1)/6)+ 4*n = 5 + 26/6*n^3 - 39/6*n^2 + 97/6*n
"""

def e(k,n):
    i=1             #2
    while i<n:      #3*(m+1)
        j=1         #2*m
        while j<n:  #3*m(m+1)
            k+=1    #4*m*m
            j*=2    #4*m*m
        i*=2        #4*m

"""
n = 2^m -> m=log2(n)

n = 1, m = 0 -> while condition:1;    loop body:0
n = 2, m = 1 -> while condition:2;    loop body:1
n = 4, m = 2 -> while condition:3;    loop body:2
n    , m     -> while condition:m+1;  loop body:m

sum = 2 + 3*(m+1) + 2*m + 3*m(m+1) + 4*m*m + 4*m*m + 4*m = 5+12*m+11*m*m = 5+12*(log2(n))+11*(log2(n))^2
"""

def f(k,n):
    i=1             #2
    while i<n:      #3*(m+1)
        j=i         #2*m
        while j<n:  #3*(m(m+1)/2 + m)
            k+=1    #4*(m(m+1)/2)
            j*=2    #4*(m(m+1)/2)
        i*=2        #4*m

"""
n = 2^m -> m=log2(n)

n = 1, m = 0 -> while condition:1;    loop body:0
n = 2, m = 1 -> while condition:2;    loop body:1
n = 4, m = 2 -> while condition:3;    loop body:2
n    , m     -> while condition:m+1;  loop body:m

sum = 2 + 3*(m+1) + 2*m + 3*(m(m+1)/2 + m) + 4*(m(m+1)/2) + 4*(m(m+1)/2) + 4*m = 5 + 5*m + 3*((m^2+m)/2+m) + 
"""