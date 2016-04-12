import Miller_Rabin_primality_test


import math
import time

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

	if (Miller_Rabin_primality_test.is_probable_prime(factor)):
		prime_factors.extend(trial_division(factor))
	else:
		pollard(factor)
	another = number//factor
	if (Miller_Rabin_primality_test.is_probable_prime(another)):
		prime_factors.extend(trial_division(another))

	else:
		pollard(another)

def main():