#Find the largest prime factor of a given number


def largest_prime_factor(n):
    prime_factors = []
    if n % 2 == 0:
        prime_factors.append(2)
    while n  % 2 == 0 :
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            prime_factors.append(i)
            n /= i

    if n > 2:
        prime_factors.append(n)

    return max(prime_factors)

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(largest_prime_factor(n))