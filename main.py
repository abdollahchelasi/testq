#!pip install pyTelegramBotAPI
#!pip install telegram-menu
#!pip install --upgrade pip

import telebot
from telebot.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton
from telebot import types


from keep_alive import keep_alive

keep_alive()


TOKEN = '6536915386:AAHcuUYghP-ZGilGD7WeT6o_NzGzJjZwS2U'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

    menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    # Add buttons to the menu
    button1 = KeyboardButton('⛪️ اتاق ها')
    button2 = KeyboardButton('🌊 ساحل')
    button3 = KeyboardButton('📞 جهت رزرو تماس بگیرید')
    button4 = KeyboardButton('🌈  مراسمات')
    button5 = KeyboardButton('سوال')
    button6 = KeyboardButton('👨🏻‍🍳 رستوران')
    button7 = KeyboardButton('🍫  کافی شاپ')
    button8 = KeyboardButton('💲 قیمت اتاق ها')

    menu.add(button1, button2, button6, button7)
    menu.add(button3, button4)
    menu.add(button8)
    menu.add(button5)

    ph = open("logo.jpeg", 'rb')

    bot.send_photo(message.chat.id, ph, caption="""

                    < به هتل ساحل طلایی خوش اومدید >
هتل ساحل طلایی در 11 کیلومتری قشم است. این هتل قبل‌ها به ساحل سیمین یا پلاژ سیمین معروف بوده. هتل ساحل طلایی از همه نظر هتلی بی‌نظیر در قشم است و طیف گسترده‌ای از خدمات و امکانات را در اختیار مسافران قرار می‌دهد. ساحل اختصاصی هتل بسیار تمیز و خلوت است  علاوه بر این‌ها مسافران می‌توانند لذت ماهیگیری  را در اسکله‌ی تفریحی هتل تجربه کنند. 
این هتل کمتر از ۲۰ دقیقه با یکی از جاذبه‌های شگفت‌انگیز قشم فاصله دارد. دره‌ی ستاره‌ها با قدمتی دو میلیون ساله، یکی از جاذبه‌های طبیعی قشم است که صحبت از آن همیشه با داستان‌ها و گاهی خرافه‌های جالبی همراه بوده. اقامت در هتل ساحل طلایی و بازدید از این نقاط دیدنی می‌تواند بدل به یکی از بهترین تجربیات مسافران قشم شود.
        --------------------------------------------------
                        /start
        --------------------------------------------------

        لطفا گزینه مورد نظر رو انتخاب کنید

    """, reply_markup=menu)





