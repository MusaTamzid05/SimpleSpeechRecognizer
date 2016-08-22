from recognizer import  Recognizer



class Listener(Recognizer):

	def __init__(self):

		Recognizer.__init__(self)


	def listen(self):

		with self.microphone() as source:
			print("say something")

			audio = self.r.listen(source)

			speech_text = None
		
		try:

			speech_text = self.r.recognize_google(audio).lower().replace("'","")


		except Exception as e:  # check the book for better exception

			speech_text = e

		return speech_text





if __name__ == "__main__":

	listener = Listener()
	text = listener.listen()

	print(text)

		