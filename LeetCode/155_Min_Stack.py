class MinStack:

    def __init__(self):
        self.st = []
        
    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val: # 새로 들어온 값이 더 작을 경우
            min_val = val # 최소값 갱신
            
        self.st.append([val, min_val])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None
        
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()

# -3이 빠지면서 stack에 영향을 안 주도록 어떻게?.. dict로!

