stuff = [10 * 5, 
10 ** 2, 
15 / 10, 
15 // 10, 
-15 // 10, 
15 % 10,
10 % 15,
10 % 10,
0 % 10,
10 / 15]

n = 0
while(len(stuff) > n ):
    print(stuff[n])
    n = n + 1

# the last one is wrong because it is not the exact value and is technically rounded