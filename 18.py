from itertools import product

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
    

def main():
    nums_list = [
75,
95, 64,
17, 47, 82,
18, 35, 87, 10,
20, 4, 82, 47, 65,
19, 1, 23, 75, 3, 34,
88, 2, 77, 73, 7, 63, 67,
99, 65, 4, 28, 6, 16, 70, 92,
41, 41, 26, 56, 83, 40, 80, 70, 33,
41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    num = TriangleNum(nums_list)
    print(num)
    
    combinations = list(product([0, 1], repeat = (len(num) - 1)))
    combinations_sum = []
    for comb in combinations:
        combinations_sum.append(get_triangle_sum(comb, num))
    print(max(combinations_sum))
    
if __name__ == '__main__':
    main()