def sum_of_squares(lim):
    return sum([num**2 for num in range(lim + 1)])

def square_of_sum(lim):
    return (sum(range(lim + 1))) ** 2

def main():
    print(abs(sum_of_squares(100) - square_of_sum(100)))

if __name__ == '__main__':
    main()