import sys
input = sys.stdin.readline

a = int(input())
deck = []
for i in range(a):
    s = input().strip()
    
    if s[:10] == 'push_front':
        deck.insert(0, int(s[11:]))
    elif s[:9] == 'push_back':
        deck.append(int(s[10:])) 

    elif s == 'pop_front':
        if len(deck):
            print(deck.pop(0))
        else: print(-1)
    elif s == 'pop_back':
        if len(deck):
            print(deck.pop(-1))
        else: print(-1)
        
    elif s == 'front':
        if len(deck):
            print(deck[0])
        else: print(-1)   
    elif s == 'back':
        if len(deck):
            print(deck[-1])
        else: print(-1)
        
    elif s == 'empty':
        if len(deck):
            print(0)
        else: print(1)
    elif s == 'size':
        print(len(deck))