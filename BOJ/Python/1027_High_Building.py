import decimal

def is_visible(x1, y1, x2, y2, x, y):
    # y < (y2-y1)/(x2-x1) * (x - x1) + y1 을
    # cross multiplication 형태로 변형
    return (y - y1) * (x2 - x1) < (y2 - y1) * (x - x1)

def get_segment_solve(target_idx, start_idx, end_idx, buildings):
    count = 0
    for left_idx in range(start_idx, end_idx):
    
        # 이미 했던 인덱스
        # left_idx와 right_idx의 직선의 방정식, (x1=left_idx, y1=buildings[left_idx], x2=right_idx, y2=buildings[right_idx])
        if start_idx == 0:
            x1 = left_idx
            x2 = target_idx
            y1 = buildings[left_idx]
            y2 = buildings[target_idx]
        else:
            x1 = target_idx
            x2 = end_idx
            y1 = buildings[target_idx]
            y2 = buildings[end_idx]

        
        # y = (y2-y1)/(x2-x1) * (x-x1) + y1 
        f = lambda x: (decimal.Decimal(y2-y1)/decimal.Decimal(x2-x1)) * decimal.Decimal(x-x1) + y1

        # 구한 직선의 방정식 f(x)에 대해 사이에 있는 b_i에 대해 연산
        for middle_idx in range(left_idx + 1, end_idx):
            x = middle_idx
            y = buildings[middle_idx]
            ## print(f"{x1}와 {x2} 사이의, {x}에 대한 유효성 검사")
            # f(b_i(x))가 buildings[b_i(x)]보다 작으면 통과, 크거나 같으면 탈락 -> 탈락 하는순간 거기서 종료 다음 loop
            #print(buildings[x], f(x))
            
            if decimal.Decimal(buildings[x]) >= decimal.Decimal(f(x)):
                ## print(f"{x1}와 {x2} 사이의, {x}에 대한 유효성 검사 실패")
                break
                
        
        else: # break문으로 종료되지 않았을 경우, 즉 사이에 있는 모든 연산이 완료된 경우, 막히는게 없으니까 마지막도 추가
            #print(f"{left_idx}, {end_idx}의 연결 유효성 확인")
            ## print(f"{x1}와 {x2} 사이의 유효성 검사 성공")
            count += 1

    
        ## print(f"start:{start_idx}, end:{end_idx}  count : {count}")

    return count

def solve() -> int:
    N = int(input().strip())

    buildings = list(map(int, input().split()))
    max_count = 0

    if N == 2:
        return 1
    
    for target_idx in range(1, len(buildings)-1): # 구하고 싶은 idx
        ## print(f"-----------target: {target_idx}------")
        left_count = get_segment_solve(target_idx, 0, target_idx, buildings)
        ## print(f"left_count 종료")
        right_count = get_segment_solve(target_idx, target_idx, len(buildings)-1, buildings)
        ## print("right_count 종료")
        max_count = max(max_count, left_count+right_count)
        ## print(f"count : {left_count+right_count}")
                
    return max_count

if __name__ == "__main__":
    print(solve())

    """
    input:
    7
    154847237 154847238 154847239 154847235 154847234 154847232 154847221
    output: 3
    answer: 4
    """


    