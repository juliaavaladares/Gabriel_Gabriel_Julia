from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_most_frequent_response


# Criando ChatBot com suas propriedades
chatbot = ChatBot(
    'Turing',
    response_selection_method=get_most_frequent_response,
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
            'maximum_similarity_threshold': 0.90,
            'statement_comparison_function': 'chatterbot.comparisons.LevenshteinDistance'

        }, 
        
    ],
    database_uri='sqlite:///database.sqlite3'
) 

chatbot.storage.drop()

 # Treinando com o arquivo txt
training_data_quesans2 = open('meio_conversa.txt').read().splitlines()
training_data_quesans3 = open('cumprimentos.txt').read().splitlines()
training_data_quesans5 = open('professores.txt').read().splitlines()
training_data_quesans6 = open('texto.txt').read().splitlines()
training_data_quesans7 = open('video.txt').read().splitlines()








training_data2 = training_data_quesans2
training_data3 = training_data_quesans3
training_data5 = training_data_quesans5
training_data6 = training_data_quesans6
training_data7 = training_data_quesans7



trainer = ListTrainer(chatbot)
trainer.train(training_data2)  
trainer.train(training_data3)
trainer.train(training_data5)  
trainer.train(training_data6)  
trainer.train(training_data7)  

#while True:
 #   request = input('You: ')
  #  response = chatbot.get_response(request)
   # print('Bot: ', response)