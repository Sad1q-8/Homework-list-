#1
##Tuple = (4, 6, 3, 9, 12, 24, 24, 76, 63)
##s = 0
##print('24 ededinin indeksi: ', end = ' ')
##for i in Tuple:
##    if i == 24:
##        print(s, end = ' ')
##    s += 1
#2
##Tuple = (4, 6, 3, 9, 12, 24, 24, 76, 63)
##print('3-e bolunen ededler:', end = ' ')
##for i in Tuple:
##    if i % 3 == 0:
##        print(i, end = ' ')
#3
##List1 = [ int(input()) for i in range(5) ]
##List2 = []
##for j in List1:
##    List2 = List2 + [j + 5]
##print(f'List1 = {List1}\nList2 = {List2}')
#4
##List1 = [ int(input()) for i in range(5) ]
##List2 = []
##for j in List1:
##    if j % 2 == 1:
##        List2 = List2 + [j]
##print(f'List1 = {List1}\nList2 = {List2}')
#5
##import random
##List = [ random.randint(0,10) for i in range(7) ]
##maxi = 0
##mini = 0
##max = List[0]
##min = List[0]
##say = 0
##cem = 0
##hasil = 1
##for j in List:
##    cem += j
##    hasil *= j
##    if j > max:
##        max = j
##        maxi = say
##    elif j < min:
##        min = j
##        mini = say
##    say += 1
##print(f'List = {List}\nCem = {cem} Hasil = {hasil} Ededi orta = {cem / say}\nEn boyuk eded = {max} , indeks = {maxi}\nEn kicik eded = {min} , indeks = {mini}')
#6
##import random
##list = [ random.randint(0,100) for i in range(10) ]
##kics = 0
##kicc = 0
##boyc = 0
##for j in list:
##    if j < 50:
##        kics += 1
##        kicc += j
##    else:
##        boyc += j
##print(f'{list}\n[0, 50) araliginda ededi orta = {kicc / kics}\n[50, 100] araliginda ededi orta = {boyc / (10 - kics)}')
#7 ve 8
##List = [ i**2 for i in range(1,16) ]
##ilk5 = []
##son5 = []
##s = 0
##print(f'List = {List}')
##print('Ilk 5 element =', end = ' ')
##while s < 15:
##    while s < 5:
##        print(List[s], end = ' ')
##        s += 1
##    if s > 9:
##        print()
##        print('Son 5 element =', end = ' ')
##        while s > 9 and s < 15:
##            print(List[s], end = ' ')
##            s += 1
##    s += 1
#9
##List1 = list(map(int,input().split()))
##List2 = list(map(int,input().split()))
##def ort(list1,list2):
##    for i in list1:
##        for j in list2:
##            if j == i:
##                return True
##    return False
##if ort(List1,List2):
##    print(f'List1 = {List1} List2 = {List2} Cavab: ortaq element var.')
##else:
##    print(f'List1 = {List1} List2 = {List2} Cavab: ortaq element yoxdur.')
#10
##List1 = [11, 22, 33, 44, 55]
##List2 = [12, 23, 33, 45, 55]
##print(f'List1 = {List1}\nList2 = {List2}')
##print('Tekrarlanan elementler:', end = ' ')
##s = 0
##k = 0
##for i in List1:
##    if List2[s] == List1[s]:
##        print(List1[s],end = ' ')
##        k += 1
##    s += 1
##print()
##print(f'Eyni indeksde yerleshen eyni elementlerin sayi = {k}')
#11
##List1 = list(map(int,input().split()))
##List2 = []
##s = True
##for i in List1:
##    if s:
##        s = False
##        continue
##    else:
##        List2 += [i]
##List2 += [List1[0]]
##print(f'List1 = {List1}    List2 = {List2}')
#12
##List1 = ['A', 'B', 'C']
##List2 = [1, 2, 3]
##List3 = []
##s = 0
##print(f'List1 = {List1}\nList2 = {List2}')
##for i in List1:
##    List3 += [[List1[s], List2[s]]]
##    s += 1
##print(f'Yeni_list = {List3}')
#13
##List = list(map(int,input().split()))
##s = 0
##for i in List:
##    if i % 2 ==0:
##        break
##    s += i
##print(f'List = {List}\nListin ilk cut ededine qeder olan cem: {s}')
#14
##import random
##List1 = [ random.randint(10,50) for i in range(int(input('Listin olcusu N: '))) ]
##def kv(a):
##    s = 1
##    while s <= a:
##        if s**2 == a:
##            return True
##        s += 1
##    return False
##List2 = []
##for j in List1:
##    if kv(j):
##        List2 += [j]
##print(f'List1 = {List1}\nList2 = {List2}')
#15
##import random
##List1 = [ random.randint(100,999) for i in range(int(input('Ededlerin sayi N: '))) ]
##def cem(a):
##    if (a%10 - a//10%10)%2 == 1 and (a%10 + a//10%10)%2 == 1:
##        return True
##    return False
##List2 = []
##for j in List1:
##    if cem(j):
##        List2 += [j]
##print(f'List1 = {List1}\nList2 = {List2}')
#16
##import random
##A = [ random.randint(0,100) for i in range(int(input('Ededlerin sayi N: '))) ]
##B = []
##def sade(a):
##    for j in range(2, a//2+1):
##        if a % j == 0:
##            return False
##    return True
##for m in A:
##    if sade(m):
##        B += [m]
##print(f'A = {A}\nB = {B}')
#17
##import random
##A = [ random.randint(-10, 10) for i in range(10) ]
##B = []
##for j in A:
##    if j % 2 == 0 and j < 0:
##        B += [j]
##print(f'A = {A}\nB = {B}')
#18
##List1 = [1, 2, 'aaaf', '1', '123', 123]
##List2 = []
##for i in List1:
##    if type(i) == int and i >=0:
##        List2 += [i]
##print(f'List1 = {List1}\nList2 = {List2}')
#19
##a = int(input('Musbet tam eded: '))
##List = []
##for i in range(1,a + 1):
##    if a % i == 0:
##        List += [i]
##print(f'List = {List}')
#20
##import math
##N = list(map(int, input().split()))
##List = []
##for i in N:
##    s = 0
##    for j in range(1, i + 1):
##        s += (4 * math.sin(j) + 2 * j)/(math.log(9 * j, 3) * 2 ** j)
##    List += [s]
##print(f'N = {N}\nList = {List}')
#21
##import math
##N = list(map(int, input().split()))
##List = []
##for i in N:
##    s = 0
##    for j in range(i + 1):
##        s += ((math.cos(j**2 + 1) ** j) ** j)/(math.log(8, 3) * (j + j ** 2) ** j)
##    List += [s]
##print(f'N = {N}\nList = {List}')
#22
##import random
##A = [ random.randint(-100, 100) for i in range(8) ]
##mu = []
##me = []
##k = 0
##for j in A:
##    if j > 0:
##        mu += [j]
##        k += 1
##    else:
##        me += [j]
##print(f'A = {A}\nB = {mu + me}\nMusbet edelerin sayi: {k}')
#23
##import random
##List1 = [ random.randint(0, 100) for i in range(10) ]
##List2 = []
##def fibonacci(a):
##    b = 1
##    c = 1
##    if a == 1 or a == 2:
##        return True
##    while c < a:
##        b, c = c, b + c
##        if c == a:
##            return True
##    return False
##for j in List1:
##    if fibonacci(j):
##        List2 += [j]
##print(f'List1 = {List1}\nList2 = {List2}')
#26
##A = list(map(int, input().split()))
##def my_max(a):
##    max = a[0]
##    ind = 0
##    k = 0
##    for i in a:
##        if i > max:
##            max = i
##            ind = k
##        k += 1
##    return max
##c = 0
##max = my_max(A)
##for j in A:
##    if j == max:
##        c += 1
##print(f'Maksimal qiymet {max}\nElementlerin sayi {c}')
#27
##A = list(map(int, input().split()))
##b = A[:len(A)//2]
##c = A[len(A)//2:]
##def ters(a):
##    for i in range(0,len(a)//2):
##        a[i], a[len(a)-1-i] = a[len(a)-1-i], a[i]
##    return a
##print(ters(b)+ters(c))
