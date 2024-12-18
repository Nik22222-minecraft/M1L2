import telebot
import random
from bot_logic import gen_pass
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("Токен")
    
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """Что умеет этот бот: 
/start - Запуск бота
/heh - команда которая вскоре будет секретной(запомни команду)
/heh число - команда которая вскоре будет секретной(запомни команду)
/word - Модные слова
/password - Генерация рандомного пароля
                 """)

@bot.message_handler(commands=['word'])
def send_hello(message):
    
    bot.reply_to(message, """Модные слова:
Кринж - Что то странное или стыдное
Лол - что то очень смешное
Рофл - шутка
Щищ - одобрение или восторг
Криповый - страшный или пугающий
Агрится - злится
Токсик - агресивное, негативное поведение в онлайне
Спойлер - информация, которая раскрывает ключевые сюжетные повороты или концовку книги, фильма, игры и т.д.
""")

@bot.message_handler(commands=['password'])
def test(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.polling()




#Код номер 2:
import random
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
