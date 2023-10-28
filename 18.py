class TriangleNum:
    def __init__(self, nums):
        self.__nums_list = nums
        self.__value = []
        self.__extract_values()
        
    def __extract_values(self):
        temp_list = self.__nums_list
        size = 1
        while(temp_list):
            self.__value.append(temp_list[:size])
            del temp_list[:size]
            size += 1
            
    def get_values(self):
        return self.__value
    
    def __getitem__(self, index):
        return self.__value[index]
    
    def __len__(self):
        return len(self.__value)
    
    def __str__(self):
        STR_COEF = 3
        result = ''
        max_size = int(STR_COEF * len(self.__value[-1]))
        for row in self.__value:
            row = [str(num) for num in row]
            add_zero = lambda x: x if int(x) > 9 else f'0{x}'
            row = list(map(add_zero, row))
            result += f"{' '.join(row):^{max_size}}\n"
        return result
    
    def get_down_left(self, i, j):
        shift_left = lambda j: j if (j - 1 >= 0) else 0
        return self.__value[i+1][shift_left(j-1)]
    
    def get_down_right(self, i, j):
        shift_right = lambda j: j if (j + 1 > len(self.__value[i])) else len(self.__value[i]) - 1
        return self.__value[i+1][shift_right(j+1)]

