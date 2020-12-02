# The datetime module is actually an abstract base class, which is kind of a fancy
# way of saying it offers new data types to the language. 
# When specifying the month or day, never use a leading zero for datetime.date().


#Import the datetime module give it an alias of dt.
import datetime as dt
#put today's date in today variable.
today = dt.date.today()
#Put another date in last_of_teens
last_of_teens = dt.date(2019, 9, 19)

#See what's in each variable
print(today)
print(last_of_teens)

print(last_of_teens.month)
print(last_of_teens.year)
print(last_of_teens.day)



# %a     Weekday, abbreviated                       Sun
# %A     Weekday, full                              Sunday
# %w     Weekday number 0-6, where 0 is Sunday      0
# %d     Number day of the month                    01-31 31
# %b     Month name abbreviated                     Jan
# %B     Month name full                            January
# %m     Month number                               01-12 01
# %y     Year without century                       19
# %Y     Year with century                          2019
# %H     Hour                                       00-23 23
# %I     Hour                                       00-12 11
# %p     AM/PM                                      PM
# %M     Minute                                     00-59 01
# %S     Second                                     00-59 01
# %f     Microsecond 000000-999999                  495846
# %z     UTC offset                                 -0500
# %Z     Time zone                                  EST
# %j     Day number of year 001-366                 300
# %U     Week number of year, Sunday as the first day of week, 00-53        50
# %W     Week number of year, Monday as the first day of week, 00-53        50
# %c     Local version of date and time             Tue Dec 31 23:59:59 2018
# %x     Local version of date                      12/31/18
# %X     Local version of time                      23:59:59
# %% A % character                                    %
print(f"{last_of_teens:%A, %B %d, %Y}")
todays_date = f"{today:%m/%d/%Y}"
print(todays_date)
# BirthDay
today = dt.date.today()
birthday = dt.date(1975, 1, 1)
delta_age = (today - birthday)
print(delta_age)
days_old = delta_age.days
print(days_old, type(days_old))


