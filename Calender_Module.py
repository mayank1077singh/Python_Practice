import datetime
import calendar
X=input() 
def findDay(date):
    month, day, year = (int(i) for i in date.split(' '))    
    born = datetime.date(year, month, day)
    return born.strftime("%A")
print(findDay(X).upper())

