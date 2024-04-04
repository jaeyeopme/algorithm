def solution(dirs):
    directions = {
        "U": (0, 1),
        "R": (1, 0),
        "D": (0, -1),
        "L": (-1, 0)
    }
    
    x, y = 0, 0
    coordinate = set()
    
    for d in dirs:
        tx, ty = x + directions[d][0], y + directions[d][1]
        
        # 경계를 넘는 경우 무시
        if not (-5 <= tx <= 5 and -5 <= ty <= 5):
            continue
            
        coordinate.add((x, y, tx, ty))
        coordinate.add((tx, ty, x, y))
        x, y = tx, ty
    
    return len(coordinate) // 2
