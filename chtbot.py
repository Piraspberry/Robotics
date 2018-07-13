from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
print (chatbot.get_response("i am gowtham"))