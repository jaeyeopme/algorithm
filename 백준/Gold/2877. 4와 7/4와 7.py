import sys

input = sys.stdin.readline

K = int(input())
binary_str = bin(K + 1)[3:]
print(binary_str.replace("0", "4").replace("1", "7"))
