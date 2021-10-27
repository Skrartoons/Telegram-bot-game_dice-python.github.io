import telebot
import random

bot = telebot.TeleBot("Token")

list1 = ['⚀','⚁','⚂','⚃','⚄','⚅']

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, 'Здравствуйте.'+'\n'+'Чтобы узнать мои возможности напишите или нажмите: /help')

@bot.message_handler(commands=['help'])
def help_menu(message):
    bot.send_message(message.chat.id, 'Чтобы управлять мной, смотрите список команд тут:'+'\n'+'/help - список команд'+'\n'+'/play - начать играть')

def get_random_no():
    q1 = random.randint(0, 5)
    a, b, c, d = q1, q1, q1, q1
    return a
    return b
    return c
    return d

@bot.message_handler(commands=['play'])
def player_1(message):
    bot.send_message(message.chat.id, 'Введите имя первого игрока: ')
    bot.register_next_step_handler(message, player_2)

def player_2(message):
    global player1
    player1 = message.text
    bot.send_message(message.chat.id, 'Введите имя второго игрока: ')
    bot.register_next_step_handler(message, dice)

def dice(message):
    a, b, c, d = get_random_no(), get_random_no(), get_random_no(), get_random_no()
    a1 = a + 1
    b1 = b + 1
    c1 = c + 1
    d1 = d + 1
    player1_random = int(a1) + int(b1)
    player2_random = int(c1) + int(d1)
    player2 = message.text
    if player1_random > player2_random:
        bot.send_message(message.chat.id, '🎲Вы бросили кости на стол: ' + '\n' + '\n' + str(player1) + ": " + str(list1[a]) + " + " + str(list1[b]) + ' (' + str(player1_random) + ')' + '\n' + str(player2) + ": " + str(list1[c]) + " + " + str(list1[d]) + ' (' + str(player2_random) + ')' + '\n' + '\n' + 'В игре, как и на войне, нужна удача. Сегодня её внимания удостоился ' + str(player1) + '. ' + str(player2) + ' остался без 💰.' + '\n' + '\n' + 'Начать заново: /play')
    elif player1_random < player2_random:
        bot.send_message(message.chat.id, '🎲Вы бросили кости на стол: ' + '\n' + '\n' + str(player1) + ": " + str(list1[a]) + " + " + str(list1[b]) + ' (' + str(player1_random) + ')' + '\n' + str(player2) + ": " + str(list1[c]) + " + " + str(list1[d]) + ' (' + str(player2_random) + ')' + '\n' + '\n' + 'В игре, как и на войне, нужна удача. Сегодня её внимания удостоился ' + str(player2) + '. ' + str(player1) + ' остался без 💰.' + '\n' + '\n' + 'Начать заново: /play')

bot.polling(none_stop=True)
