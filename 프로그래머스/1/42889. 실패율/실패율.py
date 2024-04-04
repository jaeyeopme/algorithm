def solution(N, stages):
    # 스테이지별 도전자 수(N 스테이지를 클리어하면 N + 1)
    challenger = [0] * (N + 2)
    
    for stage in stages:
        challenger[stage] += 1
        
    # 전체 인원
    total = len(stages)
    # 스테이지별 실패율
    fails = {}

    for s in range(1, N + 1):
        if challenger[s] == 0:
            fails[s] = 0
        else:
            fails[s] = challenger[s] / total
            # 전체 인원에서 이전 스테이지까지만 도달한 인원을 배제
            total -= challenger[s]

    return sorted(fails, key=lambda v: fails[v], reverse=True)