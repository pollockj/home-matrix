#!/usr/bin/env python
#~ from samplebase import SampleBase
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import numpy as np
from time import sleep
from PIL import Image

class LangtonAnt():
	def __init__(self,brightness=50):
		# Configuration for the matrix
		options = RGBMatrixOptions()
		options.brightness=brightness
		options.rows = 32
		options.chain_length = 1
		options.parallel = 1
		options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
		self.matrix = RGBMatrix(options = options)
			
	def randomColor(self):
		return np.random.randint(255,size=3)
		
	def setBoard(self):
		R,G,B = self.color
		for x in range(0,len(self.board)):
			for y in range (0,len(self.board)):
				self.canvas.SetPixel(x,y,0,0,0)
		x,y = self.position
		self.canvas.SetPixel(x,y,255,0,0)
				
	def updateBoard(self):
		R,G,B = self.color
		for x in range(0,len(self.board)):
			for y in range(0,len(self.board)):
				if [x,y] == self.position:
					self.canvas.SetPixel(x,y,255,0,0)
				elif self.board[x][y] == 1:
					self.canvas.SetPixel(x,y,R,G,B)
				elif self.board[x][y] == 0:
					self.canvas.SetPixel(x,y,0,0,0)
				else:
					print("Unknown board value: {}".format(self.board[x][y]))
					
	def updateBoardv2(self):
		#~ print("Previous Position: {}".format(self.prevPosition))
		#~ print("Current Position: {}".format(self.position))
		#~ print("-"*10)
		#~ R,G,B = self.color
		R,G,B = [0,0,255]
		x,y = self.position
		self.canvas.SetPixel(x,y,255,0,0)
		x,y = self.prevPosition
		if self.board[x][y] == 1:
			self.canvas.SetPixel(x,y,R,G,B)
		elif self.board[x][y] == 0:
			self.canvas.SetPixel(x,y,0,255,0)
		else:
			print("Unknown board value: {}".format(self.board[x][y]))
		

	def moveAnt(self):
		x,y = self.position
		if self.board[x][y] == 1: #if white square
			self.direction = (self.direction - 1) % 4 #90 degree CCW turn
		elif self.board[x][y] == 0: #if black square
			self.direction = (self.direction + 1) % 4 #90 degree CW turn
		else:
			print("Unknown board color!")

		self.board[x][y] = self.board[x][y]^1 #flip the color

		if self.direction == 0: #if facing north
			ds = [0,-1]
		elif self.direction == 1: #if facing east
			ds = [1,0]
		elif self.direction == 2: #if facing south
			ds = [0,1]
		elif self.direction == 3: #if facing west
			ds = [-1,0]
		else:
			print("Unknown direction!")
		self.prevPosition = self.position
		self.position = [(i+j) % 32 for i,j in zip(self.position,ds)]
       
	def run(self):
		self.initalize()
		for i in range(self.maxIter):
			self.moveAnt()
			self.updateBoard()
			self.canvas = self.matrix.SwapOnVSync(self.canvas)
		
	def initalize(self):
		self.canvas = self.matrix.CreateFrameCanvas()
		self.position = np.random.randint(self.matrix.width,size=2)
		self.maxIter = np.random.randint(1000,10000)
		print(self.maxIter)
		self.color = np.random.randint(255,size=3)
		self.direction = np.random.randint(3)
		self.board = [[0 for x in range(self.matrix.width)] for y in range(self.matrix.width)]
		self.setBoard()

if __name__ == "__main__":
	a = LangtonAnt()
	a.run()
