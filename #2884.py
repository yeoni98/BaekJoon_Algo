a, b = map(int, input().split())

m = int()
m = (60 + b) - 45

if b>= 45:
    print(a, b-45)
elif a == 0 and b<45:
    print(23, m)
else:
    print(a-1, m)