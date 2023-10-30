
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

