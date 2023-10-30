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
        def shift_left(j):
            return j
            
        j = shift_left(j)
        return (self.__value[i+1][j], i + 1, j)
    
    def get_down_right(self, i, j):
        def shift_right(j):
            return j + 1
           
        j = shift_right(j)
        return (self.__value[i+1][j], i + 1, j)

def get_triangle_sum(commands, triangle_num):
    i = j = 0
    sum_ = triangle_num[0][0]
    for option in commands:
        if(option):
            num, i, j = triangle_num.get_down_right(i, j)
        else:
            num, i, j = triangle_num.get_down_left(i, j)
        sum_ += num  
    else:
        return sum_
    
