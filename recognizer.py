import speech_recognition as sr

class Recognizer:

	def __init__(self):

		self.r = sr.Recognizer()
		self.microphone = sr.Microphone