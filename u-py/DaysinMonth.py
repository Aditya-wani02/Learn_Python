def is_leap(year):
    """tells you the year is leap year or not"""
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year , month):
    """Gives the days in the month in that year"""
    month_day=[31,28,31,30,31,30,31,31,30,31,30,31]
    a=is_leap(year)
    if a:
        if month == 2:
            no_day=29
        else:
            no_day=month_day[month-1]
        
    else:
        no_day=month_day[month-1]
    
    return no_day

year = int(input("enter year"))
month = int(input("enter month"))

days = days_in_month(year,month)
print(days)