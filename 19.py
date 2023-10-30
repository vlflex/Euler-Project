from datetime import date, timedelta

def is_leap_year(year):
    if(year % 100 == 0):
        if(year % 400 == 0):
            return True
        else:
            return False
        
    if(year % 4 == 0):
        return True
    else:
        return False

def get_delta(date):
    if (date.month in [4, 6, 9, 11]):
        delta = timedelta(days = 30)
    elif (date.month == 2):
        if(is_leap_year(date.year)):
            delta = timedelta(days = 29)
        else:
            delta = timedelta(days = 28)
    else:
        delta = timedelta(days = 31)
    return delta


def main():
    start = date(1901, 1, 1)
    end = date(2000, 12, 31)
    current = start
    count = 0
    
    while(current < end):
        delta = get_delta(current)
        print(current, delta, sep = '\t')
        if(current.weekday() == 6):
            count += 1
        current += delta
    print(count)
    
if __name__ == '__main__':
    main()



 
