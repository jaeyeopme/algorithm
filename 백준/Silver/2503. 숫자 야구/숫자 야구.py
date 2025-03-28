N = int(input())
guesses = [list(map(int, input().split())) for _ in range(N)]
answer  = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or a == c or b == c:
                continue
            count = 0

            for guess in guesses:
                number, strike, ball = guess
                a1, b1, c1 = map(int, str(number))
                
                if a == a1:
                    strike -= 1
                if b == b1:
                    strike -= 1
                if c == c1:
                    strike -= 1

                if a == b1 or a == c1:
                    ball -= 1
                if b == a1 or b == c1:
                    ball -= 1
                if c == a1 or c == b1:
                    ball -= 1

                if strike == 0 and ball == 0:
                    count += 1

            if count == N:
                answer += 1

print(answer)
