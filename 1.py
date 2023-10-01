def numbers_kr_3_5(count):
    return filter(lambda x: (x % 3 == 0) or (x % 5 == 0), range(1, count))
            
def main():
    right_nums = list(numbers_kr_3_5(1000))
    print(f'Ответ: {sum(right_nums)}')
    
if __name__ == '__main__':
    main()