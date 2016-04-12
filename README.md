integer factorization algorithm
======
1 Introduction
------
| Algorithm        				| trivial prime           | Miller-Rabin primality test  |
| ----------------------------- |:-----------------------:| ----------------------------:|
| Trial division(baseline)      |trial_division.py 		  |note0 					 	 |
| Euler's factorization method  |euler_trivial.py note2   |note1						 |
| Fermat's factorization method |fermatfactor_trivial.py  |fermatfactor_improved_prime.py|
| Pollard's rho algorithm 		|Pollards_rho_trivial.py  |Pollards_rho_improved_prime.py|note3

* note0 : Trivial Division use the trivial prime, which cannot use Miller-Rabin primality test
* note1 : Euler's factorization method stops the algorithm
		  when a number cannot found number = a^2 + b^2 = c^2 + d^2. 
		  Miller-Rabin is only judge the prime not find the factors.
* note2 : Since I have not find a better way to find a number = a^2 + b^2 = c^2 + d^2. 
		  So Euler's spend on the this function I will list after that 
* note3 : In Pollards_rho Miller-Rabin primality test there is some special case will have 	
		  RuntimeError: maximum recursion depth exceeded


#Integer factorization:

### 1.1
Trial division: (Baseline)
This is a base line in my integer factorization algorithm project. It is using 
a prime sieve for prime number generation which can judge a number is a prime or 
continue do factorization.

Running time: in the worst case it is O(2^(n/2)/((n/2)*ln2)) 
* n is base-2 n digit number.

### 1.2
Euler's factorization method:
This is an implementation factorization algorithm, which solves the following problem. Given an number, then find all prime factors. The base knowledge of Euler's factorization is if 
a number = a^2 + b^2 = c^2 + d^2. There is a quickly way to seperate into 2 factors.

Running time: It is very slow, worst case is greater than trial division,
only quick in some special cases and has potient quick.

### 1.3
Fermat's factorization method:
This is an implementation factorization algorithm, which solves the following problem. Given an number, then find all prime factors. The base knowledge of Fermat's factorization method:
 is if a number = a^2 - b^2 There is a quickly way to seperate into 2 factors.

Running time: Worst case is O(N^{1/2})  
			  General case is O(N^{1/3}) time.

### 1.4
Pollard's rho algorithm:
This is an implementation factorization algorithm, which solves the following problem. Given an number, then find all prime factors. The base knowledge of Pollard's rho algorithm is if a find 
the abs(x^2+1-x) mod N if not 1 then it is a factor of N.

Running time: General case by the Birthday paradox in O(\sqrt p)\ <= O(n^{1/4})
			  but this is a heuristic claim, and rigorous analysis of the algorithm remains open.

2 Experiment Result
------
# 1 St: 2 primes product each prime > million
###1.1
The testcases: 15485867*32452867 = 502560782130689

| Algorithm        				| trivial prime           | Miller-Rabin primality test  |
| ----------------------------- |:-----------------------:| ----------------------------:|
| Trial division(baseline)      |31.0308229923 		  	  |null 					 	 |
| Euler's factorization method  |32.3473279476+3.276534002|null							 |
| Fermat's factorization method |2.5645339489  			  |3.19916701317 				 |
| Pollard's rho algorithm 		|0.0414018630981          |0.0358607769012 				 |

###1.2
The testcases: 15487019*15487469 = 239854726664911

| Algorithm        				| trivial prime           | Miller-Rabin primality test  |
| ----------------------------- |:-----------------------:| ----------------------------:|
| Trial division(baseline)      |22.700715065 		  	  |null 					 	 |
| Euler's factorization method  |21.358424902+3.0871624554|null							 |
| Fermat's factorization method |3.99884200096  		  |2.206387043					 |
| Pollard's rho algorithm 		|0.0165410041809          |0.0110921859741 				 |

# 2 nd: 4 primes product each prime between[1000,9999]

###2.1
The testcases: 8147*8369*8623*7127 = 4190216175859403

| Algorithm        				| trivial prime           | Miller-Rabin primality test  |
| ----------------------------- |:-----------------------:| ----------------------------:|
| Trial division(baseline)      |109.196480989 		  	  |null 					 	 |
| Euler's factorization method  |105.0888099666+5.89233399|null							 |
| Fermat's factorization method |2.5645339489  			  |3.19916701317 				 |
| Pollard's rho algorithm 		|0.0414018630981          |0.0358607769012 				 |

###2.2
The testcases: 1259*1451*1613*1811 = 5336370322687

| Algorithm        				| trivial prime           | Miller-Rabin primality test  |
| ----------------------------- |:-----------------------:| ----------------------------:|
| Trial division(baseline)      |2.96865296364 		  	  |null 					 	 |
| Euler's factorization method  |3.3992729187+0.5768110752|null							 |
| Fermat's factorization method |5.54617881775  	      |3.116948843 				 	 |
| Pollard's rho algorithm 		|0.00448799133301         |0.00167012214661 		 	 |

# 3 rd: over 6 small prime product

###3.1
The testcases: 13*127*263*419*17*131*269 = 108990674873561

| Algorithm        				| trivial prime           | Miller-Rabin primality test  |
| ----------------------------- |:-----------------------:| ----------------------------:|
| Trial division(baseline)      |12.9187300205 		  	  |null 					 	 |
| Euler's factorization method  |12.9247641563+2.445067882|null							 |
| Fermat's factorization method |3.29201412201  		  |2.98240017891 				 |
| Pollard's rho algorithm 		|0.00494313240051         |0.00559782981873 			 |

###3.2
The testcases: 13*17*2*1123*1426499*5 = 3540328013170

| Algorithm        				| trivial prime           | Miller-Rabin primality test  |
| ----------------------------- |:-----------------------:| ----------------------------:|
| Trial division(baseline)      |4.11624193192 		  	  |null 					 	 |
| Euler's factorization method  |4.38335967064+0.452334165|null							 |
| Fermat's factorization method |3.39200806618 		  	  |2.18938994408 				 |
| Pollard's rho algorithm 		|0.00471496582031         |0.00225687026978		 		 |

3 How to run the code:
------
There is a easy way to run by 
```python runner.py```
Then following the introduction. 

Or 

You can runner each single file
which has been listed:

| Algorithm        				| trivial prime           | Miller-Rabin primality test  |
| ----------------------------- |:-----------------------:| ----------------------------:|
| Trial division(baseline)      |trial_division.py 		  |note0 					 	 |
| Euler's factorization method  |euler_trivial.py note2   |note1						 |
| Fermat's factorization method |fermatfactor_trivial.py  |fermatfactor_improved_prime.py|
| Pollard's rho algorithm 		|Pollards_rho_trivial.py  |Pollards_rho_improved_prime.py|

Reference
------
http://www.bigprimes.net/archive/prime/10/
https://rosettacode.org/wiki/Miller–Rabin_primality_test#Python:_Probably_correct_answers
https://en.wikipedia.org/wiki/Integer_factorization
https://en.wikipedia.org/wiki/Trial_division
https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
https://en.wikipedia.org/wiki/Euler%27s_factorization_method
http://mathworld.wolfram.com/PollardRhoFactorizationMethod.html
http://kadinumberprops.blogspot.ca/2012/11/fermats-factorization-running-time.html
