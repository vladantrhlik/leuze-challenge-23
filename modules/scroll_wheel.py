from pynput.mouse import Button,Controller
from modules import Module

class ScrollWheel(Module):
	def __init__(self):
		self.mouse = Controller()

	def update(self, direction):
		self.mouse.scroll(0, direction)
