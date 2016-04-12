integer factorization algorithm
======

| Algorithm        				| trivial prime           | Miller-Rabin primality test  |
| ----------------------------- |:-----------------------:| ----------------------------:|
| Trial division(baseline)      |trial_division.py 		  |note0 					 	 |
| Euler's factorization method  |euler_trivial.py         |note1						 |
| Fermat's factorization method |fermatfactor_trivial.py  |fermatfactor_improved_prime.py|
| Pollard's rho algorithm 		|Pollards_rho_trivial.py  |Pollards_rho_improved_prime.py|

* note0 : Trivial Division use the trivial prime, which cannot use Miller-Rabin primality test
* note1 : Euler's factorization method stop the algorithm 
		  when a number cannot found number = a^2 + b^2 = c^2 + d^2. 
		  Miller-Rabin is only judge the prime not find the factors.

