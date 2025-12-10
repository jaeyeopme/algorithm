import sys
input = sys.stdin.readline

for _ in range(int(input())):
    line = list(map(int, input().split()))
    T = line[0]
    arr = line[1:]
    
    count = 0

    for i in range(20):
        for j in range(i):
            if arr[j] > arr[i]:
                count += 1
                
    print(T, count)
