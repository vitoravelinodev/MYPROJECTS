import telebot

CHAVE_API = "6191050162:AAEUpTRzX2w25E7x0K5XpmKNCGk17VBwxoU"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Escolher_1"])
def Escolher_1(mensagem):
      bot.send_message(mensagem.chat.id, "Aguarde, alguém da equipe irá realizar seu atendimento 🧑‍💻" )

@bot.message_handler(commands=["Escolher_2"])
def Escolher_2(mensagem):
      bot.send_message(mensagem.chat.id, "Aguarde, alguém da equipe irá realizar seu atendimento 🧑‍💻" )

@bot.message_handler(commands=["Escolher_3"])
def Escolher_3(mensagem):
      bot.send_message(mensagem.chat.id, "Aguarde, alguém da equipe irá realizar seu atendimento 🧑‍💻" )



@bot.message_handler(commands=["Selecionar_1"])
def Selecionar_1 (mensagem):
      texto = """
      Selecione um opção:
      /Escolher_1 Empréstimo consignado 💰 
      /Escolher_2 Empréstimo pessoal 💸
      /Escolher_3  Emprétimo com garantia no FGTS 💲"""
      bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Selecionar_2"])
def Selecionar_2(mensagem):
      texto = """
      Informe seu CPF e data de nascimento 📄"""
      bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Selecionar_3"])
def Selecionar_3(mensagem):
      texto = """
      Aguarde, um agente irá realizar seu atendimento 🧑‍💻"""
      bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
       return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá! Sou o assistente virtual da InfinityCred.
    Escolha uma opção:
    /Selecionar_1 Ver opções de empréstimo 🤑 
    /Selecionar_2 Andamento de solicitação 🕗
    /Selecionar_3 Falar com atendente 📞 """ 
    bot.reply_to(mensagem, texto)

bot.polling()
