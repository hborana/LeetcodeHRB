class Solution:
    # def closestPrimes(self, left: int, right: int) -> List[int]:
    def _sieve(self, upper_limit):
    # Create an integer list to mark prime numbers (True = prime, False = not prime)
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime

        for number in range(2, int(upper_limit**0.5) + 1):
            if sieve[number]:
                # Mark all multiples of 'number' as non-prime
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left, right):
        # Step 1: Get all prime numbers up to 'right' using sieve
        sieve_array = self._sieve(right)

        prime_numbers = [
            num for num in range(left, right + 1) if sieve_array[num]
        ]

        # Step 2: Find the closest prime pair
        if len(prime_numbers) < 2:
            return -1, -1  # Less than two primes

        min_difference = float("inf")
        closest_pair = (-1, -1)

        for index in range(1, len(prime_numbers)):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = prime_numbers[index - 1], prime_numbers[index]

        return closest_pair
        # def is_prime(n):
        #     if n < 2:
        #         return False
        #     if n in (2, 3):
        #         return True
        #     if n % 2 == 0 or n % 3 == 0:
        #         return False
            
        #     for i in range(5, int(n**0.5) + 1, 2):
        #         if n % i == 0:
        #             return False
        #     return True

        # primes = [num for num in range(left, right + 1) if is_prime(num)]

        # if len(primes) < 2:
        #     return [-1, -1]

        # min_diff = float('inf')
        # result = [-1, -1]

        # for i in range(len(primes) - 1):
        #     diff = primes[i + 1] - primes[i]
        #     if diff < min_diff:
        #         min_diff = diff
        #         result = [primes[i], primes[i + 1]]

        # return result
