def is_prime_num(num):
    for divider in range(2, round(num ** 0.5) + 1):
        if num % divider == 0:
            return False
    else:
        return True
    
def get_prime_num(index):
    def prime_nums():
        num = 2
        i = 0
        while(i != index):
            if (is_prime_num(num)):
                i += 1
                yield num
            num += 1 if i < 7 else 2
            
    return list(prime_nums())[-1]
            
    
def main():
    print(get_prime_num(10001))
    
if __name__ == '__main__':
    main()