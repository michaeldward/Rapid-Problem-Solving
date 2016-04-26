import numpy as np
def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def find_digital_root(x):
    x = str(x)
    trump = 0
    for y in str(x):
        trump = trump + int(y)
    return trump
arr=[];

def init():
    zero = [1, 1, 1, 1, 1, 1, 0]
    one = [0, 0, 0, 0, 1, 1, 0]
    two = [1, 0, 1, 1, 0, 1, 1]
    three = [1, 0, 0, 1, 1, 1, 1]
    four = [0, 1, 0, 0, 1, 1, 1]
    five = [1, 1, 0, 1, 1, 0, 1]
    six = [1, 1, 1, 1, 1, 0, 1]
    seven = [1, 1, 0, 0, 1, 1, 0]
    eight = [1, 1, 1, 1, 1, 1, 1]
    nine = [1, 1, 0, 0, 1, 1, 1]
    arr[0] = zero
    arr[1] = one
    arr[2] = two
    arr[3] = three
    arr[4] = four
    arr[5] = five
    arr[6] = six
    arr[7] = seven
    arr[8] = eight
    arr[9] = nine
    arr[10] = [0, 0, 0, 0, 0, 0, 0]

def pad(b,e):
    for i in range(len(b)-len(e)):
        e.insert(0, 0)
    return e

def find_max(b,e):
    s=0
    e=pad(b,e);
    for i in b:
        s += compare(arr[b[i]],arr[e[i]])
    return s
    

def find_sam(b):
    s=0
    for i in b:
        s += compare(arr[b[i]],arr[10])*2
    return s
def compare(a, b):
    s = 0
    for x in range(0, len(a)):
        if a[x] is not b[x]:
            s = s + 1
    return s



init();
