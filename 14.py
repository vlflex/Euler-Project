class Kollatc:
    def __init__(self, start_num):
        self.__start_num = start_num
        self.__consistency = []
        
    def __generate_consistency(self):
        num = self.__start_num
        while(num != 1):
            yield num
            num = (num * 3 + 1) if (num % 2 == 1) else (num // 2)
        else:
            yield 1

    def get_consistency(self):
        return list(self.__generate_consistency())

    def __len__(self):
        return len(self.get_consistency())
    
def main():
    value = 0
    length = 0
    for num in range(2, 1_000_000):
        cosist = Kollatc(num)
        if(len(cosist) > length):
            length = len(cosist)
            value = num
    else:
        print(f'Наибольшое число {value} имеет последовательность, длиной: {len(Kollatc(value))}')
    
    
if __name__ == '__main__':
    main()