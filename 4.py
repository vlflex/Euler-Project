
def is_palidrom(num):
    digits = [int(dig) for dig in str(num)]
    middle = int(len(digits) / 2)
    
    if len(digits) == 1:
        return True
    elif (len(digits)) == 2 and (digits[0] == digits[1]):
        return True
    
    if len(digits) % 2 == 1:
        return digits[:middle] == (digits[middle+1:])[::-1]
    
    else:
        return digits[:middle] == (digits[middle:])[::-1]
    
def generate_nums():
    for i in range(100, 999 + 1):
        for j in range(100, 999 + 1):
            if  is_palidrom(i * j):
                yield i * j

def main():
    palidroms = list(generate_nums())
    print(max(palidroms))
        
if __name__ == '__main__':
    main()