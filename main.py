from telebot import TeleBot, types
import secret

bot = TeleBot(secret.token)

def miniproject(filename):
    f = open(filename, 'r')
    MAClist = []
    List = []

    for line in f.readlines():
        List.extend(line.split())
    for c in List:
        if c not in MAClist:
            MAClist.append(c)
    return MAClist

d = miniproject("database.txt")

def data(filename):
    f = open(filename, 'r')
    List = []
    MAClist = []
    Studentlist = []
    
    for line in f.readlines():
        List.extend(line.split())
    a = len(List)
    b = {}
    for x in range(a - 1):
        if x%2 == 0:
            b[List[x+1]] = List[x]
    return b

a = data("databank.txt")

def check(L1,D1):
    list = ""
    count = 0
    for x in range(0,len(L1)):
        if L1[x] in D1:
            list = list + D1[L1[x]] + " is Present!\n"
            count += 1
    list=list + "Total: " + str(count) + " out of " + str(len(D1)) 
    return list
print(check(d,a))

lister=check(d,a)

def distance(lat,lon):
    kx = 51.1493317
    ky = 71.37946940000006
    result = ""

    mx = abs(lat - kx)
    my = abs(lon - ky)

    dist = (mx ** 2 + my ** 2) ** 0.5
    dist *= 100
    result = "You are "+str(dist)[0:4] + "km away from the university"
    return result



@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row(types.KeyboardButton('Student'))
    markup.row(types.KeyboardButton('Teacher'))
    bot.send_message(message.chat.id, "Hi! I wanna help you with attendance\n Press one of the buttons below\n Command list:\n /start - Starts me✨\n /distance - How far are you from the university👣\n /help - If you need any help❗️\n /team - Builders🔨", reply_markup=markup)

@bot.message_handler(content_types=['Student'])
def handle_student(message):
	bot.send_message(message.chat.id, "Enter your fullname please")


@bot.message_handler(func=lambda msg: msg.text == 'Teacher')
def handle_teacher(message):
	bot.send_message(message.chat.id, "Enter you password please")

def password(a):
    asd1 = 'ddagar123'
    for a in asd1:
        if a == 'ddagar123':
            return "Wait a sec.."
            break
        else:
            return "Enter a valid password"

@bot.message_handler(content_types=['text'])
def handle_teacher(message):
    global asd
    asd = message.text
    bot.send_message(message.chat.id, password(asd))


@bot.message_handler(func=lambda msg: msg.text == 'ddagar123')
def handle_teacher(message):
    bot.send_message(message.chat.id, lister)


@bot.message_handler(content_types= ['sticker'])
def handle_student(message):
    bot.send_message(message.chat.id, "Oh I see")


@bot.message_handler(commands=['distance'])
def handle_location(message):

    upd = bot.get_updates()
    last_update = upd[-1]
    msg_from_user = last_update.message
    location = msg_from_user.location
    longitude = location.longitude
    latitude = location.latitude

    bot.send_message(message.chat.id,distance(latitude,longitude))



@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id,'/distance - How far away you are\n /team - Builders\n /start - Start me again please')


@bot.message_handler(commands=['team'])
def handle_team(message):
    bot.send_message(message.chat.id, 'I am made by these awesome guys: Arystan🦁 Amanzhol🐎 Bibisara🌸 Abok👨‍💻\n')


bot.polling(none_stop=True, interval=0)