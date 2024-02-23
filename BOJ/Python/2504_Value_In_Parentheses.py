from collections import deque

parentheses = input().strip()

st = deque()

def print_zero():
    print(0)
    exit(0)
    
def valid(ch, opposite):
    if ch == ']' and opposite == '(': # case : (]
        print_zero()    
    elif ch == ')' and opposite == '[': # case : [)
        print_zero()    
        
def parse_chs(ch):
    weight = 3 if ch == ']' else 2 # 괄호에 따른 가중치
    op_parenthesis = '[' if ch == ']' else '(' # 괄호에 따른 opposite parenthesis
    parse_list = [] # pending parse list
    check = False # 스택에서 제거하는 동안 상대 괄호를 만나야함
    
    while st:
        value = st.popleft()
        valid(ch, value)
        parse_list.append(value)
        if value == op_parenthesis:
            check = True
            break
        
    if not check:
        print_zero()
        
    # case len == 2 [] // push 3
    if len(parse_list) == 2:
        st.appendleft(weight) 
        
    # case len == 3 [x] // push 3 * x
    elif len(parse_list) == 3:
        st.appendleft(weight*parse_list[1]) 
        
    # case len == 4 [xy] // push 3 * (x+y) case added [x+y+z -> OK]
    elif len(parse_list) >= 4:
        st.appendleft(weight*(sum(parse_list[1:len(parse_list)-1])))            
    
for ch in parentheses:

    if ch == ')' or ch == ']':
        if not st: # case ]
            print_zero()    
        else:
            st.appendleft(ch)
            parse_chs(ch) 
    
    else: # ( or [
        st.appendleft(ch)
  
# 남아 있는 스택에 대하여
# 모두 숫자가 있어야하지만, 만약 하나라도 괄호가 있다면? 오류
result = 0

while st:
    value = st.popleft()
    if not isinstance(value, int):
        print_zero()
    else:
        result += value
        
print(result)
    

