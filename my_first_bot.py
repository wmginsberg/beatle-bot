import os
from markovbot import MarkovBot 

tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))

book = os.path.join(dirname, 'EveryBeatleslyricrecorded.txt')

tweetbot.read(book)

my_first_text = tweetbot.generate_text(50)
print("tweetbot says:")
print(my_first_text)
