class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            if n < 2:
                return False
            if n in (2, 3):
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            for i in range(5, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        primes = [num for num in range(left, right + 1) if is_prime(num)]

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        result = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i], primes[i + 1]]

        return result
