def is_prime_number(num):
    for divider in range(2, round(num ** 0.5) + 1):
        if num % divider == 0:
            return False
    else:
        return True

def generate_prime_nums(limit):
    for num in range(1, limit + 1):
        if (is_prime_number(num)):
            yield num

def get_prime_dividers(num):
    condition = lambda x: (num % x == 0)
    prime_list = list(generate_prime_nums(round(num ** 0.5)))
    return filter(condition, prime_list)
    

def main():
    NUM = 600851475143
    dividers_list = list(get_prime_dividers(NUM))
    print(dividers_list)
        
        
if __name__ == '__main__':
    main()