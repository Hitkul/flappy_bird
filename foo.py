import pygame
import sys
import time
import random

pygame.init()

size = [700, 700]
WHITE = (255, 255, 255)

intial_ball_x=110
intial_ball_y=350
current_ball_x = intial_ball_x
current_ball_y = intial_ball_y

first_pipe_x = 250
pipe_dx = 150

dy =1
current_pipes = []
def ball_fall(current_ball_y):
	current_ball_y+=dy
	if current_ball_y >size[1]:
	 	current_ball_y= size[1]
	return current_ball_y

def create_pipes():
	for i in xrange(0,4):
		if i==0:
			current_pipes.append(pipe(first_pipe_x,random.randint(0,353),random.randint(395,750)))
		else:
			current_pipes.append(pipe(first_pipe_x+(pipe_dx*i),random.randint(0,353),random.randint(395,750)))
def draw_circle(x,y):
	pygame.draw.circle(screen, WHITE, [x, y], 10)

screen = pygame.display.set_mode(size)

class pipe:
	def __init__(self,intial_pipe_x,y_1,y_2):
		self.pipe_x = intial_pipe_x
		self.y_1 = y_1
		self.y_2 = y_2

create_pipes()

def is_pipe_out_of_frame(foo):
	return foo.pipe_x < 0
def add_new_pipe_at_last(pipes):
	pipes.pop(0)
	pipes.append(pipe(first_pipe_x+(pipe_dx*3),random.randint(0,353),random.randint(395,750)))
	return pipes

def move_pipe(pipes):
	dx = 1
	for foo in pipes:
		foo.pipe_x -=dx
	if is_pipe_out_of_frame(pipes[0]):
		pipes = add_new_pipe_at_last(pipes)
	return pipes


def is_player_out():
	for foo in current_pipes:
		if intial_ball_x>foo.pipe_x and intial_ball_x<(foo.pipe_x+10):
			if current_ball_y>=foo.y_1:
				if current_ball_y>=foo.y_2:
					return True
				else:
					return False
			else:
				return True
	return False

def jump_ball(location):
	
	location-=dy
	if location <0:
		location= 0
	return location

def update_screen():
	global current_ball_y
	black = (0,0,0)
	screen.fill(black)
	draw_circle(current_ball_x,current_ball_y)
	for foo in current_pipes:
		pygame.draw.rect(screen,WHITE,(foo.pipe_x,0,10,foo.y_1))
		pygame.draw.rect(screen,WHITE,(foo.pipe_x,foo.y_2,10,750))
	pygame.display.update()
	if is_player_out():
		print "you are out"
		sys.exit()
	time.sleep(0.002)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			 for i in xrange(0,100):
				current_ball_y = jump_ball(current_ball_y)
				current_pipes= move_pipe(current_pipes)
				# current_pipes = move_pipe(current_pipes)
				update_screen()
	update_screen()
	current_pipes= move_pipe(current_pipes)
	current_ball_y = ball_fall(current_ball_y)
	

pygame.quit()