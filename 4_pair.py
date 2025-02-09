# cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
# returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b): def pair(f): return f(a, b) return pair 

# Implement car and cdr.

def cons(a ,b):
    return (a, b)

def car(pair):
    return pair[0] if(pair[0] < pair[1]) else pair[1] 

def cdr(pair):
    return pair[0] if(pair[0] > pair[1]) else pair[1] 

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
