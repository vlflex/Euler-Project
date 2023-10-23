def get_triangle_num(n):
    if(n == 1):
        return 1
    else:
        return n + get_triangle_num(n - 1)
    
def get_dividers(num):
    for i in range(1, num + 1):
        if(num % i == 0):
            yield i
            
def get_dividers_count(num):
    return len(list(get_dividers(num)))
