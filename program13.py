
year = int(input("Year: "))

if (year%4==0 and year%100!=0)  or (year%400==0):
    print("%d is a leap year." % year)


# also you can check
    
import calendar
print(f"{calendar.isleap(year)}")