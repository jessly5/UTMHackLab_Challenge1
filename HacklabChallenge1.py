n = int(input("Enter integer > 0: "))
lst = []
for i in range (n):
    lst.append(i+1)
original = lst[:]
lst.reverse()

for i in range (0, n-1):
    for k in range (0, i+1):
        lst[k], lst[k+1] = lst[k+1], lst[k]
    print(lst)
    
for n in range (n-1, 0, -1):
    while lst[n] != original[n]:
        for k in range (0, n):
            lst[k], lst[k+1] = lst[k+1], lst[k]
        print(lst)
