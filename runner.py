import Pollards_rho_trivial
import trial_division
import euler_trivial
import fermatfactor_trivial
import fermatfactor_improved_prime
import Pollards_rho_improved_prime


def main():
	print "integer factorization algorithm"
	print "type the number you want to run the algorithm"
	print "eg: 1"
	print "then will run the Trial division"
	print "1.Trial division"
	print "2.Euler's factorization method"
	print "3.Fermat's factorization method"
	print "4.Pollard's rho algorithm "
	number = input("input the number:")
	if number == 1:
		trial_division.runner()
	elif number == 2:
		euler_trivial.runner()
	elif number == 3:
		print "1.Trial prime generate"
		print "2.Miller Rabin Primality test"
		next = input("input the number")
		if next == 1:
			fermatfactor_trivial.runner()
		elif next == 2:
			fermatfactor_improved_prime.runner()
		else:
			print "wrong input"
	elif number == 4:	
		print "1.Trial prime generate"
		print "2.Miller Rabin Primality test"
		next = input("input the number")
		if next == 1:
			Pollards_rho_trivial.runner()
		elif next == 2:
			Pollards_rho_improved_prime.runner()	
		else:
			print "wrong input"
	else:
		print "wrong input"
main()

