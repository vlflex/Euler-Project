from functools import reduce

DATA = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
MULTIPLICATION = lambda x, y: x * y

class MatrixIndexException(Exception):
    def __init__(self, height, width, option):
        self.__height = height
        self.__width = width
        self.__option = option
        
    def __str__(self):
        if self.__option == 0:
            return f"MatrixIndexException: index can not be lower than zero"
        elif self.__option == 1:
            return f"MatrixIndexException: index i out of range i > {self.__height}"
        elif self.__option == 2:
            return f"MatrixIndexException: index j out of range j > {self.__width}"
        elif self.__option == 3:
            return f"MatrixIndexException: index i + nums out of range"
        elif self.__option == 4:
            return f"MatrixIndexException: index j + nums out of range"
        elif self.__option == 5:
            return f"MatrixIndexException: index i - nums out of range"
        

class Matrix:
    def __init__(self, height, width):
        self.__data = [[0] * width] * height
        self.__height = height
        self.__width = width
    
    def get_height(self):
        return self.__height
    
    def get_width(self):
        return self.__width
    
    def __check_exceptions(self, index_i, index_j, nums_count, horizontal = False, vertic = False, main_diagonal = False, side_diagonal = False):
        if index_i < 0 or index_j < 0:
            raise MatrixIndexException(self.__height, self.__width, 0)
        elif index_i >= self.__height:
            raise MatrixIndexException(self.__height, self.__width, 1)
        elif index_j >= self.__width:
            raise MatrixIndexException(self.__height, self.__width, 2)
        elif (index_i + nums_count > self.__height) and ((vertic) or (main_diagonal)):
            raise MatrixIndexException(self.__height, self.__width, 3)
        elif (index_j + nums_count > self.__width) and ((horizontal) or (main_diagonal) or (side_diagonal)):
            raise MatrixIndexException(self.__height, self.__width, 4)
        elif (index_i - nums_count < -1) and (side_diagonal):
            raise MatrixIndexException(self.__height, self.__width, 5)

    def vertic_mult(self, index_i, index_j, nums_count = 4):
        self.__check_exceptions(index_i, index_j, nums_count, vertic=True)

        extracted_nums = []
        j = index_j
        for i in range(index_i, index_i + nums_count):
            extracted_nums.append(self[i][j])
        return reduce(MULTIPLICATION, extracted_nums)
        
    def horizontal_mult(self, index_i, index_j, nums_count = 4):
        self.__check_exceptions(index_i, index_j, nums_count, horizontal=True)
        
        extracted_nums = []
        i = index_i
        for j in range(index_j, index_j + nums_count):
            extracted_nums.append(self[i][j])
        return reduce(MULTIPLICATION, extracted_nums)
    
    def main_diagonal_mult(self, index_i, index_j, nums_count = 4):
        self.__check_exceptions(index_i, index_j, nums_count, main_diagonal=True)
        
        extracted_nums = []
        for k in range(nums_count):
            i = index_i + k
            j = index_j + k
            extracted_nums.append(self[i][j])
        return reduce(MULTIPLICATION, extracted_nums)
        
    def side_diagonal_mult(self, index_i, index_j, nums_count = 4):
        self.__check_exceptions(index_i, index_j, nums_count, side_diagonal=True)
        
        extracted_nums = []
        for k in range(nums_count):
            i = index_i - k
            j = index_j + k
            extracted_nums.append(self[i][j])
        return reduce(MULTIPLICATION, extracted_nums)
    
    def __getitem__(self, index):
        return self.__data[index]
    
    def __setitem__(self, index, value):
        self.__data[index] = value
        
    def fill_with_list(self, nums_list):
        for i in range(self.__height):
            start = i * self.__width
            end = (i + 1) * self.__width
            self[i] = nums_list[start:end]

    def __str__(self):
        res = ''
        for i in range(self.__height):
            res += ' '.join([f'{str(num):<2}' for num in self[i]]) + '\n'
        return res
        
def get_nums(data):
    #преобразование чисел (из-за чисел, начинающихся с 0)
    def get_correct_num(num):
        try:
            return int(num)
        except:
            return int(num[1])
    
    data_list = data.split(' ')
    return [get_correct_num(num) for num in data_list]
    
def main():
    nums_list = get_nums(DATA)
    
    matrix = Matrix(20, 20)
    matrix.fill_with_list(nums_list)
    print(matrix)
    nums = 4
    
    try:
        #по горизонтали
        horizontal_mults = []
        for i in range(matrix.get_height()):
            i_coor = [i] * (matrix.get_width() - nums + 1)
            j_coor = list(range(matrix.get_width() - nums + 1))
            coordinates = list(zip(i_coor, j_coor))
            for coor in coordinates:
                horizontal_mults.append(matrix.horizontal_mult(*coor))

        #по вертикали
        vertic_mults = []
        for i in range(matrix.get_height() - nums + 1):
            i_coor = [i] * (matrix.get_width())
            j_coor = list(range(matrix.get_width()))
            coordinates = list(zip(i_coor, j_coor))
            for coor in coordinates:
                vertic_mults.append(matrix.vertic_mult(*coor))
        
        #по главной диагонали
        main_diagonal_mults = []
        for i in range(matrix.get_height() - nums + 1):
            i_coor = [i] * (matrix.get_width() - nums + 1)
            j_coor = list(range(matrix.get_width() - nums + 1))
            coordinates = list(zip(i_coor, j_coor))
            for coor in coordinates:
                main_diagonal_mults.append(matrix.main_diagonal_mult(*coor))
                
        #по побочной диагонали
        side_diagonal_mults = []
        for i in range(3, matrix.get_height() - nums + 1):
            i_coor = [i] * (matrix.get_width() - nums + 1)
            j_coor = list(range(matrix.get_width() - nums + 1))
            coordinates = list(zip(i_coor, j_coor))
            for coor in coordinates:
                side_diagonal_mults.append(matrix.side_diagonal_mult(*coor))
                
    except Exception as error:
        print(error)
        
    else:
        maximums = [
        max(horizontal_mults),
        max(vertic_mults),
        max(main_diagonal_mults),
        max(side_diagonal_mults),]
        print(max(maximums))
        
        
if __name__ == '__main__':
    main()
    

# side diagonal mult - копия main diagonal, ОБНОВИТЬ