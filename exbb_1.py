import tkinter as tk
import sys

win_width=600
win_height=480
win_center_x=win_width/2
tick=40

root=tk.Tk()
root.title("exbb_1")
root.geometry("600*480")
cv=tk.Canvas(root,width=win_width,height=win_height)
cv.pack()

class Ball:
	x=250
	y=250
	w=10
	
	dx=dy=2
	color="red"
	
	def draw(self):
		cv.create_oval(self.x-self.w,self.y-self.w,self.x+self.w,self.y+self.w,fill=self.color,tag="ball")
		cv.pack()
	
	def move(self):
		self.x += self.dx
		self.y += self.dy
		
		if self.x - self.w < 0 or self.x + self.w > win_width:
			self.dx*=-1
		
		if self.y - self.w < 0 or self.y + self.w > win_height:
			self.dy*=-1
		
		if self.y + self.w > paddle.y - paddle.wy and ball.x > paddle.x - paddle.wx and ball.x < paddle.x +paddle.wx:
			self.dy*=-1
	
	def delete(self):
		cv.delete("ball")

class Paddle:
	x=win_center_x
	y=win_height-30
	wx=45
	wy=8
	dx=6
	color="blue"
	
	def draw(self):
		cv.create_rectangle(self.x-self.wx,self.y-self.wy,self.x+self.wx,self.y+self.wy,fill=self.color,tag="paddle")
	
	def right(self,event):
		cv.delete("paddle")
		self.x+=self.dx
		self.draw()
	
	def left(self,event):
		cv.delete("paddle")
		self.x-=self.dx
		self.draw()
	
	def move(self):
		root.bind("<Right>",self.right)
		root.bind("<Left>",self.left)

class Block:
	w_x=100
	w_y=30
	
	global dy,score
	
	block_list=[[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1]]
	
	def draw(self):
		for i in range(6):
			for j in range(3):
				cv.create_rectangle(i*self.w_x,j*self.w_y,(i+1)*self.w_x,(j+1)*self.w_y,fill="orange",tag="block"+str(j)+str(i))
	
	def reflect(self):
		for i in range(12):
			for j in range(3):
				if (ball.y-ball.w < (j+1)*self.w_y and i*self.w_x < ball.x < (i+1)*self.w_x and self.block_list[j][i] == 1):
					ball.dy*=-1
					cv.delete("block"+str(j)+str(i))
					self.block_list[j][i]=0
					score.score+=1
					score.delete()
					score.draw()

class Score():
	score=0
	def draw(self):
		cv.create_text(win_width-50,50,text="Score="+str(self.score),font=("FixedSys",16),tag="score")
	def delete(self):
		cv.delete("score")

def gameover():
	global w,dx,dy
	if ball.y + ball.w > win_height:
		cv.delete("paddle")
		cv.delete("ball")
		cv.create_text(win_center_x,win_center_y,text="GAMEOVER(^-^#)",font=("FixedSys",40))
		ball.w=0
		ball.dx=0
		ball.dy=0

def gameclear():
	global w,dx,dy
	if score.score == 18:
		cv.delete("paddle")
		cv.delete("ball")
		cv.create_text(win_center_x,win_center_y,text="GAMECLEAR\(^o^)/",font=("FixedSys",40))
		ball.w=0
		ball.dx=0
		ball.dy=0

paddle=Paddle()
ball=Ball()
block=Block()
score=Score()

ball.draw()
paddle.draw()
block.draw()
score.draw()

def gameloop():
	ball.delete()
	ball.move()
	paddle.move()
	block.reflect()
	ball.draw()
	gameover()
	gameclear()
	root.after(tick,gameloop)

gameloop()
root.mainloop()
