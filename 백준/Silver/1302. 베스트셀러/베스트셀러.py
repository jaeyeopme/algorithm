import sys

input = sys.stdin.readline

N = int(input())
books = {}

for _ in range(N):
    name = input().strip()
    if name not in books:
        books[name] = 1
        continue
    books[name] += 1

max_count = max(books.values())

for name in sorted(books.keys()):
    if books[name] == max_count:
        print(name)
        break
