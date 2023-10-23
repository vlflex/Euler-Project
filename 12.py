def get_triangle_num(n):
    if(n == 1):
        return 1
    else:
        return n + get_triangle_num(n - 1)
