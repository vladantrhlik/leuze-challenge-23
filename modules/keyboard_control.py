from pynput.keyboard import Key, Controller
from modules import Module
from threading import Thread
import time

class KeyboardControl(Module):

	def press_key(self, key):
		self.kb.press(key)
		time.sleep(self.time)
		self.kb.release(key)

	def __init__(self, up, down, time=0):
		self.kb = Controller()
		self.up = up
		self.down = down
		self.time = time

	def update(self, direction):
		if direction == 0: return

		key = None

		if direction == 1:
			key = self.down
		elif direction == -1:
			key = self.up

		if self.time > 0:
			t = Thread(target=lambda: self.press_key(key))
			t.start()
		else:
			self.kb.press(key)
			self.kb.release(key)

