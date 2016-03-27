import math
import time

def primeGenerate(number):
	largest = number
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
	# print (prime_list,number)
	for i in range(0,number):

		if(prime_list[i] == 1):
			result.append(i)

	return result

def trial_division(n):
    """Return a list of the prime factors for a natural number."""
    if n < 2:
        return []
    prime_factors = []
    for p in primeGenerate(int(n**0.5) + 1):
        if p*p > n: 
        	break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def main():
	testcases = int(input("Testcases"))
	for i in range(testcases):
		timeA = time.time()
		number = int(input("number:"))
		print trial_division(number)
		timeB = time.time()
		print (timeB - timeA)
main()