@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "🌈  مراسمات":
        bot.send_message(message.chat.id, """
        🌈 ما در هتل ساحل طلایی جشن تولد و مراسمات عقد شاد و به یادماندنی برای شما آماده کرده‌ایم. از طراحی دکوراسیون زیبا و نورپردازی شگفت‌انگیز تا منوی لذیذ و خدمات عالی، همه چیز برای شما تدارک دیده شده است. 🌈
        """)
        s = "https://qeshm-online.com/wp-content/uploads/2023/06/60d6cd63-e18c-4372-9c71-8e711aafd5db.jpg"

        ss = "https://cdn.jabama.com/image/jabama-images/1681067/546a3a65-8471-470e-a5b3-de7877349181.jpg"

        sss = "https://cdn.jabama.com/image/jabama-images/1681067/36a761f0-2cc2-4012-aabd-6b7ce5425d01.jpg"

        ssss = "https://cdn.jabama.com/image/jabama-images/1681067/4884c638-ae84-48c3-baf9-a419d13be18f.jpg"


        sssss = "https://cdn.jabama.com/image/jabama-images/1681067/e75c99fa-02cd-4d22-8e58-3a85b451f131.jpg"

        
      
        bot.send_photo(message.chat.id,s, caption= """
             =========================
                         /start
             =========================
        """)


        bot.send_photo(message.chat.id,ss, caption= """
             =========================
                         /start
             =========================
        """)



        bot.send_photo(message.chat.id,sss, caption= """
             =========================
                         /start
             =========================
        """)

        bot.send_photo(message.chat.id,ssss, caption= """
             =========================
                         /start
             =========================
        """)



        bot.send_photo(message.chat.id,sssss, caption= """
             =========================
                         /start
             =========================
        """)

  


    elif message.text == "⛪️ اتاق ها":

        bot.send_message(message.chat.id, """
       ⛪️  این هتل دارای { اتاق های یک خوابه 4 تخته ,  اتاق های 3 تخته , دو خوابه 6 تخته , یک خوابه 5 تخته , دوبلکس 8 تخته , دوبلکس 6 تخته } ⛪️
        """)
        
        s = open("o1.jpg", "rb")
        bot.send_photo(message.chat.id,s, caption= """
       اتاق های هتل

       =========================
                   /start
       =========================
        """)



    elif message.text == "🌊 ساحل":

        bot.send_message(message.chat.id, """
       🌊 با نگاهی به این نمای ساحل دریا، شما می‌توانید امواج آرام و زیبای دریا را مشاهده کنید 🌊
        """)
        s = "https://ariabooking.ir//safar/upload/images/iran/saeheltalaei-hotel-qashem/saheltgalaei-hotel-gheshm17.jpg"
        bot.send_photo(message.chat.id,s, caption= """

        =========================
                    /start
        =========================
        """)


    elif message.text == "👨🏻‍🍳 رستوران":

        bot.send_message(message.chat.id, """
          👨🏻‍🍳 رستوران ساحل طلایی با انواع غذاهای دریایی 👨🏻‍🍳
        """)
        s = "https://www.homsa.net/images/rooms/11855/156120409234_.jpeg"
        ss = "https://ariabooking.ir//safar/upload/images/iran/saeheltalaei-hotel-qashem/saheltgalaei-hotel-gheshm13.jpg"
        bot.send_photo(message.chat.id,s, caption= """

        =========================
                    /start
        =========================
        """)

        bot.send_photo(message.chat.id,ss, caption= """

        =========================
                    /start
        =========================
        """)



    elif message.text == "🍫  کافی شاپ":

       
        s = open("cc.jpg", "rb")
        bot.send_photo(message.chat.id,s, caption= """
             🍫  انواع نوشیدنی سرد و گرم , شکلات های خارجی و ایرانی و انواع لواشک های عربی و ایرانی 🍫  


             =========================
                         /start
             =========================

        """)

        # bot.send_message( message.chat.id,"=========================================")





    elif message.text == "📞 جهت رزرو تماس بگیرید":
        bot.send_message(message.chat.id, "📞 جهت رزرو تماس بگیرید")
        photo = open("logo.jpeg", 'rb')
        bot.send_photo(message.chat.id, photo, caption="""
        شماره تماس : 09025342900 📞
        ===========================
www.goldenbeachhotel.ir:وبسایت🌐


=========================
            /start
=========================
       """)


    elif message.text == "💲 قیمت اتاق ها":
            bot.send_message(message.chat.id, "در حال بررسی قیمت اتاق ها ...")
            s = open("q.jpg", "rb")
            bot.send_photo(message.chat.id,s, caption= """
                قیمت اتاق ها 🏠
            """)



    elif message.text == "سوال" or "/Questions":

        markup = types.InlineKeyboardMarkup()
        itembtn2 = types.InlineKeyboardButton('اتاق ها رو به دریا هستند ؟ 🏠', callback_data='b2')
        itembtn4 = types.InlineKeyboardButton('آیا پارکینگ دارد ؟ 🅿️', callback_data='b4')
        itembtn5 = types.InlineKeyboardButton('رستوران چه ساعتی باز میشه ؟ 👨🏽‍🍳', callback_data='b5')
        itembtn6 = types.InlineKeyboardButton('کافی شاپ چه ساعتی باز میشه ؟ ☕', callback_data='b6')
        itembtn9 = types.InlineKeyboardButton('آیا آلاچیق هم وجود دارد ؟ 🛖', callback_data='b9')
        itembtn13 = types.InlineKeyboardButton('تور گردشگری هم دارید ؟ 🚕', callback_data='b13')                       
        itembtn14 = types.InlineKeyboardButton('آدرس هتل شما کجاست ؟ 📍', callback_data='b14')



        markup.add(itembtn2)
        markup.add(itembtn4)
        markup.add(itembtn5)
        markup.add(itembtn6)
        markup.add( itembtn9)
        markup.add(itembtn13)
        markup.add(itembtn14)


        bot.send_message(message.chat.id, """
        📞 سوال های خودتان رو ارسال کنید
        =========================
                    /start
        =========================
        """, reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
          
            if call.data == 'b2':
                bot.send_message(call.message.chat.id, """
                بله ! تمامی اتاق ها رو به دریا هستند 🏠
                
==================================
برای سوالات خود اسم < سوال > را ارسال کنید یا روی این /Questions بزنید
                  /Questions ❓
==================================
                
                """)


                


            elif call.data == 'b4':
                bot.send_message(call.message.chat.id, """
                بله ! پارکینگ وجود دارد 🅿️

    ====================================
برای سوالات خود اسم < سوال > را ارسال کنید یا روی این /Questions بزنید
                  /Questions ❓
==================================
                """)


            elif call.data == 'b5':
                bot.send_message(call.message.chat.id, """
                          👨🏽‍🍳
                رستوران برای صبحانه 8 الی 9:30
                و برای ناهار ساعت 13 الی 15:30
                و برای شام 20:30 الی 23:00
                باز است

                ==================================
برای سوالات خود اسم < سوال > را ارسال کنید یا روی این /Questions بزنید
                  /Questions ❓
==================================
                """)



            elif call.data == 'b6':
                bot.send_message(call.message.chat.id, """
                        کافی شاپ صبح 11 الی 13 باز است و عصر از ساعت 16 الی 23 باز است ☕

==================================
برای سوالات خود اسم < سوال > را ارسال کنید یا روی این /Questions بزنید
                  /Questions ❓
==================================
                """)

           

            elif call.data == 'b9':
                bot.send_message(call.message.chat.id, """  
                بله آلاچیق های کولردار و بدون کولر لب ساحل قرار دارد که میتونید صدای امواج دریا را گوش کنید 🛖
                
                ==================================
برای سوالات خود اسم < سوال > را ارسال کنید یا روی این /Questions بزنید
                  /Questions ❓
==================================
                """)


           


            

            elif call.data == 'b13':

              bot.send_message(call.message.chat.id, """
            
            بله , تور گردشگری داریم 🚕
              
             ==================================
برای سوالات خود اسم < سوال > را ارسال کنید یا روی این /Questions بزنید
                  /Questions ❓
==================================
              """)



          

            elif call.data == 'b14':

              bot.send_message(call.message.chat.id, """
              جزیره قشم - جاده ساحل جنوبی , رمچاه ( روبروی زیارتگاه شاه شهید و غار خربس ) 📍
              هتل ساحل طلایی قشم
              
              ==================================
برای سوالات خود اسم < سوال > را ارسال کنید یا روی این /Questions بزنید
                  /Questions ❓
==================================
              """)









bot.polling()





# 6536915386:AAHcuUYghP-ZGilGD7WeT6o_NzGzJjZwS2U