from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')
# Lista de conversa
conversa = ['oi','ola','Tudo Bem ?','Eu estou bem']
# Trainning
bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    quest = input("Voce: ")
    resposta = bot.get_response(quest)
    print ('Bot: ',resposta)