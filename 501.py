import time

def is_prime_number(num):
    for divider in range(2, round(num ** 0.5) + 1):
        if num % divider == 0:
            return False
    else:
        return True

def is_count_dividers(num, count):
    start = time.time()
    dividers = 1

      
    for i in range(1, (num // 2 + 1)):
        deltatime = time.time() - start
        
        if(dividers == 1) and (deltatime > 0.1):
            if(is_prime_number(num)):
                return False
        
        if(num % i == 0):
            dividers += 1
            
        if(dividers > count):
            return False
    
    if(dividers == 8):
        return True
    else:
        return False
        
       

def main():
    start = time.time()
    count = 0
    for num in range(10 ** 6 + 1):
        if(is_count_dividers(num, 8)):
            count += 1
    print(count)
    end = time.time() - start
    print(f'time: {end} sec')
        
if __name__ == '__main__':
    main()
