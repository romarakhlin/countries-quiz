# coding: utf-8

from __future__ import unicode_literals
import json
import logging
from flask import Flask, request



app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

sessionStorage = {}

@app.route("/", methods=['POST'])



# главная функция
def main():
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
        "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )



# задаём переменнцю n, для определения ошибок
n = 0
sost = 0



# обработка диалога
def handle_dialog(req, res):
    global n

    user_id = req['session']['user_id']

    # если сессия началась, спрашивать первую страну
    if req['session']['new'] == True:
        res['response']['text'] = 'Чтобы начать - "Начать" \nПодробнее о навыке - "Помощь"'
        return

    if req['session']['new'] == False:
        if req['request']['original_utterance'].lower() in ['помощь', 'что ты умеешь?']:
            res['response']['text'] = 'При запуске навыка, начинается тест. В тесте появляется картинка (флаг страны), а игроку нужно назвать, какой стране принадлежит флаг. Если пользователь ошибся, ему будет предложено изучить флаг, на котором он ошибся. Предлагается переход на Википедию с информацией о флаге страны и его историей. \n\nЧтобы начать - "Начать"'
            return
        elif req['request']['original_utterance'].lower() in ['начать']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '965417/0a0af31ba1b502d43069', 'title': 'Что это за страна?'}
            return

        if req['request']['original_utterance'].lower() in ['канада']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/00073bc55582d708708c', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['великобритания', 'британия', 'объеденённое королевство']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1540737/88616bf537494dbdac49', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['япония']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1540737/eba0aa9dca96e97107ae', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['сша', 'соединенные штаты америки', 'штаты']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '213044/e1317cc107cb038865e5', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['франция']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/d130778b25b2e035fe82', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['германия']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/0b1c007fe853f883a919', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['бразилия']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1540737/02acd8b91fc471c435f6', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['италия']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1540737/55af67683048e3113482', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['южная корея', 'корея']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/cbd436c2ea8ac7ef4e1b', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['австралия']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1540737/672f76184e5cb9b6aea7', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['китай']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/2004ee85d75e554e0620', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['израиль']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '965417/a74f0f148bc670c2f160', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['швейцария']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1540737/6917966a3b53c8c5a952', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['дания']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/ee0e03a4b4891ef22e60', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['аргентина']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/48b188bc3dd65569212a', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['норвегия']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/86d82c0c74b222a5b65a', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['греция']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1540737/cdbcd4a09d5ccffe7821', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['новая зеландия']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1540737/86ed2f1bff43addadee2', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['швеция']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/4e06a093249aa2690333', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['финляндия']:
            n += 1
            res['response']['text'] = 'text'
            res['response']['card'] = {'type': 'BigImage', 'image_id': '1652229/4ddb1577d16c696ac9c1', 'title': 'Правильно! \n\nА это какая?'}
            return
        elif req['request']['original_utterance'].lower() in ['испания']:
            n += 1
            res['response']['text'] = 'Правильно! \nЭто был последний вопрос \n\nВы указали указали все страны верно! Вы молодец!!'
            return
        else:
            if n == 0: 
                res['response']['text'] = 'Для прохождения теста заново \nПерезапустите Навык'
                return 
            elif n == 1: 
                sessionStorage[user_id] = {'suggests': ['История Канады']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Канады \nЧтобы узнать историю флага Канады - "История Канады"'
                res['response']['buttons'] = get_suggests(user_id)
                sessionStorage[user_id] = {}
                n = 0
                return 
            elif n == 2: 
                sessionStorage[user_id] = {'suggests': ['История Великобритании']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' страну из 21 \n\n\nВы ошиблись с Флагом Великобритании \nЧтобы узнать историю флага Великобритании - "История Великобритании"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 3:
                sessionStorage[user_id] = {'suggests': ['История Японии']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' страны из 21 \n\n\nВы ошиблись с Флагом Японии \nЧтобы узнать историю флага Японии - "История Японии"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 4:
                sessionStorage[user_id] = {'suggests': ['История США']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' страны из 21 \n\n\nВы ошиблись с Флагом США \nЧтобы узнать историю флага США - "История США"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 5:
                sessionStorage[user_id] = {'suggests': ['История Франции']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' страны из 21 \n\n\nВы ошиблись с Флагом Франции \nЧтобы узнать историю флага Франции - "История Франции"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 6:
                sessionStorage[user_id] = {'suggests': ['История Германии']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Германии \nЧтобы узнать историю флага Германии - "История Германии"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 7:
                sessionStorage[user_id] = {'suggests': ['История Бразилии']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Бразилии \nЧтобы узнать историю флага Бразилии - "История Бразилии"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 8:
                sessionStorage[user_id] = {'suggests': ['История Италии']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Италии \nЧтобы узнать историю флага Италии - "История Италии"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 9:
                sessionStorage[user_id] = {'suggests': ['История Южной Кореи']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Южной Кореи \nЧтобы узнать историю флага Южной Кореи - "История Южной Кореи"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 10:
                sessionStorage[user_id] = {'suggests': ['История Австралии']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Австралии \nЧтобы узнать историю флага Австралии - "История Австралии"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 11:
                sessionStorage[user_id] = {'suggests': ['История Китая']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Китая \nЧтобы узнать историю флага Китая - "История Китая"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 12:
                sessionStorage[user_id] = {'suggests': ['История Израиля']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Израиля \nЧтобы узнать историю флага Израиля - "История Израиля"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 13:
                sessionStorage[user_id] = {'suggests': ['История Швейцарии']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Швейцарии \nЧтобы узнать историю флага Швейцарии - "История Швейцарии"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 14:
                sessionStorage[user_id] = {'suggests': ['История Дании']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Дании \nЧтобы узнать историю флага Дании - "История Дании"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 15:
                sessionStorage[user_id] = {'suggests': ['История Аргентины']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Аргентины \nЧтобы узнать историю флага Аргентины - "История Аргентины"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 16:
                sessionStorage[user_id] = {'suggests': ['История Норвегии']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Норвегии \nЧтобы узнать историю флага Норвегии - "История Норвегии"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 17:
                sessionStorage[user_id] = {'suggests': ['История Греции']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Греции \nЧтобы узнать историю флага Греции - "История Греции"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 18:
                sessionStorage[user_id] = {'suggests': ['История Новой Зеландии']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Новой Зеландии \nЧтобы узнать историю флага Новой Зеландии - "История Новой Зеландии"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 19:
                sessionStorage[user_id] = {'suggests': ['История Швеции']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Швеции \nЧтобы узнать историю флага Швеции - "История Швеции"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 20:
                sessionStorage[user_id] = {'suggests': ['История Финляндии']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Финляндии \nЧтобы узнать историю флага Финляндии - "История Финляндии"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return
            elif n == 21:
                sessionStorage[user_id] = {'suggests': ['История Испании']}
                res['response']['text'] = 'К сожалению Неправильно \nВы назвали правильно '  + str(n - 1) + ' стран из 21 \n\n\nВы ошиблись с Флагом Испании \nЧтобы узнать историю флага Испании - "История Испании"'
                res['response']['buttons'] = get_suggests(user_id)
                n = 0
                sessionStorage[user_id] = {}
                return



# функция для кнопок
def get_suggests(user_id):
    if sessionStorage[user_id] == {'suggests': ['История Канады']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Канады', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Великобритании']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Великобритании', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Японии']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Японии', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История США']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Соединённых_Штатов_Америки', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Франции']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Франции', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Германии']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Германии', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Бразилии']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Бразилии', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Италии']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Италии', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Южной Кореи']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Республики_Корея', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Австралии']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Австралии', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Китая']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Китая', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Израиля']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Израиля', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Швейцарии']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Швейцарии', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Дании']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Дании', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Аргентины']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Аргентины', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Норвегии']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Норвегии', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Греции']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Греции', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Новой Зеландии']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Новой_Зеландии', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Швеции']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Швеции', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Финляндии']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Финляндии', 'hide': True} for suggest in session['suggests']]
        return suggests
    elif sessionStorage[user_id] == {'suggests': ['История Испании']}:
        session = sessionStorage[user_id]
        suggests = [{'title': suggest, 'url': 'https://ru.wikipedia.org/wiki/Флаг_Испании', 'hide': True} for suggest in session['suggests']]
        return suggests

