
def toggle(bulb: str):
    return str(abs(int(bulb)-1))

def change(src, tar, count):
    # 0번 스위치를 누른 경우 src[0], src[1]이 변경된 상태, count는 1
    # 0번 스위치를 누르지 않은 경우 src는 그대로 count는 0
    
    src = src[:]
    for i in range(1, len(src)):
        if src[i-1] != tar[i-1]: # 바로 직전 스위치 상태가 다른경우
            count += 1
            src[i-1] = toggle(src[i-1])
            src[i] = toggle(src[i])
            
            if i+1 < len(src):
                src[i+1] = toggle(src[i+1])
                
    if str(src) == str(tar):
        return count
    else: 
        return 1e9
    

if __name__ == "__main__":
    N = int(input())

    src = list(input().strip())
    tar = list(input().strip())
    
    src_copy = src[:]
    src_copy[0] = toggle(src_copy[0])
    src_copy[1] = toggle(src_copy[1])
    
    ans = min(change(src, tar, 0), change(src_copy, tar, 1))
    
    if ans == 1e9:
        print(-1)
    else:
        print(ans)

    



