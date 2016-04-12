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

def find2sqrtroot(number):
	largest = int(math.sqrt(number))
	result = []
	length = 0
	# print number,largest
	for i in range(largest//2+1):
		temp2 = number - i*i
		temp = int(math.sqrt(temp2))
		if (temp**2 == temp2):
			result.append(i)
			result.append(temp)
			length+=1
		if (length == 2):
			break
	return result

def euler(number):
	result = find2sqrtroot(number)
	# print (number)
	# print (result)
	if (len(result) != 4):
		# print (number)
		temp = trial_division(number)
		# print temp
		prime_factors.extend(temp)
		return
	else:
		b = result[0]
		a = result[1]
		d = result[2]
		c = result[3]
		k = gcd(a-c,d-b)
		h = gcd(a+c,d+b)
		l = (a-c)/k
		m = (d-b)/k
		# m = gcd(a+c,d-b)
		# l = gcd(a-c,d+b)
		factor1 = (k/2)**2 + (h/2)**2
		factor2 = l**2 + m**2
		# print (a,b,c,d)
		# print (l,m,k,h)
		# print factor1*factor2
		euler(factor1)
		euler(factor2)
 		

def main():
	global prime_factors

	testcases = int(input("Testcases"))
	for i in range(testcases):
		prime_factors = []
		timeA = time.time()
		number = int(input("number:"))
		# print find2sqrtroot(number)
		euler(number)
		print (prime_factors)
		timeB = time.time()
		print (timeB - timeA)
main()
