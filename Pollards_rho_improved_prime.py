import Miller_Rabin_primality_test


import math
import time

def primeGenerate(number):
    largest = number
    # largest = int(math.sqrt(number)+1)
    prime_list = largest*[1]
    if (number<4):
        return [2,3]
    prime_list[1] = 0
    for i in range(0,largest,2):
        prime_list[i] = 0
    
    prime_list[2] = 1
    for i in range(3,largest,2):
        if (prime_list[i] == 1):
            for j in range(2*i,largest,i):
                prime_list[j] == 1
            
    result = []
    for i in range(0,number):
        if(prime_list[i] == 1):
            result.append(i)

    return result

def trial_division(n):
    """Return a list of the prime factors for a natural number."""
    if n < 2:
        return []
    prime_factors_list = []
    temp = primeGenerate(int(n**0.5) + 1)

    for p in temp:
        if p*p > n: 
            break
        while n % p == 0:
            prime_factors_list.append(p)
            n //= p
    if n > 1:
        prime_factors_list.append(n)
    return prime_factors_list

def gcd(a,b):
    while (b != 0):
        temp = a%b
        a = b
        b = temp
    return a

def pollard(number):
    if (number == 1):
        # print prime_factors
        return 1
    x_fixed = 2
    cycle_size = 2
    x = 2
    factor = 1;
    while (factor == 1):
        count = 1
        while (count <= cycle_size and factor <= 1):
            count += 1
            x = (x*x+1)%number
            factor = gcd(x-x_fixed, number)
        cycle_size *= 2
        x_fixed = x
    if (factor == number):
        prime_factors.extend(trial_division(factor))
    elif (factor <= 3):
        prime_factors.append(factor)
    elif (Miller_Rabin_primality_test.is_probable_prime(factor)):
        prime_factors.append(factor)
    else:
        pollard(factor)
    another = number//factor
    if (another == number):
        prime_factors.extend(trial_division(another))
    elif (another <= 3):
        prime_factors.append(another)
    elif (Miller_Rabin_primality_test.is_probable_prime(another)):
        prime_factors.append(another)
    else:
        pollard(another)


def runner():
    testcases = int(input("How many Testcases: "))
    for i in range(testcases):
        number = int(input("Number : "))
        global prime_factors
        timeA = time.time()
        prime_factors = []
        pollard(number)
        print prime_factors
        timeB = time.time()
        print (timeB - timeA)

