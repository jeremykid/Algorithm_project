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