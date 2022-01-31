import telebot
from telebot import types


# -*- coding: utf-8 -*-


bot = telebot.TeleBot("5130694027:AAHuB3MM87ZQgRUO72SiCvxzyfkN2pNNt7s")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🛠 Разработчик")
    btn2 = types.KeyboardButton("👨‍👩‍👧‍👦 Sokolov")
    btn3 = types.KeyboardButton("📋 Прайс")
    btn4 = types.KeyboardButton("🎁 Кейсы")
    btn5 = types.KeyboardButton("🔝 Почему именно я?")
    btn6 = types.KeyboardButton("❓ Как я работаю?")
    btn0 = types.KeyboardButton("Главное меню")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)



    bot.send_message(message.chat.id,
    text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "🛠 Разработчик"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='ОТКРЫТЬ', url='https://t.me/sanya_sokolov')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "🛠 Alexandr Sokolov", reply_markup=markup)

    elif (message.text == "👨‍👩‍👧‍👦 Sokolov"):
        bot.send_message(message.chat.id, text="👨‍👩‍👧‍👦Продукты Alexandr Sokolov\nОтзывы - @sokolov_otzyv\nПомощник - @sanya_sokolov_bot\nВыплаты - @sokolov_oplata\nОтзывы о выплатах - @mailing_otzyv\nРабота - @alex_mailing_bot\nКонструктор - @sanya_sokolov_construct_bot\n" "Реферальная программа - t.me/alex_sokolov_bot?start=817306851\nЯ ВКонтакте - vk.com/sanya_sokolov_robot\nГруппа ВКонтакте - vk.com/sanya_sokolov_bot\nInstagram - instagram.com/portfolio_sokolov"                         )
    elif (message.text == "📋 Прайс"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton("❓Узнать цену уже готовых ботов", callback_data='good')
        btn_my_site2 = types.InlineKeyboardButton(text='🤖Заказать бота',url='https://t.me/sanya_sokolov')
        markup.add(btn_my_site)
        markup.add(btn_my_site2)
        bot.send_message(message.chat.id, "😕 Точного прайса нету. \n💰 Цена зависит от функционала бота.\n🤖 За простых чат-ботов (портфолио, документация...) 500₽ - 2000₽.\n🤖 За чат ботов средней сложности (вебинары, лид-магниты, продажи, реф. программы, матрицы) 2000₽ - 5000₽.\n❗️В эти категории попадают 95% ботов❗️\n\n🤖 За сложных ботов (глобальные игры, работа, криптовалюта, привязка к WEBhook и пр.) 5000₽ - 20 000₽", reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            try:
                if call.message:
                    if call.data == "good":
                        bot.send_message(call.message.chat.id, "t.me/annonimchatbot (Анонимный чат - 3000₽) \nt.me/prodaga_biletov_bot (Продажа билетов - 1000₽) \nt.me/install125_bot (Выполнение заданий за деньги - 1000₽)\nt.me/sagra8bot (Бот для документации садоводов - 2000₽)\nt.me/tehas_pro_bot (Агрегатор оборудования для СТО - 6000₽)\nt.me/Academy_Success_Togetherbot (Академия Успех Вместе - 2000₽)\nt.me/alex_test2881_bot (Реферальная программа Финико - 2000₽)\nt.me/yandex_eda2_bot (Поднятие рейтингов ресторанов - 2000₽)\nt.me/alex_sokolov_bot (Диалог с Александром Соколовым - 500₽)\nt.me/alex_mailing_bot (Работа - рассылка сообщений - 5000₽)\nt.me/Matrixtthebot (Покупка матриц - 5000₽)\nt.me/fame_up_bot (Накрутка подписчиков, лайков и др. - 2000₽)\nt.me/Petergoffparbot (Аренда бани - 4000₽)\nt.me/opIata_money_bot?start=500 (Оплата моих услуг - 1000₽)")
            except Exception as e:
                print(repr(e))

    elif (message.text == "🎁 Кейсы"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site3 = types.InlineKeyboardButton("🎁 Показать все кейсы", callback_data='good2')
        markup.add(btn_my_site3)
        bot.send_message(message.chat.id, text="🤖 Мои боты Telegram:\n\nt.me/annonimchatbot (Анонимный чат) \nt.me/prodaga_biletov_bot (Продажа билетов) \nt.me/GameWinMoneyBot (Игровой бот с возможностью выиграть деньги)\nt.me/sagra8bot (Бот для документации садоводов)\nt.me/Academy_Success_Togetherbot (Академия Успех Вместе)\nt.me/fame_up_bot (Накрутка подписчиков, лайков и др.)\nt.me/Matrixtthebot (Покупка матриц)", reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            try:
                if call.message:
                    if call.data == "good2":
                        bot.send_message(call.message.chat.id,
                                         "t.me/annonimchatbot (Анонимный чат) \nt.me/prodaga_biletov_bot (Продажа билетов) \nt.me/install125_bot (Выполнение заданий за деньги) \nt.me/GameWinMoneyBot (Игровой бот с возможностью выиграть деньги)\nt.me/sagra8bot (Бот для документации садоводов)\n" "t.me/tehas_pro_bot (Агрегатор оборудования для СТО)\nt.me/Academy_Success_Togetherbot (Академия Успех Вместе)\nt.me/B2BCHANGEBOT (Продажа криптовалюты) (Заказчик отключил бота)\nt.me/alex_test2881_bot (Реферальная программа Финико)\nt.me/yandex_eda2_bot " "(Поднятие рейтингов ресторанов)\nt.me/alex_sokolov_bot (Диалог с Александром Соколовым)\nt.me/alex_mailing_bot (Работа - рассылка сообщений)\nt.me/Matrixtthebot (Покупка матриц)\nt.me/MarketplacecentreBOT (Услуги для развития бизнеса) (Заказчик отключил бота)\nt.me/fame_up_bot (Накрутка подписчиков, лайков и др.)\nt.me/sofiya_5632_bot (Диалог с SMMщиком)\nt.me/sonia123_45_bot (Портфолио Софии)\nt.me/Grigorev_Design_Bot (Портфолио Павла)\nt.me/Grigorev_Send_Bot (Работа от Павла)\nt.me/Grigorev_Up_Bot?start=817306851 (Диалог с Павлом)\n" "t.me/help_freelance_bot (Помощь начинающим фрилансерам)\nt.me/Petergoffparbot (Аренда бани)\nt.me/opIata_money_bot?start=500 (Оплата моих услуг 500₽)\nt.me/trevel_money_bot (Призы за сканирование QR-кодов из видео)\nhttp://t.me/shoping_pro_bot (Покупка контактов поставщиков одежды)\nt.me/free_psychology_bot (Бесплатный бот, создан Александром Соколовым для оказания психологической помощи)\nt.me/ialb_bot (Сообщество Lashmakerов и Browистов)\nt.me/like_sgt_bot (Бот, для информирования участников Концентрата в Сургуте)\nt.me/guess_number2_bot (Угадай число, которое загадал бот)")
            except Exception as e:
                print(repr(e))
    elif (message.text == "🔝 Почему именно я?"):
        bot.send_message(message.chat.id, text="🛠 Я один из лучших разработчиков Telegram ботов в России.\n👨‍💻 За моими плечами несколько сотен чат-ботов и я буду рад создать Telegram бота для вашего бизнеса или личных целей\n🤖 Уже 5️⃣ лет я воплощаю идеи Заказчиков. Буду рад сделать чат-бота под ваши нужды.\n\n🤝Чат-Бот поможет:\n🔹Рассказать клиенту всю необходимую информацию о компании;\n🔹Автоматизировать многие процессы 24/7\n🔹Принять оплату товаров и услуг;\n🔹Записаться на приём, оставить заявку, собирать контактные данные;\n🔹Собрать все данные о клиенте в карточку;\n🔹И многое другое")
        #button1 = types.KeyboardButton("Привет")
        #markup.add(button1)


bot.polling(none_stop=True)