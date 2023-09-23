from modules import Module
from pynput.keyboard import Key, Controller
from threading import Thread
import time

class WindowSwitcher(Module):

	def release_tab(self):
		time.sleep(self.timeout)
		if time.time() - self.last_active > self.timeout*.99:
			self.kb.release(Key.alt_l)

	def __init__(self, timeout = 1):
		self.kb = Controller()
		self.last_active = 0
		self.timeout = timeout

	def update(self, direction):
		self.kb.press(Key.alt_l)

		if direction == 1:
			self.kb.tap(Key.tab)
		elif direction == -1:
			self.kb.press(Key.shift_l)
			self.kb.tap(Key.tab)
			self.kb.release(Key.shift_l)

		self.last_active = time.time()

		t = Thread(target=self.release_tab)
		t.start()


