def solution(my_string):
    return my_string.translate(str.maketrans('aeiou', '*****')).replace('*', '')
