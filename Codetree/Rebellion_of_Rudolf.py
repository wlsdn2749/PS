class Game:
    
    def __init__(self, N: int, M: int, P: int, C: int, D: int): # N: 보드 크기
        self.board = [[0] * (N+1) for _ in range(N+1)] # 0번째 행,열은 사용하지 않고 (1,1) 부터 시작 
        self.cur_turn_number = 1
        self.santas_coords = []
        self.rudolf_coords = [0, 0]
        self.M = M
        self.P = P
        self.C = C
        self.D = D
        self.is_end = False
        
    def init_santa(self):
        
        for _ in range(self.P):
            Pn, Sr, Sc = map(int, input().split())
            self.santas_coords.append([Pn, Sr, Sc, 0, 0]) # 번호, 초기 행, 초기 열, 기절 여부 까지 남아있는 턴 (0)은 기절 아님, 현재 점수
            
        self.santas_coords.sort(key=lambda x:x[0])
            
    def init_rudolf(self, Rr, Rc):
        self.rudolf_coords = [Rr, Rc]
        
    def move(self):
        
        if not self.is_end:
            #print("---루돌프---")
            self.move_ru()  
        
        if not self.is_end:
            #print("---산타---")
            self.move_santa()
                
        self.change_turn() 
    
    def check_collision(self, santa_idx):
        
        if self.rudolf_coords[0] == self.santas_coords[santa_idx][1] \
            and self.rudolf_coords[1] == self.santas_coords[santa_idx][2]: # 충돌
                self.santas_coords[santa_idx][3] = 2 # 기절 상태가 됨, (K+2) 턴에 정상 상태가 됨.
                return True 
            
        return False # 충돌되지 않는 경우
    
    def interaction(self, santa_num, r, c, min_idx):
                    
        dr = [-1,0,1,0,1,1,-1,-1]
        dc = [0,1,0,-1,1,-1,1,-1]
        
        if not (1 <= r <= N and 1 <= c <= N): # 부딪혀서 탈락한 경우
            return
        
        
        for i in range(len(self.santas_coords)):
            
            #print(self.santas_coords[i][0], "번째 산타 현재 위치", self.santas_coords[i][1], self.santas_coords[i][2], "루돌프 위치", self.rudolf_coords[0], self.rudolf_coords[1])
            
            if self.santas_coords[i][0] == santa_num: # 자기자신은 체크하면 안됨
                continue
            
            if self.santas_coords[i][1] == r and self.santas_coords[i][2] == c: # 이동한 자리에 상호작용 발생
                
                #print(f"상호작용 발생! {self.santas_coords[i][0]} 번째 산타는 {dr[min_idx]} , {dc[min_idx]} 만큼 밀려남!")
                
                self.santas_coords[i][1] += dr[min_idx]
                self.santas_coords[i][2] += dc[min_idx]
                
                self.interaction(self.santas_coords[i][0], self.santas_coords[i][1], self.santas_coords[i][2], min_idx) # 밀려난 산타는 연쇄작용
                break
            

    
    def move_ru(self):
        dr = [-1,0,1,0,1,1,-1,-1]
        dc = [0,1,0,-1,1,-1,1,-1]
        santa_num = self.get_nearest_santa()
        
        for i in range(len(self.santas_coords)):
            
            if self.santas_coords[i][0] == santa_num:  # 루돌프는 이쪽 방향으로 움직이되, 가장 가까워 지는 방향을 골라야함
                dst = 0
                min_dst = 9999999
                min_idx = 0
                for j in range(8):
                    dst = self.get_distance(
                        self.rudolf_coords[0] + dr[j],
                        self.rudolf_coords[1] + dc[j],
                        self.santas_coords[i][1],
                        self.santas_coords[i][2] 
                    )
                    
                    if min_dst > dst: # 가장 가까워지는 방향 idx와 거리 저장
                        min_idx = j
                        min_dst = dst
                
                # 이시점에서 min_idx는 가장 가까워지는 방향
                #print(f'루돌프 이동 전 위치 {self.rudolf_coords}')
                self.rudolf_coords[0] += dr[min_idx]
                self.rudolf_coords[1] += dc[min_idx]
                #print(f'루돌프 이동 후 위치 {self.rudolf_coords}')
                #print(f"루돌프가 {santa_num}번 산타쪽으로 이동")
                if self.check_collision(santa_idx=i): # 만약 충돌된다면 C칸만큼 밀려나면서 점수를 획득함
                    #print(f"루돌프는 {santa_num}번 산타에게 박치기 를 시전했다.")
                    self.santas_coords[i][4] += self.C 
                    
                    self.santas_coords[i][1] += dr[min_idx] * self.C
                    self.santas_coords[i][2] += dc[min_idx] * self.C
                    
                    #print(f"{self.santas_coords[i][0]} 번째 산타는 지금 {self.santas_coords[i][1]}, {self.santas_coords[i][2]}")
                    
                    self.interaction(santa_num, self.santas_coords[i][1], self.santas_coords[i][2], min_idx)
                
                break 
        
            else:
                continue
                        

    def move_santa(self):
        
        dr = [-1,0,1,0] # 상우하좌
        dc = [0,1,0,-1]
        
        for i in range(len(self.santas_coords)):
            
            if self.santas_coords[i][3] > 0: # 기절했거나
                continue
            
            if not ( 1 <= self.santas_coords[i][1] <= N and 1 <= self.santas_coords[i][2] <= N) : # 게임에서 탈락한 산타는 움직일 수 없음
                continue
            
            dst = 0
            min_dst = self.get_distance(
                self.rudolf_coords[0],
                self.rudolf_coords[1],
                self.santas_coords[i][1],
                self.santas_coords[i][2] 
            ) # 이 거리보다 min_dst가 커질 경우는 움직일 수 있는 칸이 있더라도 가만히 있다.
            min_idx = -1
            for j in range(4):
                
                duplicate = False
                for k in range(len(self.santas_coords)):
                    if self.santas_coords[i][1] + dr[j] == self.santas_coords[k][1] \
                        and self.santas_coords[i][2] + dc[j] == self.santas_coords[k][2]: # 가려고하는데 이미 있는 경우 이동조차 못하므로 체크안함
                            duplicate = True
                
                if duplicate:
                    continue
                
                dst = self.get_distance(
                    self.rudolf_coords[0],
                    self.rudolf_coords[1],
                    self.santas_coords[i][1] + dr[j],
                    self.santas_coords[i][2] + dc[j] 
                )
                
                if min_dst > dst: # 가장 가까워지는 방향 idx와 거리 저장
                    min_idx = j
                    min_dst = dst
                    
            #TODO implementation 움직일 수 있는 칸이 있더라도 가까워 질 수 있는 방법이 없는 경우 
            if min_idx == -1: # 가만히 있는다
                #print(self.santas_coords[i][0], "번째 산타는 가만히 있는다")
                continue
            
            # 이시점에서 min_idx는 가장 가까워지는 방향
            self.santas_coords[i][1] += dr[min_idx]
            self.santas_coords[i][2] += dc[min_idx]
            
            
            
            #print("방향:", min_idx, ",", self.santas_coords[i][0], "번째 산타 이동 후", self.santas_coords[i][1], self.santas_coords[i][2], "루돌프 위치", self.rudolf_coords[0], self.rudolf_coords[1])
            
            if self.check_collision(santa_idx=i): # 만약 충돌된다면 D칸만큼 밀려나면서 점수를 획득함
                #print(f"{self.santas_coords[i][0]}번 산타는 루돌프에게 박치기를 시전했다!.")
                min_idx = (min_idx + 2) % 4 # 루돌프와 부딪혔기 떄문에 반대방향으로 변경
                self.santas_coords[i][4] += self.D
                
                self.santas_coords[i][1] += dr[min_idx] * self.D
                self.santas_coords[i][2] += dc[min_idx] * self.D
                
                #print(self.santas_coords[i][0], "번째 산타 충돌 후", self.santas_coords[i][1], self.santas_coords[i][2], "루돌프 위치", self.rudolf_coords[0], self.rudolf_coords[1])
                
                
                self.interaction(self.santas_coords[i][0], self.santas_coords[i][1], self.santas_coords[i][2], min_idx)
    
    def get_nearest_santa(self): # 몇 번째 산타가 가장 가까운지 Return
        
        min_santa_num = 9999999
        min_santa_dist = 9999999
        
        temp_santas_coords = sorted(self.santas_coords, key=lambda x:(-x[1], -x[2])) # r, c좌표가 큰순으로 정렬
        
        for i in range(len(temp_santas_coords)):
            dst = self.get_distance(
                self.rudolf_coords[0],
                self.rudolf_coords[1],
                temp_santas_coords[i][1],
                temp_santas_coords[i][2] 
            )   
            if not (1 <= temp_santas_coords[i][1] <= N and 1 <= temp_santas_coords[i][2] <= N): # 이미 탈락한 산타는 루돌프가 박치기 안함,, 탈락헀는데 박치기하면 너무 슬프자나 ㅠㅠ..
                continue  
            
            if min_santa_dist > dst: # 좌표를 구햇더니 루돌프로 부터 가까운 값이면?
                min_santa_dist = dst
                min_santa_num = temp_santas_coords[i][0]
                
        return min_santa_num
                

    def get_distance(self, r1, c1, r2, c2):
        return (r1-r2)**2 + (c1-c2)**2
        
        
    def change_turn(self): # 턴 변경
            
        fall_count = 0 # 탈락한 산타 명수
        for i in range(len(self.santas_coords)):
            
            if not (1 <= self.santas_coords[i][1] <= N and 1 <= self.santas_coords[i][2] <= N): # 탈락했다면
                fall_count += 1
                
            else: # 탈락하지 않았다면
                self.santas_coords[i][4] += 1 # 1점 부여
                self.santas_coords[i][3] = max(self.santas_coords[i][3]-1, 0) # 기절 Turn 하나 줄임 
            
        if fall_count == self.P or self.cur_turn_number == M: # P명의 산타가 모두 게임에서 탈락하거나, M턴이 지난경우 게임 종료
            self.is_end = True
    
        self.cur_turn_number += 1
        
        # Debug
        #print(f"현재 turn은 {self.cur_turn_number-1}")
        for i in range(len(self.santas_coords)):
            pass
            #print(self.santas_coords[i][4], end=" ")
        #print("")


if __name__ == "__main__":
    N, M, P, C, D = map(int, input().split())
    Rr, Rc = map(int, input().split()) # 루돌프의 초기위치
    
    game = Game(N, M, P, C, D)
    game.init_rudolf(Rr, Rc)
    game.init_santa()
    
    while not game.is_end:
        game.move()
        
    for i in range(len(sorted(game.santas_coords, key=lambda x:x[0]))):
        print(game.santas_coords[i][4], end=" ")