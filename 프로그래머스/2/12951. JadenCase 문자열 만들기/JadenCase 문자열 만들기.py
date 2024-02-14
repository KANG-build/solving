def solution(s):
    new = ''
    for i in s.split(' '):
        if i == '':
            new += ' '
        else:
            new += i[0].upper()
            new += i[1:].lower()
            new += ' '
    return new[:-1]