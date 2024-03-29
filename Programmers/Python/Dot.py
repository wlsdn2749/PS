'''
    원점으로 부터 거리가 d를 넘지 않는 점

    거리 함수 구현 
    이때 증감 배수 k가 있다

    d = 5, k = 1
    (0,1),(0,2),(0,3),(0,4),(0,5)
    (1,0),(0,) ...



    한쪽만 구해주고 같은거는 따로 더해주기

    a는 1~k 고정하고
    b는 이분탐색으로 가능한지 여부 따지기

    mid = d//2
    if distance(a, mid) < d:
        mid = (a+mid) // 2
    else:
        mid = (0+mid) // 2

    mid 아래는 모두 가능?

'''

def get_possible_y(x, d):
    # print(int((d**2 - x**2)**0.5))
    return int((d**2 - x**2)**0.5)

def solution(k, d):
    answer = 0

    for idx, x in enumerate(range(0,d+1, k)):
        answer += get_possible_y(x,d) // k +1 


    return answer
