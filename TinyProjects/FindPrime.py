import math


def find_prime_2(num):
    primes_bool = [False, False]+[True]*(num-1)
    for i in range(3, len(primes_bool)):
        if i & 1 == 0:
            primes_bool[i] = False
    for i in range(3, int(math.sqrt(num))+1):
        if primes_bool[i] is True:
            for j in range(i+j, num+1, i):
                primes_bool[j] = False
    primes = []
    [primes.append(i) for i, v in enumerate(primes_bool) if v is True]
    return primes


if __name__ == "__main__":
    print(find_prime_2(int(input("num:"))))
# to learn
