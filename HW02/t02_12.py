from t02_10 import f
from t02_11 import g

def h(n):
    return f(n) + g(n) #O(n^2)
#O(n^2)

"""
Оптимізувати можна наступним чином:

def h(n):
    return (n*(n+1)*(n+8))/6 #O(1)
В цьому випадку асимптотична оцінка буде: O(1)    
"""