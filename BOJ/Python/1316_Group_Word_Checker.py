from collections import defaultdict

N = int(input())

def group_word_check(s: str):
    dd = defaultdict(list)
    
    for idx, char in enumerate(s):
        dd[char].append(idx)
        
    for key, value in dd.items():
        
        if len(value) == 1:
            continue
        
        else:
            for idx in range(len(value)-1):
                if abs(value[idx] - value[idx+1]) != 1:
                    return 0
    return 1

        
if __name__ == "__main__":
    
    result = 0
    for i in range(N):
        result += group_word_check(input().strip())
        
    print(result)
    

    
    
    
    
    