#Установите модуль ephem
#Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, например /ephem Mars
#В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
#При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater("659806032:AAEzxPcmOtNRtawBl_maB_zF4Nzxpz_oGFQ", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", what_constellation))
    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Hi! Give me some planet (ex. "/planet Mars")'
    print(text)
    update.message.reply_text(text)


def what_constellation(bot, update):
    user_text = update.message.text
    command, planet = user_text.split()
    today = datetime.datetime.today().strftime('%Y/%m/%d')
    try:
        body = getattr(ephem, planet)
        body = body(today)
        constellation = ephem.constellation(body)
        answer = '{} is in {} today'.format(planet, constellation[1])
        print(answer)
        update.message.reply_text(answer)
    except:
        print('Sorry, try smth else :(')
        update.message.reply_text('Sorry, try smth else :(')


main()
