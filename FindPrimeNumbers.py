
#version1
n=20
#set is variable to store unqiue list
number_range = set(range(2,n+1))
prime_list = [] #empty list

prime = number_range.pop()
prime_list.append(prime)
multiples = set(range(prime*2,n+1,prime))

#difference_update removes the items exists in both sets number_range and multiples
number_range.difference_update(multiples)

#print(number_range)
#print(range(2,n+1))
#print("prime", prime)
#print("multiples",multiples)

#version2

#Upper bound
# n=20

# #number range to be checked
# number_range = set(range(2,n+1))

# #empty list to append discovered primes to
# prime_list = []
# while number_range:
# 	prime = number_range.pop()
# 	prime_list.append(prime)
# 	multiples = set(range(prime*2,n+1,prime))

# 	#difference_update removes the items exists in both sets number_range and multiples
# 	number_range.difference_update(multiples)
# #print out list of primes
# print(prime_list)

# #number of  primes that were found
# prime_count = len(prime_list)
# print("prime_count",prime_count)

# #largest prime
# largest_prime = max(prime_list)
# print("largest_prime",largest_prime)

# #summary
# print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")

#version3

def primes_finder(n):
	#number range to be check
	number_range = set(range(2,n+1))
	#empty list to append discovered primes to
	prime_list = []

	#while loop
	while number_range:
		prime = number_range.pop()
		prime_list.append(prime)
		multiples = set(range(prime*2,n+1,prime))

		#difference_update removes the items exists in both sets number_range and multiples
		number_range.difference_update(multiples)
	#print out list of primes
	print(prime_list)

	#number of  primes that were found
	prime_count = len(prime_list)
	print("prime_count",prime_count)

	#largest prime
	largest_prime = max(prime_list)
	print("largest_prime",largest_prime)

	#summary
	print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")
	return prime_list
primes_finder(100)
#print(prime_list)






