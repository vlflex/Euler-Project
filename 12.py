def get_triangle_num(n):
    return sum(range(1, n + 1))
    
def get_dividers(num):
    dividers = []
    for i in range(1, num + 1):
        if(num % i == 0):
            yield i
            
def get_dividers_count(num):
    return len(list(get_dividers(num)))



def main():
    # count = 0
    # i = 0
    # while(count <= 500):
    #     triangle_num = get_triangle_num(i)
    #     count = get_dividers_count(triangle_num)
    #     i += 1
        
    #     if(count == 20):
    #         print(triangle_num)
    #         break
        
    # else:
    #     print(triangle_num)
    
    print(get_dividers_count(999999999))
        
if __name__ == '__main__':
    main()
