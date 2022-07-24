import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup #можно обратиться не импортируя через types.ReplaykeyboardMarkup
from decouple import config
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config("BOT_TOKEN"))
@bot.message_handler(commands=["start"])
def get_start_message(message):
    text_message = f"Добро пожаловать {message.from_user.username} "
    bot.send_message(message.chat.id, text_message)
    if message.text.lower() == "/start":
        markup = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton("Подборка фильмов про дождь ", callback_data="01")
        button2 = types.InlineKeyboardButton("Подборка фильмов про малышей", callback_data="02")
        button3 = types.InlineKeyboardButton("Подборка фильмов про Гарри Поттера", callback_data="03")
        button4 = types.InlineKeyboardButton("Подборка сериалов про маньяков", callback_data="04")
        button5 = types.InlineKeyboardButton("Подборка фильмов с Эркюлем Пуаро", callback_data="05")
        button6 = types.InlineKeyboardButton("Подборка фильмов про Человека Паука", callback_data="06")
        button7 = types.InlineKeyboardButton("Подборка фильмов про Джет Ли", callback_data="07")
        button8 = types.InlineKeyboardButton("Подборка сериалов про ЛГБТ", callback_data="08")
        button9 = types.InlineKeyboardButton("Подборка фильмов про Уилла Смитта", callback_data="09")
        button10 = types.InlineKeyboardButton("Подборка фильмов про Леонардо Ди Каприо", callback_data="10")
        button11 = types.InlineKeyboardButton("Подборка фильмов про Тома Харди", callback_data="11")
        button12 = types.InlineKeyboardButton("Подборка фильмов про Джима Керри", callback_data="12")

        markup.add(button1, button2, button3, button4, button5, button6, button7,
                   button8, button9, button10, button11, button12)
    mess = f"<i>Выберите пожалуйста <b>подборку</b> фильмов :</i>"
    bot.send_message(message.chat.id, mess, parse_mode="HTML", reply_markup=markup)



HEADERS = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "accept": "*/*",
}

url = "https://www.film.ru/compilation/"
genre = {"01": "filmy-pro-dozhd",
         "02": "filmy-pro-malyshey",
         "03": "vse-filmy-vselennoy-garri-pottera",
         "04": "luchshih-serialov-pro-manyakov-i-seriynyh-ubiyc",
         "05": "vse-filmy-i-serialy-s-erkyulem-puaro",
         "06": "vse-filmy-o-cheloveke-pauke",
         "07": "15-luchshih-filmov-s-dzhetom-li",
         "08": "serialy-netfliks-ob-lgbt",
         "09": "vse-filmy-uilla-smita-ot-luchshego-k-hudshemu",
         "10": "15-luchshih-roley-leonardo-dikaprio",
         "11": "vse-filmy-toma-hardi-ot-luchshego-k-hudshemu",
         "12": "luchshie-filmy-s-dzhimom-kerri",
         }
img = "https://www.film.ru/"

def get_film(url,headers):
    req = requests.get(url)
    print(req)
    soup = BeautifulSoup(req.text, 'html.parser')
    pars = soup.find_all("div", class_="film_list")
    spisok = []
    for i in pars:
        # print(i.find('img'), "IMG")
        spisok.append({
            'Название': i.find('a', class_='film_list_link').find('strong').get_text().strip(),
            'Год':i.find('a', class_='film_list_link').get_text().split(',')[1].strip()[:4],
            'Рейтинг':i.find('a', class_='film_list_link').find('em').get_text(),
            'Фото': img + i.find('img').get('data-src'),
        })
    # year2 = spisok[0].get('Год').replace(" ", "")
    # print("AAAAAAAAAAAAAAAAA")
    # print(year2.split(',')[1].strip()[:4])
    # print("AAAAAAAAAAAAAAOAOAOAOAOAOAOOAOAOAOAO")
    return spisok

@bot.callback_query_handler(func=lambda call: True)
def get_call_data(call):
    if call.data == "01":
        final_url = url + genre["01"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')


            # bot.send_message(call.message.chat.id,f'{i["Название"]} , parse_mode='HTML')
            # bot.send_message(call.message.chat.id, f"{i['Фото']}")
    elif call.data == "02":
        final_url = url + genre["02"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "03":
        final_url = url + genre["03"]
        podborka = get_film(final_url, HEADERS)

        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "04":
        final_url = url + genre["04"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "05":
        final_url = url + genre["05"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "06":
        final_url = url + genre["06"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "07":
        final_url = url + genre["07"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "08":
        final_url = url + genre["08"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "09":
        final_url = url + genre["09"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "10":
        final_url = url + genre["10"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "11":
        final_url = url + genre["11"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')

    elif call.data == "12":
        final_url = url + genre["12"]
        podborka = get_film(final_url, HEADERS)
        for i in podborka:
            bot.send_message(call.message.chat.id, f'{i["Название"]} ' + f'Year: {i["Год"]} ' f'Ratio: {i["Рейтинг"]} ' + '[.]' + '(' + i['Фото'] + ')', parse_mode='markdown')





bot.polling()
