from math import log, ceil

def find_prime_upper_limit(n):
    if n < 6:
        return 14
    return ceil(n * (log(n) + log(log(n))))

def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False

def nth_prime(n):
    prime_list = list(find_primes(find_prime_upper_limit(n)))
    return prime_list[n - 1]

print(nth_prime(10001))

#source: https://codereview.stackexchange.com/questions/188053/project-euler-problem-7-in-python-10001st-prime-number
#method used is basically identical to top comment as i did not know of the upper bound for the nth prime or the sieve of eratosthenes
