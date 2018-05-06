import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import os
import random 
class Museum():
	def __init__(self,d='art/',brightness=50):
		self.images = os.listdir(d)
		# Configuration for the matrix
		options = RGBMatrixOptions()
		options.brightness=brightness
		options.rows = 32
		options.chain_length = 1
		options.parallel = 1
		options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
		self.matrix = RGBMatrix(options = options)
		self.imageDirectory=d
	def generateIndexArray(self):
		array = range(len(self.images))
		random.shuffle(array)
		return array
		
	def run(self):
		while True:
			imgIndex = self.generateIndexArray()
			for index in imgIndex: 
				print(self.images[index])
				image = Image.open(self.imageDirectory + self.images[index])
				image = image.rotate(180)
				# Make image fit our screen.
				image.thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
				self.matrix.SetImage(image.convert('RGB'))
				time.sleep(random.randint(5*60,10*60))

if __name__ == "__main__":
	m = Museum()
	m.run()
