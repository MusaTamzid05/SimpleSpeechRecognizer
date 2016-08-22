from listener import Listener
from recognizer import Recognizer
from reader import Reader

from time import sleep

def main():

	listener = Listener()
	reader = Reader()


	while True:

		reader.read("Say something")
		text = listener.listen()

		if text == "stop":
			reader.read("Bye Bye Friend")
			break


		text = "you said {}".format(text)
		reader.read(text)

		sleep(2)


if __name__  == "__main__":
	main()

