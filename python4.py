#1
##import random
##A = [random.randint(0, 5) for i in range(5)]
##n = int(input('Ne axtaririq: '))
##c = []
##for j in range(len(A)):
##    if A[j] == n:
##        c += [j]
##print(A)
##if len(c) == 0:
##    print('Tapilmadi')
##else:
##    print('Tapildi', end = ' ')
##    for m in c:
##        print(f'A[{m}] = {A[m]}', end = ' ')
#2
##A = list(map(int, input().split()))
##print(A)
##def cem(a):
##    s = 0
##    while a > 0:
##        s += a % 10
##        a //= 10
##    return s
##B = [cem(j) for j in A]
##for m in range(len(A) - 1):
##    for k in range(len(A) - m - 1):
##        if B[k] < B[k +1]:
##            B[k], B[k + 1] = B[k + 1], B[k]
##            A[k], A[k + 1] = A[k + 1], A[k]
##print(A)
#3
##L = [input()[2:] for i in range(5)]
##for j in range(len(L)):
##    i_min = j
##    for m in range(j + 1, (len(L))):
##        if L[m] < L[i_min]:
##            i_min = m
##    L[i_min], L[j] = L[j], L[i_min]
##print(L)
#4
##import random
##L = [input() for i in range(random.randint(1,20))]
##for j in range(len(L)):
##    i_min = j
##    for m in range(j + 1, (len(L))):
##        if L[m][4:] < L[i_min][4:]:
##            i_min = m
##    L[i_min], L[j] = L[j], L[i_min]
##print(L)
#5
##import random
##A = [random.randint(-100, 100) for i in range(10)]
##print(A)
##def bubblesort(a):
##    for m in range(len(a)):
##        for k in range(len(a) - m - 1):
##            if a[k] > a[k +1]:
##                a[k], a[k + 1] = a[k + 1], a[k]
##    return a
##    
##for m in range(len(A)):
##    for k in range(len(A) - m - 1):
##        if A[k] < A[k +1]:
##            A[k], A[k + 1] = A[k + 1], A[k]
##A[:len(A)//2], A[len(A)//2:] = bubblesort(A[:len(A)//2]), bubblesort(A[len(A)//2:])
##print(A)
#6
##import random
##A = [random.randint(-100, 100) for i in range(10)]
##print(A)
##def bubblesortar(a):
##    for m in range(len(a)):
##        for k in range(len(a) - m - 1):
##            if a[k] > a[k +1]:
##                a[k], a[k + 1] = a[k + 1], a[k]
##    return a
##def bubblesortaz(a):
##    for m in range(len(a)):
##        for k in range(len(a) - m - 1):
##            if a[k] < a[k +1]:
##                a[k], a[k + 1] = a[k + 1], a[k]
##    return a
##c = [x for x in A if x > 0]
##d = [s for s in A if s <= 0]
##print(bubblesortaz(c)+bubblesortar(d))
##print(f'Musbet elementlerin sayi: {len(c)}')
#8
import random
A = [random.randint(-100, 100) for i in range(10)]
print(A)
def bubblesort(a):
    for m in range(len(a)):
        for k in range(len(a) - m - 1):
            if a[k] > a[k +1]:
                a[k], a[k + 1] = a[k + 1], a[k]
    return a
print(bubblesort(A))
x = int(input('ededi daxil edin: '))
l = 0
for g in A:
    if x == g:
        l += 1
if l == 0:
    print('Tapilmadi')
else:
    print(f'{l} eded tapildi.')
