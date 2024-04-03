# M D C L X V I -> 내림차순 나열
# VLD는 1번
# IXCM은 연속해서 3번까지만 사용 가능

# 작은 숫자가 큰 숫자의 왼쪽에 오는 경우는 
# 한, 두 단계 차이나는 경우 (큰단계 - 작은단계) 값
# IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900
# Queue ( Encoding )

# MCMXL = 1000 + 900 + 40
# 1000 + (100 + (1000) - 2* 100) + (10 + (50) - 2*10)

# MMCDXCIII
# 1000 1000 (100 + (500) - 2*100) + (10 + (100) - 2*10) + 1 + 1 + 1 

# Decoding

# 천의 자리
# 3000 -> MMM...

# 백의 자리
# 900 -> CM
# 800 -> DCCC
# 700 -> DCC
# 600 -> DC
# 500 -> D
# 400 -> CD
# 300 -> CCC

# 2493 (Decoding)
# MM (2000)
# CD (400)
# XC (90)
# III (3)
# 

def encoding(string: str) -> int:
    q = list()
    
    for c in string:
        if not q:
            q.append(roman_dict[c])
            continue
        
        if q:
            if q[-1] < roman_dict[c]:
                q.append(roman_dict[c] - 2*q[-1])
            else:
                q.append(roman_dict[c])
    
    return sum(q)

def decoding(number: int) -> str:
    
    def partial(number, e):
        return_str = []
        roman_str = []
        if e == None:
            return_str.append( 'M' * (number // 1000 ))
            return ''.join(return_str)
        
        if e == 1000:
            roman_str = ['M', 'D', 'C']
        elif e == 100:
            roman_str = ['C', 'L', 'X']
        else:
            roman_str = ['X', 'V', 'I']
                    
        
        order = (number%e) // (e//10)
        
        if (order) == 4:
            return_str.append(roman_str[2] + roman_str[1])  
        
        elif (order) == 9:
            return_str.append(roman_str[2] + roman_str[0])
            
        else:
            if(order) >= 5:
                return_str.append(roman_str[1])
                number -= (e//2)
                order = (number%e) // (e//10)
                
            return_str.append(roman_str[2] * (order))
        
        return ''.join(return_str)
    
    return (partial(number, None) +
            partial(number, 1000) +
            partial(number, 100) +
            partial(number, 10))


   
roman_dict = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000}

    
str1 = input().strip()
str2 = input().strip()

added_number = encoding(str1) + encoding(str2)
print(added_number)

roman_string = decoding(added_number)
print(roman_string)


