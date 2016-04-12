
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

def remove2(number):
    while (number == number//2*2):
        prime_factors.append(2)
        number = number//2
    return number

def fermat(number):
    number = remove2(number)
    a = math.ceil(math.sqrt(number))
    b = a*a - number
    while (int(math.sqrt(b))**2 != b):
        a = a+1
        b = a*a - number
    temp = a-int(math.sqrt(b))
    # prime_factors.append(temp)
    prime_factors.extend(trial_division(temp))
    prime_factors.extend(trial_division(number//temp))
    return

def runner():
    global prime_factors

    testcases = int(input("How many Testcases: "))
    for i in range(testcases):
        prime_factors = []
        timeA = time.time()
        number = int(input("number:"))
        # print find2sqrtroot(number)
        fermat(number)
        print prime_factors
        timeB = time.time()
        print (timeB - timeA)
