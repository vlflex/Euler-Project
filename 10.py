def is_prime_number(num):
    for divider in range(2, round(num ** 0.5) + 1):
        if num % divider == 0:
            return False
    else:
        return True

def prime_nums_generator(lim):
    num = 2
    while (num < lim):
        if is_prime_number(num):
            yield num
        num += 1 if num < 7 else 2

def main():
    limit = 2_000_000
    prime_nums = list(prime_nums_generator(limit))
    print(sum(prime_nums))
    

if __name__ == '__main__':
    main()