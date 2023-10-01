#возвращает n-е число Фибаначчи
def fibonacci(n):
    if (n == 1) or (n == 0):
        return 1
    elif (n == 2):
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n - 2)
    
def filter_consistency(limit):
    condition = lambda x: (x % 2)
    index = 0
    
    while fibonacci(index) <= limit:
        num = fibonacci(index)
        if condition(num):
            yield num
        index += 1
        
    
    
def main():
    nums = list(filter_consistency(4_000_000))    
    print(sum(nums))
    
if __name__ == '__main__':
    main()