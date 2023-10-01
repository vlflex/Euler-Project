def is_pif_trio(a, b, c):
    a **= 2
    b **= 2
    c **= 2
    return (a + b == c) or (b + c == a) or (a + c == b)

def get_pif_trip(sum_):
    for c in range(1, sum_):
        for b in range(1, c):
            for a in range(1, b):
                if (is_pif_trio(a, b, c)) and (a + b + c == sum_):
                    return a, b, c

def main():
    try:
        a, b, c = get_pif_trip(1000)
        print(f'{a} * {b} * {c} = {a * b * c}')
    except:
        print('Тройка не найдена')

if __name__ == '__main__':
    main()