class Number:
    def __init__(self, value):
        self.__value = value
        self.__digits = []
        self.__get_digits()
        
    def __get_digits(self):
        self.__digits = [int(dgt) for dgt in str(self.__value)]
    
    def get_value(self):
        return self.__value
    
    def __getitem__(self, index):
        return self.__digits[index]
        
def main():
    num = Number(2**1000)
    print(sum(num[:]))
    
if __name__ == '__main__':
    main()