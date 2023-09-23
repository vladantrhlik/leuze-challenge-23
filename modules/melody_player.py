from modules import Module
import time
from pysinewave import SineWave
from melodies import melodies
from threading import Thread

class MelodyPlayer(Module):

	def play_sound(self, freq, length):
		self.sinewave.set_frequency(freq)
		self.sinewave.play()
		time.sleep(length)
		self.sinewave.stop()
		self.sinewave.set_frequency(0)

	def __init__(self, melody):

		if melody not in melodies.keys():
			print("melody not fount")
			return

		self.melody = melodies[melody]
		self.sinewave = SineWave(pitch=12, pitch_per_second=100)
		self.position = 0

	def update(self, direction):
		self.position += direction

		if self.position >= len(self.melody)/2-1:
			self.position = 0

		freq = self.melody[int(self.position)*2]
		length = self.melody[int(self.position)*2+1]

		t = Thread(target=lambda: self.play_sound(freq, .5 ))
		t.start()

