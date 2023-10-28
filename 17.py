class EngNum:
    def __init__(self, value):
        self.__value = value
        self.__str = ''
        self.__digits = []
        self.__dict = {
            1:'one',
            2:'two',
            3:'three',
            4:'four',
            5:'five',
            6:'six',
            7:'seven',
            8:'eight',
            9:'nine',
            10:'ten',
            11:'eleven',
            12:'twelve',
            15:'fifteen',
            20:'twenty',
            30:'thirty',
            40:'forty',
            50:'fifty',
            60:'sixty',
            70:'seventy',
            80:'eighty',
            90:'ninety',
            100:'hundred',
            1000:'one thousand',
        }
        self.__init_digits()
        self.__init_str_value()
    
    def __init_digits(self):
        self.__digits = [int(dgt) for dgt in str(self.__value)]
    
    def __init_str_value(self):
        if (self.__value in self.__dict.keys()):
            self.__str = self.__dict[self.__value]
        elif(11 < self.__value < 20):
            self.__str = f"{self.__dict[self[-1]]}teen"
        elif(20 < self.__value < 100):
            self.__str = f"{self.__dict[self[0] * 10]}-{self.__dict[self[-1]]}"
        elif(100 <= self.__value < 1000):
            temp_num = EngNum(self[-2] * 10 + self[-1])
            self.__str = f"{self.__dict[self[0]]} {self.__dict[100]} and {temp_num.__str__()}"
          
        
    def get_value(self):
        return self.__value
    
    def __getitem__(self, index):
        return self.__digits[index]
    
    def __str__(self):
        return self.__str
    
    def __len__(self):
        return len(self.__str)
    
def main():
    string = ''
    max_num = 1000
    for num in range(1, max_num + 1):
        eng = EngNum(num)
        string += eng.__str__().replace(' ', '').replace('-', '')
    print(f"кол-во: {len(string)}")
   
    
    
if __name__ == '__main__':
    main()