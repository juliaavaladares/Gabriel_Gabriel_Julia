from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'Turing',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Me desculpe mas ainda não aprendi uma resposta adequada para este tipo de pergunta',
            'maximum_similarity_threshold': 1
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 

 # Training with Personal Ques & Ans 
training_data_quesans = open('ques_ans.txt').read().splitlines()

training_data = training_data_quesans

trainer = ListTrainer(chatbot)
trainer.train(training_data)  
while True:
    request = input('You: ')
    response = chatbot.get_response(request)
    print('Bot: ', response)