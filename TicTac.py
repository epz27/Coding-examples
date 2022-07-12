# -*- coding: utf-8 -*-

import os
class TicTacToe:
    
    def __init__(self,n):
        
        self.board=[]
        self.verts=[]
        self.horiz=[]
        self.n=n
        self.remaining=n*n
        for i in range(n):
            self.verts.append([0,0])
            self.board.append([])
            self.horiz.append([0,0])
            for j in range(n):
                self.board[i].append("-")
    
        self.main=[0,0]
        self.off=[0,0]
    
    def __str__(self):
        ans=""
        for i in range(self.n):
            line=str(self.board[i][0])
            for j in range(1,self.n):
                line+="|"+str(self.board[i][j])
            ans+=line
            if i!=self.n-1:
                ans+="\n"
        return ans
            
    def move_X(self,i,j):
        self.board[i][j]="X"
        self.horiz[i][0]+=1
        if self.horiz[i][0]==self.n:
            print("\n")
            print("Player 1 Wins!!")
            print("\n")
            print(self)
            return 1
        self.verts[j][0]+=1
        if self.verts[j][0]==self.n:
            print("\n")
            print("Player 1 Wins!!")
            print("\n")
            print(self)
            return 1
        
        if i==j:
            self.main[0]+=1
            if self.main[0]==self.n:
                print("\n")
                print("Player 1 Wins!!")
                print("\n")
                print(self)
                return 1
        if i+j==self.n-1:
            self.off[0]+=1
            if self.off[0]==self.n:
                print("\n")
                print("Player 1 Wins!!")
                print("\n")
                print(self)
                return 1
        self.remaining-=1
        print("\n")
        print(self)
        print("\n")
        return 0
    
    def move_O(self,i,j):
        self.board[i][j]="O"
        self.horiz[i][1]+=1
        if self.horiz[i][1]==self.n:
            print("\n")
            print("Player 2 Wins!!")
            print("\n")
            print(self)
            return 2
        self.verts[j][1]+=1
        if self.verts[j][1]==self.n:
            print("\n")
            print("Player 2 Wins!!")
            print("\n")
            print(self)
            return 2
        
        if i==j:
            self.main[1]+=1
            if self.main[1]==self.n:
                print("\n")
                print("Player 2 Wins!!")
                print("\n")
                print(self)
                return 2
        if i+j==self.n-1:
            self.off[1]+=1
            if self.off[1]==self.n:
                print("\n")
                print("Player 2 Wins!!")
                print("\n")
                print(self)
                return 2
        self.remaining-=1
        print("\n")
        print(self)
        print("\n")
        return 0




if __name__ == "__main__":
    
    size=input("Welcome to TicTacToe! Enter board size: ")
    
    game=TicTacToe(int(size))
    
    end=False
    turn=1
    while not end:
        if turn==1:
            nex=input("Player 1, enter your move (i,j): ")
            pos=nex[1:len(nex)-1]
            nums=pos.split(",")
            result=game.move_X(int(nums[0]),int(nums[1]))
            turn=2
        else:
            nex=input("Player 2, enter your move (i,j): ")
            pos=nex[1:len(nex)-1]
            nums=pos.split(",")
            result=game.move_O(int(nums[0]),int(nums[1]))
            turn=1
        if result==1 or result==2:
            end=True
        if game.remaining==0:
            end=True
            print("\n")
            print("Noone wins")
            
            
    

        
            
            