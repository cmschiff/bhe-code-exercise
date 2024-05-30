import numpy as np


class Sieve:
    def __init__(self, initial_size=10000000) -> None:
        # set default generated size of array for quick access
        self.SIZE = initial_size
        # generate initial primes array
        self._update_primes()

    def _update_primes(self):
        # set primes array attribute
        self.primes = self._generate_primes()
        # true size of the primes array (up to upper bound)
        self.primesHeld = len(self.primes)

    def _generate_primes(self):
        # Adjust for zero indexing
        curSize = self.SIZE + 1
        # Use Rosser's Theorem for the upper bound of the nth prime number
        # Pn = n(log(n) + log(log(n))) for n >= 6
        if curSize >= 6:
            upper_bound = int(curSize * (np.log(curSize) + np.log(np.log(curSize))))
        else:
            upper_bound = 13
        # Initialize a boolean array of size 'upper_bound' to track primes
        isPrime = np.ones(upper_bound, dtype=bool)
        # Set 0 and 1 to False (not primes)
        isPrime[0:2] = False
        # Eratosthenes step: iterate from 2 to sqrt(upper_bound) sqrt(upper_bound) because we will end up using i*i
        # (eventually i*i = upper_bound when i reaches the end of the range) so there's no reason to go beyond that
        for i in range(2, int(np.sqrt(upper_bound))):
            # If i is prime (True)
            if isPrime[i]:
                # Mark all multiples of i composite (False)
                isPrime[i * i: upper_bound: i] = False
        # Get indices of all True values in isPrime
        primes = np.flatnonzero(isPrime)
        # Return the primes array
        return primes

    def nth_prime(self, n: int) -> int:
        # If the n prime we're looking for is larger than how many we have
        if n >= self.primesHeld:
            # set new default size of array
            self.SIZE = n
            # regenerate primes array
            self._update_primes()
        # Return the nth prime
        return int(self.primes[n])
