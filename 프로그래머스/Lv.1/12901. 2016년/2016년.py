import datetime

def solution(a, b):
    dt = datetime.datetime(2016, a, b)
    weekday = dt.weekday()
    return ["MON","TUE","WED","THU","FRI","SAT", "SUN"][weekday]