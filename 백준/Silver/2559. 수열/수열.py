N, K = map(int, input().split())
temps = list(map(int, input().split()))
acc = sum(temps[:K])
ans = acc

left, right = 0, K - 1

while right < N - 1:
    acc -= temps[left]
    left += 1
    right += 1
    acc += temps[right]
    ans = max(ans, acc)

print(ans)
