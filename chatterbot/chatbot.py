from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criando ChatBot com suas propriedades
chatbot = ChatBot(
    'Turing',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii',
    ],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            #'excluded_words': ['de', 'do', 'da', 'Um', 'Uma', 'Uns'], #palavras que são excluídas pelo algoritmo na hora de procurar para não se confundir
            'default_response': 'Me desculpe, mas eu não entendi',
            'maximum_similarity_threshold': 0.80,
            'statement_comparison_function': 'chatterbot.comparisons.LevenshteinDistance'

        }, 
        
    ],
    database_uri='sqlite:///database.sqlite3'
) 

 # Treinando com o arquivo txt
training_data_quesans = open('mineracao.txt').read().splitlines()
training_data_quesans = open('eng_software.txt').read().splitlines()



training_data = training_data_quesans

trainer = ListTrainer(chatbot)
trainer.train(training_data)  
#while True:
 #   request = input('You: ')
  #  response = chatbot.get_response(request)
   # print('Bot: ', response)