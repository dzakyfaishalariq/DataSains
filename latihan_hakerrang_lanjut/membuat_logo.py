import os
os.system('cls')
array = input().split()
baris = int(array[0])
colom = int(array[1])

i = 1
j = 1
bantuan = 0
while i <= baris:
    if i == baris//2+1:
        print("WELCOME".center(colom, '-'))
    elif i > baris//2+1:
        print((".|."*bantuan).center(colom, '-'))
        bantuan -= 2
    else:
        print((".|."*j).center(colom, '-'))
        bantuan = j
        j += 2
    i += 1
