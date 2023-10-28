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
            100:'hundred',
            1000:'thousand',
        }
        self.__init_digits()
        self.__init_str_value()
    
    def __init_digits(self):
        self.__digits = [int(dgt) for dgt in str(self.__value)]
    
    def __init_str_value(self):
        if (self.__value in self.__dict.keys()):
            self.__str = self.__dict[self.__value]
        
    def get_value(self):
        return self.__value
    
    def __getitem__(self, index):
        return self.__digits[index]
    
    def __str__(self):
        return self.__str
