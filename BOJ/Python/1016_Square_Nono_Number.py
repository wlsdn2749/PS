min_number, max_number = map(int, input().split())

arr = [1 for _ in range(max_number - min_number + 1)]

# 제곱 수 미리 구해놓기
# 4 - 16 - 64  이런식으로 제곱수로 나눠지는 제곱수는 넣을 필요가 없다
# 4 - 36
square_number = set()
number = 2
MAX_NUMBER = 1000000000000
LIMIT_MAX = int(MAX_NUMBER ** 0.5)
prime = [1 for _ in range(LIMIT_MAX + 1)]
while number <= LIMIT_MAX:
    if prime[number] == 0:
        number+=1
        continue

    for i in range(number, LIMIT_MAX, number):
        if prime[number] == 1:
            prime[number] = 0
    
    square_number.add(number**2)
    number+=1
    

result = 0
sorted_square_number = sorted(square_number) # ~1000) 까지의 소수 제곱들
# print(list(sorted_square_number))

for k in sorted_square_number:
    b_min_k = min_number if (min_number // k) * k >= min_number else (min_number//k) * k + k
    while b_min_k <= max_number:
        if arr[b_min_k - min_number] == 1:
            # print(b_min_k, "는 나누어 떨어짐")
            arr[b_min_k - min_number] = 0 # 이 숫자는 나누어 떨어짐
        
        b_min_k += k
        
print(sum(arr))

