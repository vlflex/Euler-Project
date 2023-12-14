class Num:
    def __init__(self, value):
        self.__value: int = value
        
    # получение значения числа
    @property
    def value(self):
        return self.__value
    
    # свойство для получения делителей
    @property
    def dividers(self):
        return list(self.__get_dividers())
    
    # генератор для получения делителей
    def __get_dividers(self):
        previous_i: int = 0
        for i in range(1, (self.__value // 2 + 1)):
            if(i * previous_i == self.__value):
                break
            
            if(self.__value % i == 0):
                yield i
                if(i != 1):
                    yield self.__value // i
                previous_i = i
