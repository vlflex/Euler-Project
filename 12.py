def get_triangle_num(n):
    return sum(range(1, n + 1))
    

def get_dividers_count(num):
    dividers = []
    for i in range(1, (num // 2 + 1)):
        if(num % i == 0):
            dividers.append(i)
            if(len(dividers) > 2) and (dividers[-1] * dividers[-2] == num):
                return (len(dividers) - 1) * 2
    else:
        dividers.append(num)
                
    return len(dividers)
        


def main():
    count = 0
    i = 0
    while(count <= 500):
        triangle_num = get_triangle_num(i)   
        count = get_dividers_count(triangle_num)
        i += 1
               
    else:
        print(triangle_num)
    
    # print(get_dividers_count(999999999))
    # print(list(get_dividers(28)))
        
if __name__ == '__main__':
    main()
