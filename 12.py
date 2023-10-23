def get_triangle_num(n):
    num = 0
    for i in range(1, n + 1):
        num += i
    return num
    
def get_dividers(num):
    for i in range(1, num + 1):
        if(num % i == 0):
            yield i
            
def get_dividers_count(num):
    return len(list(get_dividers(num)))
