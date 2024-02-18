N = int(input())
hints = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            # 서로 다른 숫자 세개
            if a == b or a == c or b == c:
                continue

            cnt = 0

            for hint in hints:
                numbers = list(str(hint[0]))
                a1, b1, c1 = map(int, numbers)

                strike = hint[1]
                ball = hint[2]

                strike_count = 0
                ball_count = 0

                if a == a1:
                    strike_count += 1
                if b == b1:
                    strike_count += 1
                if c == c1:
                    strike_count += 1

                if a != a1 and str(a) in numbers:
                    ball_count += 1    
                if b != b1 and str(b) in numbers:
                    ball_count += 1    
                if c != c1 and str(c) in numbers:
                    ball_count += 1    
                
                if strike == strike_count and ball == ball_count:
                    cnt += 1

            # 모든 힌트를 통과했다면
            if cnt == N:
                answer += 1

print(answer)