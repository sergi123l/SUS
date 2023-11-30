import telebot 
from config import token
from random import randint
from logic import Pokemon , Figher , Wizzard

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        del Pokemon.pokemons[message.from_user.username]
    chance= randint(1,3)
    if chance == 1 :
        pokemon = Pokemon(message.from_user.username)
    elif chance == 2 :
        pokemon = Figher(message.from_user.username)
        bot.send_message(message.chat.id,'Класс боец')
    else :
        pokemon = Wizzard(message.from_user.username)
        bot.send_message(message.chat.id,'Класс маг')
    bot.send_message(message.chat.id, pokemon.info())
    bot.send_photo(message.chat.id, pokemon.show_img())

@bot.message_handler(commands=['sus'])
def stat(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_photo(message.chat.id, pokemon.sas())
    else:
        bot.reply_to(message, "Ты ещё не создал себе покемона(/go)")

@bot.message_handler(commands=['sila'])
def stut(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_photo(message.chat.id, pokemon.sad())
    else:
        bot.reply_to(message, "Ты ещё не создал себе покемона(/go)")
        
@bot.message_handler(commands=['attack'])
def attaack(message):
    if message.reply_to_message:
        if message.from_user.username in Pokemon.pokemons.keys():
            if message.reply_to_message.from_user.username in Pokemon.pokemons.keys():
                pokemon = Pokemon.pokemons[message.from_user.username]
                enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
                m = pokemon.attack(enemy) 
                bot.reply_to(message, m)
@bot.message_handler(commands=['hill'])
def hil(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        m = pokemon.hill()
        bot.reply_to(message, m)


@bot.message_handler(commands=['pokem'])
def pok(message):
    if message.reply_to_message:
        if message.from_user.username in Pokemon.pokemons.keys():
            if message.reply_to_message.from_user.username in Pokemon.pokemons.keys():
                pokn = Pokemon.pokemons[message.from_user.username]
                g = 0
                if Ba > se:
                    g = ">"
                    pass
                elif Ba < se:
                    g = "<"
                    pass
                else: # если равны
                    g = "="
                    pass
                bot.reply_to(message, g)



bot.infinity_polling(none_stop=True)

