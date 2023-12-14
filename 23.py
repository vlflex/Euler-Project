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
                
    # булевое свойство "число - совершенное"
    @property
    def is_perfect(self) -> bool:
        return self.value == sum(self.dividers)
    
    # булевое свойство "число - избыточное"
    @property
    def is_excess(self) -> bool:
        return self.value < sum(self.dividers)
    
    # булевое свойство "число можно быть записано
    # как сумма двух избыточных чисел"
    @property 
    def is_excess_sum(self) -> bool:
        # число - чётное и его можно представить 
        # как сумма двух (равных) избыточных чисел
        LOWERST_EXCESS = 12
        if(self.value % 2 == 0) and (Num(self.value//2).is_excess):
            return True
        # обычный поиск подходящих слагаемых
        else:
            for num1 in range(LOWERST_EXCESS, self.value // 2):
                num2: int = self.value - num1
                if(Num(num1).is_excess and Num(num2).is_excess):
                    return True
        return False
