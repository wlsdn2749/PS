class Game:
    
    def __init__(self, N: int, M: int, P: int, C: int, D: int): # N: 보드 크기
        self.cur_turn_number = 1
        self.santas_coords = []
        self.rudolf_coords = [0, 0]
        self.M = M
        self.P = P
        self.C = C
        self.D = D
        self.dr = [-1,0,1,0,1,1,-1,-1]
        self.dc = [0,1,0,-1,1,-1,1,-1]
        self.is_end = False
        
    def init_santa(self):
        
        for _ in range(self.P):
            Pn, Sr, Sc = map(int, input().split())
            self.santas_coords.append([Pn, Sr, Sc, 0, 0]) # 번호, 초기 행, 초기 열, 기절 여부 까지 남아있는 턴 (0)은 기절 아님, 현재 점수
            
        self.santas_coords.sort(key=lambda x:x[0])
            
    def init_rudolf(self, Rr, Rc):
        self.rudolf_coords = [Rr, Rc]
        
    def get_distance(self, r1, c1, r2, c2):
        return (r1-r2)**2 + (c1-c2)**2
        
    def move(self):
        
        if not self.is_end:
            #print("---루돌프---")
            self.move_ru()  
        
        if not self.is_end:
            #print("---산타---")
            self.move_santa()
                
        self.change_turn() 
    
    def get_santa_idx_from_santa_num(self, santa_num):
        return santa_num - 1
    def get_nearest_santa(self): # 몇 번째 산타가 루돌프로 부터 가장 가까운지 idx를 Return
        
        min_santa_idx = 9999999
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
                min_santa_idx = self.get_santa_idx_from_santa_num(temp_santas_coords[i][0])
                
        return min_santa_idx
    
    def check_collision(self, santa_idx):
        
        if not self.get_distance(self.rudolf_coords[0],
                self.rudolf_coords[1],
                self.santas_coords[santa_idx][1],
                self.santas_coords[santa_idx][2],
            ): # 충돌
                self.santas_coords[santa_idx][3] = 2 # 기절 상태가 됨, (K+2) 턴에 정상 상태가 됨.
                return True 
            
        return False # 충돌되지 않는 경우
    
    def interaction(self, santa_idx, min_idx):
                
        if not (1 <= self.santas_coords[santa_idx][1] <= N and 1 <= self.santas_coords[santa_idx][2] <= N): # 부딪혀서 탈락한 경우
            return
        
        for i in range(len(self.santas_coords)):
            if santa_idx == i:
                continue
            
            if self.santas_coords[i][1] == self.santas_coords[santa_idx][1] and self.santas_coords[i][2] == self.santas_coords[santa_idx][2]: # 이동한 자리에 상호작용 발생
                
                self.santas_coords[i][1] += self.dr[min_idx]
                self.santas_coords[i][2] += self.dc[min_idx]
                
                self.interaction(i, min_idx) # 밀려난 산타는 연쇄작용
                break
    
    
    def move_ru(self):

        nearest_santa_idx = self.get_nearest_santa()
        
        # 루돌프는 이쪽 방향으로 움직이되, 가장 가까워 지는 방향을 골라야함
        
        min_dst = 9999999
        
        for j in range(8):
            dst = self.get_distance(
                self.rudolf_coords[0] + self.dr[j],
                self.rudolf_coords[1] + self.dc[j],
                self.santas_coords[nearest_santa_idx][1],
                self.santas_coords[nearest_santa_idx][2] 
            )
            
            if min_dst > dst: # 가장 가까워지는 방향 idx와 거리 저장
                min_idx = j
                min_dst = dst
        
        # 이시점에서 min_idx는 가장 가까워지는 방향

        self.rudolf_coords[0] += self.dr[min_idx]
        self.rudolf_coords[1] += self.dc[min_idx]

        if self.check_collision(santa_idx=nearest_santa_idx): # 만약 충돌된다면 C칸만큼 밀려나면서 점수를 획득함

            self.santas_coords[nearest_santa_idx][4] += self.C 
            
            self.santas_coords[nearest_santa_idx][1] += self.dr[min_idx] * self.C
            self.santas_coords[nearest_santa_idx][2] += self.dc[min_idx] * self.C
            
            self.interaction(nearest_santa_idx, min_idx)
            
                        
    def move_santa(self):
        
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
                    if self.santas_coords[i][1] + self.dr[j] == self.santas_coords[k][1] \
                        and self.santas_coords[i][2] + self.dc[j] == self.santas_coords[k][2]: # 가려고하는데 이미 있는 경우 이동조차 못하므로 체크안함
                            duplicate = True
                
                if duplicate:
                    continue
                
                dst = self.get_distance(
                    self.rudolf_coords[0],
                    self.rudolf_coords[1],
                    self.santas_coords[i][1] + self.dr[j],
                    self.santas_coords[i][2] + self.dc[j] 
                )
                
                if min_dst > dst: # 가장 가까워지는 방향 idx와 거리 저장
                    min_idx = j
                    min_dst = dst
                
            if min_idx == -1: # 가만히 있는다
                continue
            
            # 이시점에서 min_idx는 가장 가까워지는 방향
            self.santas_coords[i][1] += self.dr[min_idx]
            self.santas_coords[i][2] += self.dc[min_idx]

            
            if self.check_collision(santa_idx=i): # 만약 충돌된다면 D칸만큼 밀려나면서 점수를 획득함

                min_idx = (min_idx + 2) % 4 # 루돌프와 부딪혔기 떄문에 반대방향으로 변경
                self.santas_coords[i][4] += self.D
                
                self.santas_coords[i][1] += self.dr[min_idx] * self.D
                self.santas_coords[i][2] += self.dc[min_idx] * self.D
                
                self.interaction(i, min_idx)
        
    def change_turn(self): # 턴 변경
            
        fall_count = 0 # 탈락한 산타 수
        for i in range(len(self.santas_coords)):
            
            if not (1 <= self.santas_coords[i][1] <= N and 1 <= self.santas_coords[i][2] <= N): # 탈락했다면
                fall_count += 1
                
            else: # 탈락하지 않았다면
                self.santas_coords[i][4] += 1 # 1점 부여
                self.santas_coords[i][3] = max(self.santas_coords[i][3]-1, 0) # 기절 Turn 하나 줄임 
            
        if fall_count == self.P or self.cur_turn_number == M: # P명의 산타가 모두 게임에서 탈락하거나, M턴이 지난경우 게임 종료
            self.is_end = True
    
        self.cur_turn_number += 1
    

if __name__ == "__main__":
    N, M, P, C, D = map(int, input().split())
    Rr, Rc = map(int, input().split()) # 루돌프의 초기위치
    
    game = Game(N, M, P, C, D)
    game.init_rudolf(Rr, Rc)
    game.init_santa()
    
    while not game.is_end:
        game.move()
        
    for i in range(len(game.santas_coords)):
        print(game.santas_coords[i][4], end=" ")