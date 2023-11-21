class Num:
    def __init__(self, value):
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    
    @property
    def dividers(self):
        return list(self.__get_dividers())
    
    def __get_dividers(self):
        previous_i = 0
        for i in range(1, (self.__value // 2 + 1)):
            if(i * previous_i == self.__value):
                break
            
            if(self.__value % i == 0):
                yield i
                if(i != 1):
                    yield self.__value // i
                previous_i = i
    
    
def is_friend_nums(num1: Num, num2: Num) -> bool:
    if(num1.value == sum(num2.dividers) and num2.value == sum(num1.dividers)):
        return True
    else:
        return False
                
def main():
    from datetime import datetime
    print(f"Start: {datetime.now().strftime('%H:%M:%S')}")
    MAX_NUM: int = 10_000
    counter: int = 0
    for i in range(1, MAX_NUM):
        for j in range(int(i * 0.6), i):
            num1: Num = Num(i)
            num2: Num = Num(j)
            if(is_friend_nums(num1, num2)):
                counter += num1.value + num2.value
                print(counter)
                
    print(counter)
    print(f"End: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == '__main__':
    main()