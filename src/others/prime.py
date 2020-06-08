primes = [2]
print(2)
counter = 0
for n in range(3, 2**64 - 1):
	for prime in primes:
		counter += 1
		if n % prime == 0:
			break
	else:
		print(n)
		primes.append(n)	
