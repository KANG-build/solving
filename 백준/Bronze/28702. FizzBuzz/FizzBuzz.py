첫째줄 = input()
둘째줄 = input()
셋째줄 = input()

if 첫째줄.isdigit():
    i = int(첫째줄) + 3
elif 둘째줄.isdigit():
    i = int(둘째줄) + 2
elif 셋째줄.isdigit():
    i = int(셋째줄) + 1
    
if i%3 == 0 and i%5 == 0:
    print("FizzBuzz")
elif i%3 == 0:
    print("Fizz")
elif i%5 == 0:
    print("Buzz")
else:
    print(i)
