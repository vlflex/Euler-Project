def is_right_num(num, lim = 20):
    for divider in range(1, lim + 1):
        if (num % divider) != 0:
            return False
    else:
        return True

def search_num(num = 20):
    while(not(is_right_num(num))):
        num += 20
    return num

#1, 2, 4, 5, 10, 20
#3, 7, 11, 13, 17, 19
def main():
    start_num = 20 * 3 * 7 * 11 * 13 * 17 * 19
    print(search_num(start_num))

if __name__ == '__main__':
    main()