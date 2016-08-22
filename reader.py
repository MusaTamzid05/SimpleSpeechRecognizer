from recognizer import Recognizer

import os
import sys

class Reader(Recognizer):

	def __init__(self):

		Recognizer.__init__(self)

	def read(self,message):

		if sys.platform == "darwin":
			tts_engine = "say"

		elif sys.platform == "linux2" or sys.platform == "linux":
			tts_engine = "espeak"


		return os.system(tts_engine + ' "' + message + '"')


if __name__ == "__main__":

	reader = Reader()

	reader.read("This is a read test")




