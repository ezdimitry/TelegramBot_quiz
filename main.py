import telebot

from asker import Asker

bot = telebot.TeleBot("5544500907:AAGN35ygS96Rn1ufl8o01OP3M5hbyKYYxJQ")

qst = [Asker.Question("2+2",
                      ["4", "22"], 0),
       Asker.Question("3+3",
                      ["6", "33", "9"], 0),
       Asker.Question("4+4",
                      ["44", "8"], 1),
       Asker.Question("сумма углов треугольника равна",
                      ["100", "120", "180", "360"], 2),
       Asker.Question("22+22",
                      ["2222", "44"], 1),
       Asker.Question("3*(3+2)",
                      ["15", "332"], 0),
       Asker.Question("55+45",
                      ["5545", "1685", "100"], 2)]


asker = Asker(qst)


def fromListToStr(lst):
    ret = ""
    for i in range(ord('a'), ord('a') + len(lst)):
        ret = ret + chr(i) + ") " + lst[i - ord('a')] + "\n"
    return ret


answs = []
start = False

def comeBack():
    global asker
    asker= Asker(qst)
    global answs
    answs = []
    global start
    start = False

def printQuestion(bot, message):
    bot.send_message(message.from_user.id,
                     asker.questions[asker.i].content + " \n" + fromListToStr(asker.questions[asker.i].answers))


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    global start
    global answs
    global asker
    if message.text == "/start":
        comeBack()
        bot.send_message(message.from_user.id, "Напишите Start, Чтобы начать викторину")
        return
    if message.text == "Start":
        printQuestion(bot, message)
        start = True
        return
    if start:
        answs.append(asker.questions[asker.i].check(ord(str(message.text).lower()[0]) - ord('a')))
        string = "не верный!"
        if answs[-1]:
            string = string[3:]
        bot.send_message(message.from_user.id, "Ответ " + string)
        asker.i += 1

        if asker.i == len(asker.questions):
            bot.send_message(message.from_user.id, "Ваш результат: " + str(100*(answs.count(True) / len(asker.questions))) + "%")
            comeBack()
            bot.send_message(message.from_user.id, "Чтобы пройти тест еще раз напишите Start")
        else:
            printQuestion(bot, message)


bot.polling(none_stop=True, interval=0)
