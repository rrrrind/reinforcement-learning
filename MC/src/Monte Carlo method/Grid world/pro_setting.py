# 格子世界の構築
import numpy as np

def generate_stage():
    stage = [[0,4],[1,4],[2,4],[3,4],[4,4],
             [0,3],[1,3],[2,3],[3,3],[4,3],
             [0,2],[1,2],[2,2],[3,2],[4,2],
             [0,1],[1,1],[2,1],[3,1],[4,1],
             [0,0],[1,0],[2,0],[3,0],[4,0]]
    return stage



# エージェントの設計
# エージェントには，『状態』『行動』『報酬』『方策』を持たせている

class Agent(): 
    # 行動aの宣言。引数で使うので、初めに宣言する。
    actions = [[0,1],[0,-1],[-1,0],[1,0]] # up,down,left,right
    
    def __init__(self):
        self.position = []
        self.pi = []
    
    def set_pos(self,now_pos):
        # 現在地の更新
        self.position = now_pos
        
    def get_pos(self):
        # 現在地の取得
        return self.position
    
    def set_pi(self,new_pi):
        # 方策の更新
        self.pi = new_pi
    
    def get_pi(self):
        # 方策の取得
        return self.pi
    
    def move(self,action):
        # 行動後の位置の取得
        if self.get_pos() == [1,4]: # 10ptゾーン
            next_pos = [1,0]
        elif self.get_pos() == [3,4]: # 5ptゾーン
            next_pos = [3,2]
        else :
            next_pos = [self.get_pos()[0] + action[0], self.get_pos()[1] + action[1]]
        
        # 境界線外に出ている時の処理
        if 0 > next_pos[0] or next_pos[0] > 4 or 0 > next_pos[1] or next_pos[1] > 4:
            next_pos = self.get_pos()
            
        self.set_pos(next_pos)
        
    def reward(self,state,action):
        if state == [1,4]:
            return 10
        
        if state == [3,4]:
            return 5
        
        if state[1] == 4 and action == [0,1]:
            return -1
        elif state[1] == 0 and action == [0,-1]:
            return -1
        elif state[0] == 0 and action == [-1,0]:
            return -1
        elif state[0] == 4 and action == [1,0]:
            return -1
        else :
            return 0
