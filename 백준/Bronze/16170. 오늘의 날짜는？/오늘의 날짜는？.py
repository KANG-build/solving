import datetime as dt

x = dt.datetime.now()
print(x.year)
if len(str(x.month)) == 1:
    print('0', end='')
print(x.month)
print(x.day)