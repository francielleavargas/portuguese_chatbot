# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer 
from chatterbot import ChatBot

bot = ChatBot('Test')

#Pode carregar uma lista externa
conv = ['Ola', 'Ola! Ha quanto tempo nao nos vemos!',
'Obrigada!', 'Voces planejam ter filhos?',
'Sim, mas nao agora', 'Por que nao?']

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
	quest = str(raw_input('Voce: ')) #Entrada do usuário
	response = str(bot.get_response(quest))
	print('Bot: ', response)