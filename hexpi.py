import timeit

def S(j, n):
    s = 0.0
    k = 0
    while k <= n:
        r = 8*k+j
        s = (s + pow(16, n-k, r) / r) % 1.0
        k += 1
    # Right sum
    t = 0.0
    k = n + 1
    while 1:
        newt = t + pow(16, n-k) / (8*k+j)
        if t == newt:
            break
        else:
            t = newt
        k += 1
    return s + t

def pi(n):
    n -= 1
    x = (4*S(1, n) - 2*S(4, n) - S(5, n) - S(6, n)) % 1.0
    return int(x * 16)

def hexpi(n):
    output = '3.'
    hexdigits = '0123456789abcdef'
    for i in range(1, n):
        output += hexdigits[pi(i)]
    return output

def pibin(n):
    if n % 4 == 0:
        return pi(n//4) // 8
    elif n % 4 == 1:
        return pi(n//4) // 4 % 2
    elif n % 4 == 2:
        return pi(n//4) // 2 % 2
    elif n % 4 == 3:
        return pi(n//4) % 2

def taubinstring(n):
    output = '110.'
    for i in range(5, n+2):
        output += str(pibin(i))
    return output
